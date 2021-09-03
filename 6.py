# import ogr
import subprocess
from osgeo import ogr

inraster = '/Users/v/Desktop/Kshema/Polygons/polygonfolder/T43PER_20191103T052001.tif'
inshape = '/Users/v/Desktop/Kshema/Polygons/polygonfolder/final version polygons.shp'

ds = ogr.GetDriverByName(inshape)
lyr = ds.GetLayer(0)

lyr.ResetReading()
ft = lyr.GetNextFeature()

while ft:

    country_name = ft.GetFieldAsString('admin')

    outraster = inraster.replace('.tif', '_%s.tif' % country_name.replace(' ', '_'))    
    subprocess.call(['gdalwarp', inraster, outraster, '-cutline', inshape, 
                     '-crop_to_cutline', '-cwhere', "'admin'='%s'" % country_name])

    ft = lyr.GetNextFeature()

ds = None