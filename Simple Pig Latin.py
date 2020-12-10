'''
[+]Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

[+]Examples:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

#solution:
def pig_it(text):
    word = []
    specchar = ["!", "?", "."]
    pig = text.split()
    for i in range(len(pig)):
        if pig[i][0] in specchar:
            word.append(pig[i])
        else:
            word.append(pig[i].replace(pig[i][0],"",1) + pig[i][0] + "ay")
    return " ".join(word)

#solution 2:
def pig_it(text):
    return " ".join(word[1:] + word[0:1] + "ay" if word.isalpha() else word for word in text.split())
