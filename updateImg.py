from PIL import Image

def isWithinRange(num, target, range):
    if(num - range <= target <= num + range):
        return True
    else:
        return False

def convertImage():
    img = Image.open("assets/favicon.png")
    img = img.convert("RGBA")
  
    datas = img.getdata()
  
    newData = []
  
    for item in datas:
        if item[3] == 0:
            newData.append((255, 255, 255))
        else:
            newData.append(item)
  
    img.putdata(newData)
    img.save("./New.png", "PNG")
    print("Successful")
  
convertImage()