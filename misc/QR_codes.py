import qrcode

data:str = "ENTER YOUR DATA HERE"

img = qrcode.make(data)
print(type(img)) 
img.save("current_QR.png")