import mysql.connector

mycon=mysql.connector.connect(host="Localhost", user="root", passwd="ztech@44", db="Student")
print(mycon	)
cur=mycon.cursor()
print(cur)
try:
	dbs=cur.execute("Show databases")
except:
	mycon.rollback()
	
for x in cur:
	print(x)

'''
from pathlib import Path
import os
from PIL import Image
entries=Path('/var/www/html/s3/')
size_images=dict()
for entry in entries.iterdir():
	if entry.is_file():
		print(entry.name)
        
