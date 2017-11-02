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
def makePicSepia():
  """ Converts a picture to a sepia tone  """
  """ TODO define function and decide if needs arguments.  Rename Function if wanted """
 # TODO * in this case add a check to make sure the red does not go over 255 - 
 # TODO if the resulting red is over 255, set it to 255... This is a requirement for the function

  
def betterBnW():
    """ Converts an image to gray-scale """
    """ TODO if we get negative feedback from LAB3 on this function, fix... otherwise remove this comment."""
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        luminance = r*0.299 + g*0.587 + b*0.114
        setRed(p, luminance)
        setGreen(p, luminance)
        setBlue(p, luminance)
    repaint(pic)

    
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
  
  
  
  
  
