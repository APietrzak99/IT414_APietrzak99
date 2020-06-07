from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

my_image = Image.open("images/mountain_scene.jpg")

print(my_image.size)

draw_text = ImageDraw.Draw(my_image)
font = ImageFont.truetype("fonts/Syne-Regular.otf", 24)
draw_text.text((25,50), "A Mountain", (204, 51, 153), font)
my_image.save("sample-output.jpg")

my_image.rotate(90).save("sample-rotated-output.jpg")
