import requests
from PIL import Image, ImageFont, ImageDraw

URL = "http://127.0.0.1:8000/maintitles/python/"
URL_1 = "http://127.0.0.1:8000/titles/python-asoslari/"
response = requests.get(url=URL).json()
response_1 = requests.get(url=URL_1).json() 
my_image = Image.open("C:/Users/User/Desktop/Wallpaper/img_test.jpg")

maintitles_font = ImageFont.truetype("D:/Asosiy/Prayer-times/images/Fonts/Alkatra-VariableFont_wght.ttf", 50)
tiles_font = ImageFont.truetype("D:/Asosiy/Prayer-times/images/Fonts/Alkatra-VariableFont_wght.ttf", 40)

maintitles = response[0]['name']
titles = response_1[0]['name']

image_editable_maintitles = ImageDraw.Draw(my_image)
image_editable_titles = ImageDraw.Draw(my_image)

image_editable_maintitles.text((70, 35), maintitles, (0, 0, 0), font=maintitles_font)
image_editable_titles.text((90, 90), titles, (0, 0, 0), font=tiles_font)

my_image.save(f"result_test.jpg")
