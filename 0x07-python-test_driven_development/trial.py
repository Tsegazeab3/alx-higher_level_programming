def text_indentation(text):
    punctuations = ".?:"
    for char in text:
        if char != ' ':
            print(char, end="")
        if char in punctuations:
            print('\n')