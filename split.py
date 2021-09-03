import glob
import fiona
import pandas as pd
from subprocess import Popen
import csv
li = []
c =0
with fiona.open('/Users/v/Desktop/Kshema/New1/1ad100.shp', 'r') as dst_in:
	print((dst_in))
	# i = 100
	for index, feature in enumerate(dst_in):
		print(index,feature)
	# 	if index == i:
	# 		# print("hello",i)
	# 		i = i + 100
		
	# 		with fiona.open('/Users/v/Desktop/Kshema/New1/1ad{}.shp'.format(index), 'w', **dst_in.meta) as dst_out:
	# 			dst_out.write(feature)
	# 			break
