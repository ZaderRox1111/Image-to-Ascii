import sys
from PIL import Image

def main():
    image_to_open = sys.argv[1]
    file_to_store_ascii = sys.argv[2]

    with Image.open(image_to_open) as im:
        pixels = im.load()
    width, height = im.size

    all_pixels = make_bw(width, height, pixels)
    all_ascii = turn_to_ascii(all_pixels)
    store_file(file_to_store_ascii, all_ascii)

def make_bw(width, height, pixels):
    all_pixels = []

    if width <= 500 and height <= 400:
        multiplier = 1
    else:
        if width >= height:
            multiplier = round(width / 100)
        else:
            multiplier = round(height / 100)

    # multiplier = 1
    # if width > 4000 or height > 5000:
    #     multiplier = 80
    # elif width > 3000 or height > 4000:
    #     multiplier = 60
    # elif width > 2000 or height > 3000:
    #     multiplier = 35
    # elif width > 1000 or height > 2000:
    #     multiplier = 25
    # elif width > 500 or height > 1000:
    #     multiplier = 12

    for x in range(width // multiplier):
        rows = []
        for y in range(height // multiplier):
            cpixel = pixels[multiplier * x,multiplier * y]
            bw_value = int(round(sum(cpixel) / float(len(cpixel))))

            rows.append(bw_value)
        all_pixels.append(rows)

    return all_pixels

def turn_to_ascii(all_pixels):
    all_ascii = []

    ascii_scale = '@%#M+=>-:. '

    for row in all_pixels:

        ascii_row = []
        for pixel in row:
            
            # basically compares the pixel's grayscale to the list of ascii --> ex: 155/255 about= ascii_scale[155/255]
            ascii_index = round((pixel/255) * (len(ascii_scale)))
            if ascii_index >= len(ascii_scale):
                ascii_index = len(ascii_scale) - 1
            ascii_char = ascii_scale[ascii_index]
            ascii_row.append(ascii_char)

        all_ascii.append(ascii_row)

    return all_ascii

def store_file(ascii_file, all_ascii):
    all_ascii_lines = []

    # uses zip to transpose image, so that it is oriented the correct way
    transposed_image = list(zip(*all_ascii))

    for row in transposed_image:
        rows = ''
        for pixel in row:
            rows += (pixel + ' ')
        rows += '\n'
        all_ascii_lines.append(rows)

    with open(ascii_file, 'w') as f:
        f.writelines(all_ascii_lines)

main()
