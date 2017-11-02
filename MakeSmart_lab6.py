# Team MakeSmart
# Maco Doussias, Pavlos Papadonikolakis, Jake McGhee

def getPic():
    """ prompts a user to pick a file to be converted to a JES picture """
    
    return makePicture(pickAFile())
    
    
# Problem 1

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