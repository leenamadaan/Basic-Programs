'''from pathlib import Path
import os
from PIL import Image


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    
    
        convert_mb = megabyte * input_kilobyte"""
        
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		megabyte = float(0.000976562)
		return ('{0:.2f}'.format(megabyte*num/1024))

def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
		file_info = os.stat(file_path)
		print(file_info.st_size)
		return convert_bytes(file_info.st_size)
    		
			
    
  
# Lets check the file size of MS Paint exe 
# or you can use any file path
file_path =r"/var/www/html/s3/Clocktower_Panorama_20080622_20mb.jpg"
print file_size(file_path)
'''
'''
from pathlib import Path
import os
from PIL import Image
folder_images="/var/www/html/s3/"
size_images=dict()
for dirpath, _, filenames in os.walk(folder_images):
	for path_image in filenames:
		image=os.path.abspath(os.path.join(dirpath,path_image))
		with Image.open(image) as img:
			width, height=img.size
			size_images[path_image]={'width':width,'height':height}
			
print(size_images)
'''




import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
   
print(convert_size(18462554))   
