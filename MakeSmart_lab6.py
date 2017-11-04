# Team MakeSmart
# Maco Doussias, Pavlos Papadonikolakis, Jake McGhee
# Lab 6  


#Warmup
def removeRedEye():
  """ This function removes the red-eye from  a pic """
  """ TODO define function and decide if needs arguments.  Rename function if wanted """

def crazyEye():
  """ This function changes eye color to a crazy eye color """
  """ TODO define function and decide if needs arguments.  Rename Function if wanted """

  
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
  """ This function will "artify" a pic by manipulating the color ranges """
  """ TODO define function and decide if needs arguments.  Function should be name this per LAB#6 instruction. """
  """ TODO See lab 6 for color ranges """

#Problem 3
def chromakey():
    """Swaps the green in an image and replaces it with a different background image
       Args: threshold (int or float): Sensitivity for greenscreen replacement"""
       
    threshold = 200 #modify if image is not coming out as expected
    
    # get source image and background image
    print("Please select a photo with a green screen")
    source = getPic()
    print("Please select a photo to use as a background for your new picture")
    background = getPic()
    
    # makes sure background image is big enough to fill the source image
    if getWidth(background) < getWidth(source):
        print("chromakey error - background image is too narrow. Background image width: %i. Source image width: %i." % getWidth(background), getWidth(source))
        return
    elif getHeight(background) < getHeight(source):
        print("chromakey error - background image is too short. Background image height: %i. Source image height: %i." % getHeight(backgound), getHeight(source))
        return
    
    # reduce size of background image if it is significantly bigger than the source image    
    while getWidth(background) > getWidth(source)*2 and getHeight(background) > getHeight(source)*2:
        background = shrink(background)
    
    # replace background   
    for x in range (0, getWidth(source)):
        for y in range (0, getHeight(source)):
            color = getColor(getPixel(source,x,y))
            if distance(color, green) < threshold:
                color = getColor(getPixel(background,x,y))
                setColor(getPixel(source, x, y), color) 
    show(source)
    return source
    
def shrink(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(width/2, height/2)
  for x in range (0, width-1, 2):
    for y in range (0, height-1, 2):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, x/2, y/2), color)
  return canvas
    
  
