import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('withLogo', exist_ok=True)

# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
            continue # skip non-image files and the logo file itself

    im = Image.open(filename)  ## If the file is image, open it as image 

    #Add logo text
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("DroidSans.ttf", 12)  ## Make sure the .ttf is available in the current directory 
    print ("Adding watermark to %s" % (filename))
    draw.text((50,20),"All Rights Reserved",fill=(128,255,255))
    
    # Save changes.
    im.save(os.path.join('withLogo', filename))
    
