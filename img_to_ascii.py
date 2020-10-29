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

    multiplier = 1
    if width > 250:
        multiplier = 10

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
    for row in all_pixels:

        ascii_row = []
        for pixel in row:

            if pixel >= 230:
                ascii_row.append(' ')
            elif pixel >= 205:
                ascii_row.append('.')
            elif pixel >= 180:
                ascii_row.append(':')
            elif pixel >= 155:
                ascii_row.append('-')
            elif pixel >= 120:
                ascii_row.append('=')
            elif pixel >= 95:
                ascii_row.append('+')
            elif pixel >= 70:
                ascii_row.append('*')
            elif pixel >= 45:
                ascii_row.append('#')
            elif pixel >= 20:
                ascii_row.append('%')
            else:
                ascii_row.append('@')

        all_ascii.append(ascii_row)

    return all_ascii

def store_file(ascii_file, all_ascii):
    all_ascii_lines = []

    for row in all_ascii:
        rows = ''
        for pixel in row:
            rows += (pixel + ' ')
        rows += '\n'
        all_ascii_lines.append(rows)

    with open(ascii_file, 'w') as f:
        f.writelines(all_ascii_lines)

main()
