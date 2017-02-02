# Author: Honorio Vega
# Date : 01/31/2017
# using python3
# import our media file functions.py
from PIL import Image
from project_1_functions import removeObstruction

def main():
    
    picturesInfo = {'path' : 'Project1Images' , 'fileType' : 'png'}
    removeObstruction( picturesInfo, 'slow.png')
    
main()
