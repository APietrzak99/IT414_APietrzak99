import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def image_logo_draw(passed_logo,fname,employee_info):
    logoIm = Image.open("images/" + passed_logo)

    #resize logo to fit image a little better
    newlogoIm = logoIm.resize((100,50))
    logoWidth, logoHeight = newlogoIm.size
    img = Image.open("images/"+fname)
    width, height = img.size

    #add logo image to employee image
    img.paste(newlogoIm, (width - logoWidth, height - logoHeight), newlogoIm)

    #draw employee info text to the image
    draw_text = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/Syne-Regular.otf", 18)
    draw_text.text((10,400), employee_info, (0, 0, 0), font)
    #save changed images to output_images folder
    img.save(os.path.join('images/output_images', fname))