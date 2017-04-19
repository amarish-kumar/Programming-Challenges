class Pixel (object):
    def __init__ (self, rgb):
        self.red = rgb [0]
        self.green = rgb [1]
        self.blue = rgb [2]
        
    def isIntense (self):
        if (self.red < COLOR_MINIMUM_INTENSITY):
            return False
        elif (self.green < COLOR_MINIMUM_INTENSITY):
            return False
        elif (self.blue < COLOR_MINIMUM_INTENSITY):
            return False
        else:
            return True

def filterImage (image_matrix):
    filtered_matrix = list ()
    
    for row in image_matrix:
        filtered_row = list ()
        
        for pixel in row:
            if (pixel.isIntense ()):
                filtered_row.append (' ')
            else:
                filtered_row.append ('X')
                
        filtered_matrix.append (filtered_row)
    return (filtered_matrix)
                
def initLetterDict ():
    # Does the very boring job of initializing the letterDict
    # Letter width: 8u height: 10u
    LETTER_DICT ["A"] = ['   XX   ', '  XXXX  ', ' XX  XX ', 'XX    XX', 'XX    XX', 'XX    XX', 'XXXXXXXX', 'XX    XX', 'XX    XX', 'XX    XX']
    LETTER_DICT ["B"] = ['XXXXXX  ', 'XX   XX ', 'XX    XX', 'XX   XX ', 'XXXXXX  ', 'XX   XX ', 'XX    XX', 'XX    XX', 'XX   XX ', 'XXXXXX  ']
    LETTER_DICT ["C"] = ['  XXXXX ', ' XX   XX', 'XX     X', 'XX      ', 'XX      ', 'XX      ', 'XX      ', 'XX     X', ' XX   XX', '  XXXXX ']
    LETTER_DICT ["D"] = ['XXXXXX  ', 'XX   XX ', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX   XX ', 'XXXXXX  ']
    LETTER_DICT ["E"] = ['XXXXXXX ', 'XX      ', 'XX      ', 'XX      ', 'XXXXXX  ', 'XX      ', 'XX      ', 'XX      ', 'XX      ', 'XXXXXXX ']
    LETTER_DICT ["F"] = ['XXXXXXXX', 'XX      ', 'XX      ', 'XX      ', 'XXXXXX  ', 'XX      ', 'XX      ', 'XX      ', 'XX      ', 'XX      ']
    LETTER_DICT ["G"] = ['  XXXXX ', ' XX   XX', 'XX      ', 'XX      ', 'XX      ', 'XX   XXX', 'XX    XX', 'XX    XX', ' XX   XX', '  XXXXX ']
    LETTER_DICT ["H"] = ['XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XXXXXXXX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX']
    LETTER_DICT ["I"] = [' XXXXXX ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', ' XXXXXX ']
    LETTER_DICT ["J"] = ['   XXXX ', '     XX ', '     XX ', '     XX ', '     XX ', '     XX ', '     XX ', ' X   XX ', ' XX XX  ', '  XXX   ']
    LETTER_DICT ["K"] = ['XX    XX', 'XX   XX ', 'XX  XX  ', 'XX XX   ', 'XXXX    ', 'XXXX    ', 'XX XX   ', 'XX  XX  ', 'XX   XX ', 'XX    XX']
    LETTER_DICT ["L"] = ['XX      ', 'XX      ', 'XX      ', 'XX      ', 'XX      ', 'XX      ', 'XX      ', 'XX      ', 'XX      ', 'XXXXXXX ']
    LETTER_DICT ["M"] = ['XX    XX', 'XXX  XXX', 'XXXXXXXX', 'XX XX XX', 'XX XX XX', 'XX XX XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX']
    LETTER_DICT ["N"] = ['XX    XX', 'XXX   XX', 'XXXX  XX', 'XXXX  XX', 'XX XX XX', 'XX XX XX', 'XX  XXXX', 'XX   XXX', 'XX   XXX', 'XX    XX']
    LETTER_DICT ["O"] = ['  XXXX  ', ' XX  XX ', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', ' XX  XX ', '  XXXX  ']
    LETTER_DICT ["P"] = ['XXXXXXX ', 'XX    XX', 'XX    XX', 'XX    XX', 'XXXXXXX ', 'XX      ', 'XX      ', 'XX      ', 'XX      ', 'XX      ']
    LETTER_DICT ["Q"] = ['  XXXX  ', ' XX  XX ', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX XX XX', 'XX  XXXX', ' XX  XX ', '  XXXX X']
    LETTER_DICT ["R"] = ['XXXXXXX ', 'XX    XX', 'XX    XX', 'XX    XX', 'XXXXXXX ', 'XXXXX   ', 'XX  XX  ', 'XX   XX ', 'XX    XX', 'XX    XX']
    LETTER_DICT ["S"] = [' XXXXXX ', 'XX    XX', 'XX      ', 'XX      ', ' XXXXXX ', '      XX', '      XX', '      XX', 'XX    XX', ' XXXXXX ']
    LETTER_DICT ["T"] = ['XXXXXXXX', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ']
    LETTER_DICT ["U"] = ['XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', ' XX  XX ', '  XXXX  ']
    LETTER_DICT ["V"] = ['XX    XX', 'XX    XX', 'XX    XX', ' XX  XX ', ' XX  XX ', ' XX  XX ', '  XXXX  ', '  XXXX  ', '   XX   ', '   XX   ']
    LETTER_DICT ["W"] = ['XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', 'XX XX XX', 'XX XX XX', 'XX XX XX', 'XXXXXXXX', 'XXX  XXX', 'XX    XX']
    LETTER_DICT ["X"] = ['XX    XX', 'XX    XX', ' XX  XX ', '  XXXX  ', '   XX   ', '   XX   ', '  XXXX  ', ' XX  XX ', 'XX    XX', 'XX    XX']
    LETTER_DICT ["Y"] = ['XX    XX', 'XX    XX', ' XX  XX ', '  XXXX  ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ']
    LETTER_DICT ["Z"] = ['XXXXXXX ', '     XX ', '     XX ', '    XX  ', '   XX   ', '  XX    ', ' XX     ', 'XX      ', 'XX      ', 'XXXXXXX ']
    LETTER_DICT ["0"] = ['   XX   ', '  XXXX  ', ' XX  XX ', 'XX    XX', 'XX    XX', 'XX    XX', 'XX    XX', ' XX  XX ', '  XXXX  ', '   XX   ']
    LETTER_DICT ["1"] = ['   XX   ', '  XXX   ', ' XXXX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', '   XX   ', ' XXXXXX ']
    LETTER_DICT ["2"] = ['  XXXX  ', ' XX  XX ', 'XX    XX', '      XX', '     XX ', '    XX  ', '   XX   ', '  XX    ', ' XX     ', 'XXXXXXXX']
    LETTER_DICT ["3"] = [' XXXXX  ', 'XX   XX ', '      XX', '     XX ', '   XXX  ', '     XX ', '      XX', '      XX', 'XX   XX ', ' XXXXX  ']
    LETTER_DICT ["4"] = ['     XX ', '    XXX ', '   XXXX ', '  XX XX ', ' XX  XX ', 'XX   XX ', 'XXXXXXXX', '     XX ', '     XX ', '     XX ']
    LETTER_DICT ["5"] = ['XXXXXXX ', 'XX      ', 'XX      ', 'XX XXX  ', 'XXX  XX ', '      XX', '      XX', 'XX    XX', ' XX  XX ', '  XXXX  ']
    LETTER_DICT ["6"] = ['  XXXX  ', ' XX  XX ', 'XX    X ', 'XX      ', 'XX XXX  ', 'XXX  XX ', 'XX    XX', 'XX    XX', ' XX  XX ', '  XXXX  ']
    LETTER_DICT ["7"] = ['XXXXXXXX', '      XX', '      XX', '     XX ', '    XX  ', '   XX   ', '  XX    ', ' XX     ', 'XX      ', 'XX      ']
    LETTER_DICT ["8"] = ['  XXXX  ', ' XX  XX ', 'XX    XX', ' XX  XX ', '  XXXX  ', ' XX  XX ', 'XX    XX', 'XX    XX', ' XX  XX ', '  XXXX  ']
    LETTER_DICT ["9"] = ['  XXXX  ', ' XX  XX ', 'XX    XX', 'XX    XX', ' XX  XXX', '  XXX XX', '      XX', ' X    XX', ' XX  XX ', '  XXXX  ']
    
# Minimum pixel intensity
COLOR_MINIMUM_INTENSITY = 140
# Number of letters per image
NUM_LETTERS_PER_IMAGE = 5
# 10 spaces from the left before the word begins
WORD_PADDING_LEFT = 5
# 11 empty lines from the top before word begins
WORD_PADDING_TOP = 11
# Each character has a width of 8 pixel units
LETTER_WIDTH = 8
# Each character has a height of 10 pixel units
LETTER_HEIGHT = 10
# The gap between each character
LETTER_GAP = 1
# Dictionary of every possible character using this font
LETTER_DICT = dict ()
initLetterDict ()
    
r, c = map (int, input ().split (' '))

image = list ()

# Go through each row and RGB-ify it
for i in range (r):
    row = list ()
    RGBs = input ().split (' ')
    
    for RGB in RGBs:
        row.append (Pixel (list (map (int, RGB.split (',')))))
        
    image.append (row)

# Return a simplified matrix of image data
# ' ' = Nothing is there
# 'X' = Letter is there
image_bw = filterImage (image)

# Character matrix buffer for converted image lettering
char_matrix_buffer = dict ()
for i in range (NUM_LETTERS_PER_IMAGE):
    char_matrix_buffer [i] = list ()

# Start from the layer @ top of word
# Move until reaching bottom of word
for layer in range (WORD_PADDING_TOP, WORD_PADDING_TOP + LETTER_HEIGHT, 1):
    # Each image has exactly 5 characters. Use 5 character matrix buffers
    for pix in range (WORD_PADDING_LEFT, WORD_PADDING_LEFT + (LETTER_WIDTH * NUM_LETTERS_PER_IMAGE), LETTER_WIDTH + LETTER_GAP):
        # For each layer, clip out NUM_LETTERS_PER_IMAGE strings LETTER_WIDTH in width and add to buffer
        index = int ((pix - WORD_PADDING_LEFT) / LETTER_WIDTH)
        char_matrix_buffer [index].append ("".join (image_bw [layer][pix:pix + LETTER_WIDTH]))
        
# Perform character matching RAW
# Starting from 'A', move through dict until you match all layers of each char matrix
matches = ""

for i in range (NUM_LETTERS_PER_IMAGE):
    for key, value in LETTER_DICT.items ():
        if (char_matrix_buffer [i] == value):
            matches += key
            continue
            
print (matches)