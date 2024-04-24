"""
    purpose:
        utils
    state: development/initial
    ------------------------------------------------------------------
    
"""
#
# sys
import sys
import pandas as pd

#
# LibSP
lib_abspaths = [r'i:\aPy\LibSP\QGis',
                r'i:\aPy\LibSP',
                ]
for path in lib_abspaths:
    if path not in sys.path:
        sys.path.append(path)
import spprint
import spstring

#
# the current project



def clean_string_obreb(s: str):
    """Extract pure obręb string."""
    garbage = ('obr.', 'obr', 'obręb', 'obreb',)
    delimiters_to_remove = '\t\n ,.;#'
    for g in garbage:
        s = s.replace(g, '')
    s = spstring.clean_string(s, delimiters_to_remove, ' ')

    # !> tu mozna dodać sprawdzenie, czy obręb jest
    return s

def main():
    pass


if __name__ == '__main__':
    main()
