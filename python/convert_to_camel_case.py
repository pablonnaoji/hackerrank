import re

def to_camel_case(text):
    if not text:
        return ''
    output = ''.join(x for x in text.title() if x.isalnum())
    answer = output[0].lower() + output[1:]
    if text[0].isupper():
        answer = output[0].upper() + output[1:] 
    print("ANSWER",answer)
    return answer

if __name__ == '__main__':
    text = 'the-stealth-warrior'
    answer = to_camel_case(text)
    print(answer)