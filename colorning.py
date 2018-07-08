# -*- coding: utf-8 -*-
"""Colorning."""

from typing import Dict, List, Tuple

COLORS = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
          'white')
SHORT_COLORS = ('k', 'r', 'g', 'y', 'b', 'm', 'c', 'w')

STYLES = ('reset', 'bold', 'faint', 'italic', 'underline', 'slowblink',
          'rapidblink', 'reverse', 'conceal', 'cross')
FG_BASE = 30
BG_BASE = 40
BLIGHT = 60

ANSI_HEADER = '\x1b['
ANSI_FOOTER = 'm'


def _color_code(name: str, base: int) -> str:
    if name.lower() == name:
        lower_name = name
    elif name.upper() == name:
        base += BLIGHT
        lower_name = name.lower()
    else:
        raise ValueError(
            'All character of name must be only lower case or only upper case.'
        )
    color_set = SHORT_COLORS if len(name) == 1 else COLORS
    return str(base + color_set.index(lower_name))


def colorning(text: str,
              f: str = None,
              b: str = None,
              s: str = None,
              reset: bool = True) -> str:
    code = ''
    if f:
        if f.lower() not in COLORS + SHORT_COLORS:
            raise ValueError('"%s" is invalid color.' % f)
        code += _color_code(f, FG_BASE) + ';'
    if b:
        if b.lower() not in COLORS + SHORT_COLORS:
            raise ValueError('"%s" is invalid color.' % b)
        code += _color_code(b, BG_BASE) + ';'
    if s:
        if s not in STYLES:
            raise ValueError('"%s" is invalid style.' % s)
        s_list = set(s.split(','))
        code += ''.join([str(STYLES.index(style)) + ';' for style in s_list])
    code = ANSI_HEADER + code + ANSI_FOOTER
    reset = '' if not reset else \
        ANSI_HEADER + str(STYLES.index('reset')) + ';' + ANSI_FOOTER
    return code + text + reset


def multi_color(args: List[Tuple[str, Dict]]):
    result = ''
    for text, arg in args:
        arg['reset'] = False
        result += colorning(text, **arg)
    return result + colorning('', reset=True)
