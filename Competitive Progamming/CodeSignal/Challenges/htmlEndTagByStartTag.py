""" Link: https://app.codesignal.com/challenge/6CH5C9bcLd9Pfoyk7 """

def htmlEndTagByStartTag(startTag):
    index = len(startTag) - 1
    for i, c in enumerate(startTag):
        if c == ' ':
            index = i 
            break 
    return '</' + startTag[1: index] + '>'