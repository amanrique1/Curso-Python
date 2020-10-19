import PIL, os
from PIL import Image
cwd = os.getcwd() 
  
# print the current directory 
print("Current working directory is:", cwd) 
#os.chdir('d:\Users\Andres3\Documents\WEB\periodontograma\public\assets\img\interior') # change to directory where image is located

picture= Image.open('11.png')

picture.rotate(180, expand=True).save('18_rotated.png')
