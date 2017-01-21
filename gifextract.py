import os
import numpy as np
from PIL import Image


def analyseImage(path):
    """
    Pre-process pass over the image to determine the mode (full or additive).
    Necessary as assessing single frames isn't reliable. Need to know the mode 
    before processing all frames.
    """
    im = Image.open(path)
    results = {
        'size': im.size,
        'mode': 'full',
    }
    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return results


def getGIFFrames(path):
    """
    Iterate the GIF, extracting each frame. Returns a list of numpy
    2D array for each frame.
    """
    im = Image.open(path)
    palette = im.getpalette()
    mode = analyseImage(path)['mode']

    try:
        res = []
        i = 0
        while True:
            if not im.getpalette():
                im.putpalette(palette)

            new_frame = Image.new('RGBA', im.size)
            if mode == 'partial':
                new_frame.paste(last_frame)
            new_frame.paste(im, (0, 0))

            res.append(np.array(new_frame))

            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return res
