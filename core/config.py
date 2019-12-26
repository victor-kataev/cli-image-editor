from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--rotate', action='store_true', help='rotates the image 90 degrees clockwise')
parser.add_argument('--mirror', action='store_true', help='flips the image horizontally')
parser.add_argument('--inverse', action='store_true', help='represents the image in negative')
parser.add_argument('--bw', action='store_true', help='black and white the image')
parser.add_argument('--lighten', type=int, choices=range(0, 101), action='store', help='increases brightness on <0-100> percent')
parser.add_argument('--darken', type=int, choices=range(0, 101), action='store', help='decreases brightness on <0-100> percent')
parser.add_argument('--sharpen', action='store_true', help='sharps the image')
parser.add_argument('src', help='source image')
parser.add_argument('dst', help='destination')

args = parser.parse_args()