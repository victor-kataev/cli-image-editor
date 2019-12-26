from PIL import Image
import numpy as np
import sys
import utils
from config import *

def main():
    img = Image.open(sys.argv[-2])
    matrix = np.asarray(img, np.uint8)

    args_list = [x for x in sys.argv[1:-2] if '--' in x]

    for opt in args_list:
        opt = opt[2:] # discard leading --
        val = getattr(args, opt)
        if val not in [None, False]:
            func = getattr(utils, opt)
            matrix = func(matrix, val)

    if matrix.ndim == 3:
        output = Image.fromarray(matrix.astype(dtype=np.uint8), mode='RGB')
    else:
        output = Image.fromarray(matrix.astype(dtype=np.uint8), mode='L')
    output.save(args.dst)


if __name__ == '__main__':
    main()