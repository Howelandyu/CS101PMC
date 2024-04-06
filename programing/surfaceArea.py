# def surfaceArea(height,width,depth):
#     frontSide=height*width
#     rightSide=height*depth
#     topSide=width*depth
#     return(frontSide+rightSide+topSide)*2

def volume(height,width,depth):
    return (height,width,depth)

def surfaceArea(height,width,depth):
    frontSide=height*width
    rightSide=height*depth
    topSide=width*depth
    return((frontSide+rightSide+topSide)*2,(height*width*depth))

print(surfaceArea(1,1,1))
