from PIL import Image
d = {1: "postcard.jpg", 2: "23f.jpg", 3: "8m.jpg", 4: "dr.jpg"}
print("1 - Новый год\n"
      "2 - 23 февраля\n"
      "3 - 8 марта\n"
      "4 - День рождения")
ans = int(input("Для получения открытки введите число - номер прадника : "))
filename = d[ans]
with Image.open(filename) as img:
    img.load()
img.show()
