import os
from PIL import Image, ImageDraw, ImageFont

LOGO_FILENAME = 'logo.png'
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
            continue # skip non-image files and the logo file itself

    im = Image.open(filename)  ## If the file is image, open it as image 
    width, height = im.size    ## and set width amnd height

    # Add the logo.
    print('Adding logo to %s' % (filename))
    im.paste(logoIm, (width-logoWidth , height - logoHeight))

    # Save changes.
    im.save(os.path.join('withLogoImage', filename))
