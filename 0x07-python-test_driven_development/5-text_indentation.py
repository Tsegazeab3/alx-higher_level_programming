#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text,str):
        raise TypeError("text must be a string")
    i = 0
    while i <= len(text) - 1 :
        if text[i] in ".?:":
            print('{}\n'.format(text[i]))
            i += 1
            while i < len(text) and text[i]==' ':
                i += 1
                continue
        else:
            print(text[i],end="")
            i += 1