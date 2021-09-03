import fiona
import rasterio
import shapely.geometry
import numpy as np

from rasterstats.io import Raster
from PIL import Image


tif_filename = '/Users/v/Desktop/Kshema/Polygons/polygonfolder/T43PER_20191103T052001.tif'
with Raster(tif_filename, band=1) as raster_obj_1:
    with Raster(tif_filename, band=2) as raster_obj_2:
        with Raster(tif_filename, band=3) as raster_obj_3:
            index = 0
            for feat in fiona.open('/Users/v/Desktop/Kshema/Polygons/polygonfolder/final version polygons.shp'):
                polygon_geometry = feat['geometry']
                polygon = shapely.geometry.Polygon(polygon_geometry['coordinates'][0])
                polygon_bounds = polygon.bounds

                raster_subset_1 = raster_obj_1.read(bounds=polygon_bounds)
                polygon_mask = rasterio.features.geometry_mask(geometries=[polygon_geometry],
                                                    out_shape=(raster_subset_1.shape[0],raster_subset_1.shape[1]),
                                                    transform=raster_subset_1.affine,
                                                    all_touched=False,
                                                    invert=True)

                raster_subset_2 = raster_obj_2.read(bounds=polygon_bounds)
                raster_subset_3 = raster_obj_3.read(bounds=polygon_bounds)

                masked_1 = raster_subset_1.array * polygon_mask
                masked_2 = raster_subset_2.array * polygon_mask
                masked_3 = raster_subset_3.array * polygon_mask

                masked_all = np.dstack([masked_1, masked_2, masked_3])

                img = Image.fromarray(masked_all[:, :, :].astype('uint8'), 'RGB')
                img.save('out/' + str(index) + '.jpg')
                index += 1