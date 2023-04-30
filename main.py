#Функции
###################################################
def TaskSelection():
    print("Выберите номер задачи:\n"
          "1 - Обрезать открытку.\n"
          "2 - Открытка к празднику.\n"
          "3 - Открытка с именем.")
    number = input()
    match number:
        case "1":
            CropPostcard()
        case "2":
            PostcardForTheHoliday()
        case "3":
            PostcardWithTheName()
        case _:
            print("Введен неправильный номер.")
            TaskSelection()

###################################################
def CropPostcard():
    from PIL import Image
    filename = "Birthday.jpg"
    with Image.open(filename) as img:
        img.load()
        cropped_img = img.crop((115, 30, 940, 445))
        cropped_img.save("cropped_postcard.jpg")
        #cropped_img.show()
###################################################

def PostcardForTheHoliday():
    from PIL import Image
    d = {1: "NewYear.PNG", 2: "February23.jpg", 3: "March8.jpg", 4: "Birthday.jpg", 5: "9May.PNG"}
    print("1 - Новый год\n"
          "2 - 23 февраля\n"
          "3 - 8 марта\n"
          "4 - День рождения\n"
          "5 - День победы")
    file = int(input("Введите номер праздника для получения открытки: "))
    filename = d[file]
    with Image.open(filename) as img:
        img.load()
        img.show()
###################################################

def PostcardWithTheName():
    from PIL import Image, ImageDraw, ImageFont
    name = input("Введите имя получателя открытки: ")
    filename = "Birthday.jpg"
    with Image.open(filename) as img:
        img.load()
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 2 - 150, 15),
        name + ", поздравляю!",
        font=ImageFont.truetype("timesnewromanpsmt.ttf", 50),
        fill=('#015ef4')
    )
    img.show()
    img.save(name + "_postcard.png")
###################################################

#Основная программа
TaskSelection()
