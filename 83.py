from PIL import Image, ImageDraw, ImageFont
name = input("Введите имя получателя: ")
filename = "postcard.jpg"
with Image.open(filename) as img:
    img.load()
# используется файл с жирными символами шрифта Arial
font = ImageFont.truetype("arial_bold.ttf", 25)
draw_text = ImageDraw.Draw(img)
draw_text.text(
    (img.width // 2 - 100, 15),
    name + ", поздравляю!",
    font=font,
    fill=('#FAACAC')
)
img.show()
img.save(name + "_postcard.png")
