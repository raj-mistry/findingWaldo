#1
def compareOne(template,searchImage,x1,y1):
 targetx = x1 #x coordinate for searchimage
 targety = y1 #y coordinate for searchimage
 
 totaldifference = 0 #total luminence difference
  
 #looping through pixels of the template as well as the section of the scene being compared
 for x in range (0,getWidth(template)/10,1): #/10 to make it faster
  targety = y1
  for y in range (0,getHeight(template)/10,1):#/10 to make it faster (scan less of the template)
   #x and y are the coordinates for the template
   
   #getting the pixels for comparison
   templatepixel = getPixelAt(template,x,y)
   targetpixel = getPixelAt(searchImage,targetx,targety)
   
   #calculating luminence for each pixel
   templatepixelLuminence = getRed(templatepixel)+getGreen(templatepixel)+getBlue(templatepixel)
   targetpixelLuminence = getRed(targetpixel)+getGreen(targetpixel)+getBlue(targetpixel)
   
   #calculating difference between luminences and adding to the total difference
   difference = abs(templatepixelLuminence-targetpixelLuminence)
   totaldifference = totaldifference+difference
   
   targety = targety+1
  targetx = targetx+1
  
 return totaldifference #output the total difference
 
 
#2
def compareAll(template,searchImage):
 W = getWidth(searchImage)
 W2 = getWidth(template)
 H = getHeight(searchImage)
 H2 = getHeight(template)
 BIG = 10000000000000000000000000000000000000000
 matrix = [[BIG for i in range(H-H2-1)] for j in range(W-W2-1)]
 for x in range(0,len(matrix)):
  for y in range (0,len(matrix[x])):
   matrix[x][y]= compareOne(template,searchImage,x,y)
 return matrix


def find2Dmin(matrix):
 lowestDifference = matrix[0][0]
 lowestX = 0
 lowestY = 0
 for x in range(0,len(matrix)):
  for y in range (0,len(matrix[x])):
   if matrix[x][y]<lowestDifference:
    lowestDifference = matrix[x][y]
    lowestX = x
    lowestY = y
 #print lowestDifference
 coordinates = [lowestX,lowestY]
 #print lowestX
 #print lowestY
 return(coordinates)

def displayMatch(searchImage,x1,y1,w1,h1,color):
 addRect(searchImage,x1,y1,w1,h1,red)
 addRect(searchImage,x1+1,y1+1,w1-2,h1-2,red)
 addRect(searchImage,x1+2,y1+2,w1-3,h1-3,red)
 return searchImage

def grayscale(picture):
 for pixel in getPixels(picture):
  graypixel = (getRed(pixel)+getGreen(pixel)+getBlue(pixel))/3
  setColor(pixel, makeColor(graypixel,graypixel,graypixel))
 return picture

def findWaldo(template,scene):
 template = grayscale(template)
 scene = grayscale(scene)
 list = find2Dmin(compareAll(template,scene))
 show(displayMatch(scene,list[0],list[1],getWidth(template),getHeight(template),red))


def main():
 tinywaldo = makePicture('C:\\Users\\rajmi\\OneDrive\\Desktop\\a2\\a2 attached files Nov 18, 2018 251 PM\\tinywaldo.jpg')
 waldo = makePicture('C:\\Users\\rajmi\\OneDrive\\Desktop\\a2\\a2 attached files Nov 18, 2018 251 PM\\waldo.jpg')
 tinyscene = makePicture('C:\\Users\\rajmi\\OneDrive\\Desktop\\a2\\a2 attached files Nov 18, 2018 251 PM\\tinyscene.jpg')
 scene = makePicture('C:\\Users\\rajmi\\OneDrive\\Desktop\\a2\\a2 attached files Nov 18, 2018 251 PM\\scene.jpg')
 findWaldo(waldo,tinyscene)
 