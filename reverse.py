def reverse(st):
    sentence = []
    word = ""
    whitespace = ""
    for l in st:
       if l != " ":
            word += l
            whitespace = ""
       else: 
            whitespace += l
            sentence.append(word)
            word = ""
            sentence.append(l)
    sentence.append(word)
    return ''.join(sentence[::-1])

print(reverse("Hello world"))
print(reverse("Hello  world"))


