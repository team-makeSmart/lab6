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
  """ Chroma-Key finds all pixels that are the same color as the backdrop and replaces them like a green screen effect. """
  """ TODO define function and decide if needs arguments.  Function should be name this per LAB#6 instruction. """
  """ TODO See lab 6 for color ranges
  
