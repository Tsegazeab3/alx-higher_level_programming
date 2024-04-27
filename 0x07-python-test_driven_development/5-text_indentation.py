#!/usr/bin/python3
"""
This module containts the text_indent function
the test file is inside tests as 5-text_indentation
it has not implement no other modules
"""


def text_indentation(text):
    """
    text_indentation function:
        indents text
    Args:
        text to be indented
    exceptions:
        Type Error: text must be a string only
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i <= len(text) - 1:
        if text[i] in ".?:":
            print('{}\n'.format(text[i]))
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
                continue
        else:
            print(text[i], end="")
            i += 1
