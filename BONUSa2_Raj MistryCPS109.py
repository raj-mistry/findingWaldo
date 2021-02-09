#1
def compareOne(template,searchImage,x1,y1):
 targetx = x1 #x coordinate for searchimage
 targety = y1 #y coordinate for searchimage
 
 totaldifference = 0 #total luminence difference
  
 #looping through pixels of the template as well as the section of the scene being compared
 for x in range (0,3): #only scan one column
  targety = y1
  for y in range (0,3):
   #x and y are the coordinates for the template
   
   #getting the pixels for comparison
   templatepixel = getPixelAt(template,x,y)
   targetpixel = getPixelAt(searchImage,targetx,targety)
   
   #calculating luminence for each pixel
   templatepixelLuminence = getRed(templatepixel)*3
   targetpixelLuminence = getRed(targetpixel)*3
   
   #calculating difference between luminences and adding to the total difference
   difference = abs(templatepixelLuminence-targetpixelLuminence)
   totaldifference = totaldifference+difference
   
   targety +=1
  targetx +=1
  
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
 coordinates = [lowestX,lowestY]
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
 grayscale(template)
 grayscale(scene)
 template = scaledown(template,2)
 scene = scaledown(scene,2)
 list = find2Dmin(compareAll(template,scene))
 foundWaldo = scaleup(displayMatch(scene,list[0],list[1],getWidth(template),getHeight(template),red),2)
 return foundWaldo

def scaledown(picture,amount):
 canvas = makeEmptyPicture(getWidth(picture)/amount,getHeight(picture)/amount)
 sourceX = 0
 sourceY = 0
 for targetX in range (0,(getWidth(picture)/amount)):
  sourceY = 0
  for targetY in range (0,(getHeight(picture)/amount)):
   color = getPixelAt(picture,sourceX,sourceY)
   setColor(getPixelAt(canvas,targetX,targetY),makeColor(getColor(getPixelAt(picture,sourceX,sourceY))))
   sourceY = sourceY+amount
  sourceX = sourceX+amount
 return canvas
 
def scaleup(picture,amount):
 canvas = makeEmptyPicture(getWidth(picture)*amount,getHeight(picture)*amount)
 sourceX = 0
 sourceY = 0
 for targetX in range (0,getWidth(picture)*amount):
  sourceY = 0
  for targetY in range (0,getHeight(picture)*amount):
   color = getPixelAt(picture,int(sourceX),int(sourceY))
   setColor(getPixelAt(canvas,targetX,targetY),makeColor(getColor(color)))
   sourceY = sourceY+(1.0/amount)
  sourceX = sourceX+(1.0/amount)
 show(canvas)
 return picture
 
 
def main():
 tinywaldo = makePicture('C:\\Users\\rajmi\\OneDrive\\Desktop\\a2\\a2 attached files Nov 18, 2018 251 PM\\tinywaldo.jpg')
 waldo = makePicture('C:\\Users\\rajmi\\OneDrive\\Desktop\\a2\\a2 attached files Nov 18, 2018 251 PM\\waldo.jpg')
 tinyscene = makePicture('C:\\Users\\rajmi\\OneDrive\\Desktop\\a2\\a2 attached files Nov 18, 2018 251 PM\\tinyscene.jpg')
 scene = makePicture('C:\\Users\\rajmi\\OneDrive\\Desktop\\a2\\a2 attached files Nov 18, 2018 251 PM\\scene.jpg')
 
 findWaldo(waldo,tinyscene)
 