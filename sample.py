# -*- coding: utf-8 -*-
"""Sample of colorning."""

from colorning import colorning as c
from colorning import multi_color as cs
from colorning import COLORS
from colorning import STYLES

print()
print(c('Foreground: ' + '|'.join(COLORS), f='k', b='w'))
for bg in COLORS:
    color_texts = []
    for fg in COLORS:
        color_texts.append((' [x] ', {'f': fg, 'b': bg}))

    head = '%-12s' % ('BG: ' + bg)
    print(head + cs(color_texts))

print()
for style in STYLES:
    color_texts = []
    for fg in COLORS:
        color_texts.append((' [x] ', {'f': fg, 's': style}))
    head = '%-20s' % ('Style: ' + style)
    print(head + cs(color_texts))

c('text', f='wrong')
