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
   return pic
   

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
    return pic
    
def chromakey(threshold):
    """Swaps the green in an image and replaces it with a different background image"
    """Args: threshold (int or float): Sensitivity for greenscreen replacement"

    print("Please select a photo with a green screen")
    source = getPic()
    print("Please select a photo to use as a background for your new picture")
    background = getPic()
    
    if getWidth(background) < getWidth(source):
        print("chromakey error - background image is too narrow. Background image width: %i. Source image width: %i." % getWidth(background), getWidth(source))
        return
    elif getHeight(background) < getHeight(source):
        print("chromakey error - background image is too short. Background image height: %i. Source image height: %i." % getHeight(backgound), getHeight(source))
        return
    for x in range (0, getWidth(source)):
        for y in range (0, getHeight(source)):
            color = getColor(getPixel(source,x,y))
            if distance(color, green) < threshold:
                color = getColor(getPixel(background,x,y))
                setColor(getPixel(source, x, y), color) 
    show(source)
    return source
    