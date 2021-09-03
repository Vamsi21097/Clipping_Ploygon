import pandas as pd
from shapely.geometry import Polygon
import rasterio
import rasterio.mask
from matplotlib import pyplot
from rasterio.plot import show

polygons = []
df = pd.read_csv('/Users/v/Desktop/Kshema/Polygons/polygonfolder/polygons.csv')

for id, p in df.groupby('id'):

    poly = Polygon(zip(p.x,p.y)) #
    polygons.append(poly)

with rasterio.open("/Users/v/Desktop/Kshema/Polygons/polygonfolder/T43PER_20191103T052001.tif") as src:
    out_image, out_transform = rasterio.mask.mask(src, polygons, crop=True)
    out_meta = src.meta
    out_meta.update({"driver": "GTiff",
         "height": out_image.shape[1],
         "width": out_image.shape[2],
         "transform": out_transform})

    with rasterio.open("LC_masked.tif", "w", **out_meta) as dest:
        dest.write(out_image)

#showing the results
src=rasterio.open("LC.tif")
masked = rasterio.open("LC_masked.tif")
fig, (ax1, ax2) = pyplot.subplots(1,2, figsize=(21,7))   
show((src, 1), ax=ax1, title='Original')
show((masked, 1), ax=ax2, title='Masked')
pyplot.show()