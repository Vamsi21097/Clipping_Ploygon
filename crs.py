import rasterio as rio
def reproject_raster(in_path, out_path):

    """
    """
    # reproject raster to project crs
    with rio.open(in_path) as src:
        src_crs = src.crs
        transform, width, height = calculate_default_transform(src_crs, crs, src.width, src.height, *src.bounds)
        kwargs = src.meta.copy()

        kwargs.update({
            'crs': crs,
            'transform': transform,
            'width': width,
            'height': height})

        with rio.open(out_path, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rio.band(src, i),
                    destination=rio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=crs,
                    resampling=Resampling.nearest)
    return(out_path)


in_path = '/Users/v/Desktop/Kshema/Polygons/polygonfolder/T43PER_20191103T052001.tif'
out_path = '/Users/v/Desktop/Kshema/Polygons/polygonfolder/output.tif'

print(reproject_raster(in_path,out_path))