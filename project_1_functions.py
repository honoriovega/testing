# Author: Honorio Vega
# Date : 01/31/2017

from PIL import Image
import glob

avg = lambda a,b : (a + b) // 2
isEven = lambda x : x % 2 == 0

# finds the median in a list of numbers
# note: list start indexing at zero
def median(arr):
    
    length = len(arr)
    
    # special case - only one number in list
    if(length == 1) : return arr[0]

    # sort the numbers
    arr.sort()
    
    # store the length
    mid = length // 2

    return arr[mid] if isEven(length) else avg( arr[mid],arr[mid - 1] )
    

# read files from path
def readPictures(path,fileType,image_list):
    append = image_list.append
    files = glob.glob('%s/*.%s' % (path,fileType) )
    for filename in files :
        im = Image.open(filename)
        append(im)

# read pixels from pictures
def readPixels(picInfo,pixelInfo):
    pictures = []
    readPictures(picInfo['path'], picInfo['fileType'],pictures)
    append = pixelInfo.append
    width, height = pictures[0].size
    for picture in pictures:
        pixels = list(picture.getdata())
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        append(pixels)

    return (width,height)

# get the values of the picture
# and add to R, G, B respectively mult array
def getMedians(pixels,i,j,rgbs):
    # loop 3 times because (R, G, B)
    for k in range(3):
        append = rgbs[k].append
        for pixel in pixels : append( pixel[j][i][k] )

# This function removes an obstruction from a series of photos.
# It reads the files from a directory
def removeObstruction(picInfo,outputFileName):

    pixels = []
    width, height = readPixels(picInfo, pixels)

    # create a new file to write to
    result = Image.new('RGB', (width,height) )

    # stores the rgb information for each picture
    rgbs = [ [], [], [] ]
    px = result.load()
    for i in range(width):
        for j in range(height):
            getMedians(pixels,i,j,rgbs)
            px[i,j] = tuple([median(rgb) for rgb in rgbs])
            # reset the list
            rgbs = [[],[],[]]

    # write the image
    result.save(outputFileName)