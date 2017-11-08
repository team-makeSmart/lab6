# Team MakeSmart
# Maco Doussias, Pavlos Papadonikolakis, Jake McGhee
# Lab 6  


#Warmup
def removeRedEye():
  """ This function removes the red-eye from  a pic and displays it """
  pic = makePicture(pickAFile()) 
  def removeRedEyeInBoundingBox(x1,y1,x2,y2):
    for x in range(x1, x2):
      for y in range(y1 , y2):
        p = getPixel(pic, x, y)
        color = getColor(p)
        if distance(color,red) < 200.0:
          r = getRed(p)
          g = getGreen(p)
          b = getBlue(p)
          r = (g + b) / 2
          color = makeColor(r , g, b)
          setColor(p,color)  
  removeRedEyeInBoundingBox(55,67,67,79)
  removeRedEyeInBoundingBox(157,67,171,80)
  show(pic)
  

def crazyEye():
  """ This function removes the red-eye from  a pic and displays it as a yellow crazy-eye!!!"""
  pic = makePicture(pickAFile()) 
  def makeCrazyEyeInBoundingBox(x1,y1,x2,y2):
    for x in range(x1, x2):
      for y in range(y1 , y2):
        p = getPixel(pic, x, y)
        color = getColor(p)
        if distance(color,red) < 200.0:
          r = getRed(p)
          g = r
          b = getBlue(p)
          color = makeColor(r , g, b *.10)
          setColor(p,color)  
  makeCrazyEyeInBoundingBox(55,67,67,79)
  makeCrazyEyeInBoundingBox(157,67,171,80)
  show(pic)

  
#Problem 1
def getPic():
  
  """ prompts a user to pick a file to be converted to a JES picture """
    
  return makePicture(pickAFile())
  

def sephia():
   pic = getPic()
   pic = betterBnW(pic)
   pixels = getPixels(pic)
   for p in pixels:
       r = getRed(p)
       if r < 63:
           setRed(p, r*1.1)
           setBlue(p, r*.9)
       elif r < 193:
           setRed(p, r*1.15)
           setBlue(p, r*.85)
       else:
           r *= 1.08
           if (r > 255):
              r = 255
           setRed(p, r)
           setBlue(p, r*.93)
   show(pic)

  
def betterBnW(pic):
    """ Converts an image to gray-scale """
    
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        luminance = r*0.299 + g*0.587 + b*0.114
        setRed(p, luminance)
        setGreen(p, luminance)
        setBlue(p, luminance)
    return(pic)

#Problem 2

def Artify():
  """ This function will artify a pic by manipulating the color ranges """
  def changePixel(pixelColorValue):
    """This nested function will take a pixels color value from 0 -255 and alter it to be within below range, then return it """
    if pixelColorValue < 63:
      pixelColorValue = 31
    elif pixelColorValue >= 63 and pixelColorValue < 128:
      pixelColorValue = 95
    elif pixelColorValue >= 128 and pixelColorValue < 192:
      pixelColor = 159
    else:
      pixelColorValue = 223 
    return pixelColorValue  
  pic = getPic() #Prompts user to choose a picture file, stores in pic variable
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)  #Gets the red value from the pixel and stores in r
    g = getGreen(p)   
    b = getBlue(p)
    r = changePixel(r) #Alters the red value and stores in r
    g = changePixel(g)
    b = changePixel(b)
    setRed(p,r) #Sets the red value of the pixel 
    setGreen(p,g)
    setBlue(p,b)  
  repaint(pic) #Displays picture to screen
  

#Problem 3
def chromakey():
    """Swaps the green in an image and replaces it with a different background image
       Args: threshold (int or float): Sensitivity for greenscreen replacement"""
       
    threshold = 200 # modify if image is not coming out as expected
    
    # get source image and background image
    print "Please select a photo with a green screen" 
    source = getPic()
    print "Please select a photo to use as a background for your new picture"
    background = getPic()
    
    # makes sure background image is big enough to fill the source image
    if getWidth(background) < getWidth(source):
      print "chromakey error - background image is too narrow. Background image width: %i. Source image width: %i." %(getWidth(background), getWidth(source))
      return
    elif getHeight(background) < getHeight(source):
      print "chromakey error - background image is too short. Background image height: %i. Source image height: %i." %(getHeight(backgound), getHeight(source))
      return
    
    # replace background   
    for x in range (0, getWidth(source)):
       for y in range (0, getHeight(source)):
         color = getColor(getPixel(source,x,y))
                            
         if distance(color, green) < threshold:
            color = getColor(getPixel(background,x,y)) 
            setColor(getPixel(source, x, y), color) 
    show(source)
    return source
    
    
  