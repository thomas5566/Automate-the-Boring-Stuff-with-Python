#!python3

import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_card(name):
    """Creates a personalised invitation card with the provided name on it."""
    name = name.strip()
    flower = Image.open('flower.png').convert("RGBA")
    width, height = flower.size
    card = Image.new('RGBA', (width, height), 'white')

    card.paste(flower, (10, 40), flower)
    cut_guide = Image.new('RGBA', (width+4 , height+4), 'black')
    cut_guide.paste(card, (2, 2))

    draw_obj = ImageDraw.Draw(cut_guide)
    fonts_folder = 'C:\\Windows\\Fonts'
    custom_font  = ImageFont.truetype(os.path.join(fonts_folder, 'comicz.ttf'), 72)
    draw_obj.text((120, 100), name, fill='blue', font=custom_font)

    cut_guide.save('{}-invite.png'.format(name))


with open('guests.txt') as f:
    guests = f.readlines()

for guest in guests:
    create_card(guest)

print('All invitations personalised and save to the CWD - enjoy the dinner.')