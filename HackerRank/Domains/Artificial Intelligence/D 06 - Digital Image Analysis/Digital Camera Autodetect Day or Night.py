class Pixel (object):
    def __init__ (self, rgb):
        self.red = int (rgb [0])
        self.green = int (rgb [1])
        self.blue = int (rgb [2])
        self.lum = self.calcLuminance ()
        
    def calcLuminance (self):
        return (0.2126 * self.red + 0.7152 * self.green + 0.0722 * self.blue)
        
# Anything at or below this threshold is considered dark
DARK_THRESHOLD = 50
 
pixels = list ()

# Read in data as pixels in giant list
while (True):
    try:
        for pix in input ().split (' '):
            pixels.append (Pixel (pix.split (',')))
    except (EOFError):
        break
        
# Count up the dark / light pixels and see which has more
light = 0
dark = 0
for pix in pixels:
    if (pix.lum <= DARK_THRESHOLD):
        dark += 1
    else:
        light += 1
        
if (dark > light):
    print ("night")
else:
    print ("day")