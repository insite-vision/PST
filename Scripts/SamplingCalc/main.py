#! /usr/bin/env python3

import argparse


parser = argparse.ArgumentParser(description='image sampling calculator')
parser.add_argument('size', type=int, nargs=1, help='base image size')
parser.add_argument('window', type=int, nargs=1, help='window size')
parser.add_argument('shift', type=int, nargs=1, help='window shift')

args = parser.parse_args()

img_size = args.size[0]
window_size = args.window[0]
shift = args.shift[0]

# generate zero-initialized pixel count matrix
pixel_count = []
for _ in range(img_size):
    row = []
    for _ in range(img_size):
        row.append(0)
    pixel_count.append(row)

# for each window
r = 0
while True:
    c = 0
    while True:
        # increment count for each pixel in window
        for window_r in range(window_size):
            for window_c in range(window_size):
                if r+window_r < img_size and c+window_c < img_size:
                    pixel_count[r + window_r][c + window_c] += 1

        c += shift
        if c + window_size > img_size:
            break

    r += shift
    if r  + window_size > img_size:
        break

# print pixel count
for row in pixel_count:
    for pixel in row:
        print('{0:2d} '.format(pixel), end='')
    print()
    print()
