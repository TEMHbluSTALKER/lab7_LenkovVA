from PIL import Image
filename = "postcard.jpg"
with Image.open(filename) as img:
    img.load()
cropped_img = img.crop((110, 210, 640, 470))
# cropped_img.show()
cropped_img.save("cropped_postcard.jpg")
