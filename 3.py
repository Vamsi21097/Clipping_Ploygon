
import geopandas 

poly = geopandas.read_file(r'/Users/v/Desktop/Kshema/Polygons/polygonfolder/final version polygons.shp')


#determine projection for shape and change it into the image projection
poly.crs = {'init' :'epsg:4326'}
poly=poly.to_crs(epsg = 32643)

#Load image
img=rasterio.open(r'what\a\wonderful\path\image.tif')