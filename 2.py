import pandas as pd

df = pd.read_csv('/Users/v/Desktop/Kshema/Polygons/polygonfolder/polygons.csv')
poly_data = (df['wkt_geom'])

# print(poly_data)
polygons_id = []
final_lat=[]
final_long=[]
cnt=0
polygons = []
for p in poly_data:
	p=p.replace("MultiPolygon (((","")
	p=p.replace(")","")
	p= p.split(",")
	# print(p)
	polygons_id.append(cnt)
	for i in p:
		if i[0]==" ":
			lat=i.split(" ")[1]
			lon=i.split(" ")[2]
		else:
			lat=i.split(" ")[0]
			lon=i.split(" ")[1]
	poly = (zip(lat,lon))
	polygons.append(poly)
	final_lat.append(lat)
	final_long.append(lon)
	cnt+=1
	# print(p)
# print(len(final_lat))
# print(len(final_long))
for l in polygons:
	print(l)
	for j,k in l:
		print(j,k)

# poly = (zip(final_lat,final_long))
# print(poly)
# for i,j in poly:
# 	print(i,j)
