import gdal

# gdalwarp -dstnodata -9999 -cutline data/shapefile.shp data/input.tif data/output.tiff


# from osgeo import gdal, ogr

OutTile = gdal.Warp("/Users/v/Desktop/Kshema/Polygons/polygonfolder/cut.tif", 
                    "/Users/v/Desktop/Kshema/Polygons/polygonfolder/T43PER_20191103T052001.tif", 
                    cutlineDSName='/Users/v/Desktop/Kshema/Polygons/polygonfolder/final version polygons.shp',
                    cropToCutline=True,
                    dstNodata = 0)

OutTile = None 

 