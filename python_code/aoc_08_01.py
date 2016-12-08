# Sebastian Raschka, 2016

"""
source: http://adventofcode.com/2016/day/8

DESCRIPTION

You come across a door implementing what you can only assume is an
implementation of two-factor authentication after a long
game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on
a nearby desk). Then, it displays a code on a little screen, and you type
that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken
everything apart and figured out how it works. Now you just have to work out
what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for
the screen; these instructions are your puzzle input. The screen is 50 pixels
wide and 6 pixels tall, all of which start off, and is capable of three
somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the
screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row)
right by B pixels. Pixels that would fall off the right end appear at the
left end of the row.
rotate column x=A by B shifts all of the pixels in column A
(0 is the left column) down by B pixels. Pixels that would fall
off the bottom appear at the top of the column.
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate row x=1 by 1 again rotates the second column down by one pixel,
causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful, and will soon
dominate the tiny-code-displaying-screen market. That's what the advertisement
on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display:
after you swipe your card, if the screen did work,
how many pixels should be lit?
"""

from collections import deque


def init_screen(screen, rect_str):
    rect_str = rect_str.split(' ')[-1]
    x, y = rect_str.strip().split('x')
    x, y = int(x), int(y)
    for i in range(y):
        for j in range(x):
            screen[i][j] = '#'


def rotate(screen, rot_str):
    s = rot_str.split()[1:]
    idx = int(s[1].split('=')[-1])
    by = int(s[-1])
    if s[0] == 'row':
        screen[idx].rotate(by)
    else:
        dq = deque([i[idx] for i in screen])
        dq.rotate(by)
        for i, j in zip(screen, dq):
            i[idx] = j


def count_pixels(screen):
    pixels = 0
    for row in screen:
        pixels += row.count('#')
    return pixels


if __name__ == '__main__':
    data = """rect 1x1
                rotate row y=0 by 5
                rect 1x1
                rotate row y=0 by 5
                rect 1x1
                rotate row y=0 by 5
                rect 1x1
                rotate row y=0 by 5
                rect 1x1
                rotate row y=0 by 2
                rect 1x1
                rotate row y=0 by 2
                rect 1x1
                rotate row y=0 by 3
                rect 1x1
                rotate row y=0 by 3
                rect 2x1
                rotate row y=0 by 2
                rect 1x1
                rotate row y=0 by 3
                rect 2x1
                rotate row y=0 by 2
                rect 1x1
                rotate row y=0 by 3
                rect 2x1
                rotate row y=0 by 5
                rect 4x1
                rotate row y=0 by 5
                rotate column x=0 by 1
                rect 4x1
                rotate row y=0 by 10
                rotate column x=5 by 2
                rotate column x=0 by 1
                rect 9x1
                rotate row y=2 by 5
                rotate row y=0 by 5
                rotate column x=0 by 1
                rect 4x1
                rotate row y=2 by 5
                rotate row y=0 by 5
                rotate column x=0 by 1
                rect 4x1
                rotate column x=40 by 1
                rotate column x=27 by 1
                rotate column x=22 by 1
                rotate column x=17 by 1
                rotate column x=12 by 1
                rotate column x=7 by 1
                rotate column x=2 by 1
                rotate row y=2 by 5
                rotate row y=1 by 3
                rotate row y=0 by 5
                rect 1x3
                rotate row y=2 by 10
                rotate row y=1 by 7
                rotate row y=0 by 2
                rotate column x=3 by 2
                rotate column x=2 by 1
                rotate column x=0 by 1
                rect 4x1
                rotate row y=2 by 5
                rotate row y=1 by 3
                rotate row y=0 by 3
                rect 1x3
                rotate column x=45 by 1
                rotate row y=2 by 7
                rotate row y=1 by 10
                rotate row y=0 by 2
                rotate column x=3 by 1
                rotate column x=2 by 2
                rotate column x=0 by 1
                rect 4x1
                rotate row y=2 by 13
                rotate row y=0 by 5
                rotate column x=3 by 1
                rotate column x=0 by 1
                rect 4x1
                rotate row y=3 by 10
                rotate row y=2 by 10
                rotate row y=0 by 5
                rotate column x=3 by 1
                rotate column x=2 by 1
                rotate column x=0 by 1
                rect 4x1
                rotate row y=3 by 8
                rotate row y=0 by 5
                rotate column x=3 by 1
                rotate column x=2 by 1
                rotate column x=0 by 1
                rect 4x1
                rotate row y=3 by 17
                rotate row y=2 by 20
                rotate row y=0 by 15
                rotate column x=13 by 1
                rotate column x=12 by 3
                rotate column x=10 by 1
                rotate column x=8 by 1
                rotate column x=7 by 2
                rotate column x=6 by 1
                rotate column x=5 by 1
                rotate column x=3 by 1
                rotate column x=2 by 2
                rotate column x=0 by 1
                rect 14x1
                rotate row y=1 by 47
                rotate column x=9 by 1
                rotate column x=4 by 1
                rotate row y=3 by 3
                rotate row y=2 by 10
                rotate row y=1 by 8
                rotate row y=0 by 5
                rotate column x=2 by 2
                rotate column x=0 by 2
                rect 3x2
                rotate row y=3 by 12
                rotate row y=2 by 10
                rotate row y=0 by 10
                rotate column x=8 by 1
                rotate column x=7 by 3
                rotate column x=5 by 1
                rotate column x=3 by 1
                rotate column x=2 by 1
                rotate column x=1 by 1
                rotate column x=0 by 1
                rect 9x1
                rotate row y=0 by 20
                rotate column x=46 by 1
                rotate row y=4 by 17
                rotate row y=3 by 10
                rotate row y=2 by 10
                rotate row y=1 by 5
                rotate column x=8 by 1
                rotate column x=7 by 1
                rotate column x=6 by 1
                rotate column x=5 by 1
                rotate column x=3 by 1
                rotate column x=2 by 2
                rotate column x=1 by 1
                rotate column x=0 by 1
                rect 9x1
                rotate column x=32 by 4
                rotate row y=4 by 33
                rotate row y=3 by 5
                rotate row y=2 by 15
                rotate row y=0 by 15
                rotate column x=13 by 1
                rotate column x=12 by 3
                rotate column x=10 by 1
                rotate column x=8 by 1
                rotate column x=7 by 2
                rotate column x=6 by 1
                rotate column x=5 by 1
                rotate column x=3 by 1
                rotate column x=2 by 1
                rotate column x=1 by 1
                rotate column x=0 by 1
                rect 14x1
                rotate column x=39 by 3
                rotate column x=35 by 4
                rotate column x=20 by 4
                rotate column x=19 by 3
                rotate column x=10 by 4
                rotate column x=9 by 3
                rotate column x=8 by 3
                rotate column x=5 by 4
                rotate column x=4 by 3
                rotate row y=5 by 5
                rotate row y=4 by 5
                rotate row y=3 by 33
                rotate row y=1 by 30
                rotate column x=48 by 1
                rotate column x=47 by 5
                rotate column x=46 by 5
                rotate column x=45 by 1
                rotate column x=43 by 1
                rotate column x=38 by 3
                rotate column x=37 by 3
                rotate column x=36 by 5
                rotate column x=35 by 1
                rotate column x=33 by 1
                rotate column x=32 by 5
                rotate column x=31 by 5
                rotate column x=30 by 1
                rotate column x=23 by 4
                rotate column x=22 by 3
                rotate column x=21 by 3
                rotate column x=20 by 1
                rotate column x=12 by 2
                rotate column x=11 by 2
                rotate column x=3 by 5
                rotate column x=2 by 5
                rotate column x=1 by 3
                rotate column x=0 by 4"""

    screen = [deque(50 * '.') for _ in range(6)]
    for row in data.split('\n'):
        row = row.strip()
        if not row:
            continue
        elif row.startswith('rect'):
            init_screen(screen, rect_str=row)
        else:
            rotate(screen, rot_str=row)

    print(count_pixels(screen))
