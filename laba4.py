def text2int(textnum, numwords={}):
    if not numwords:
        units = [
        "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
        "девять", "десять", "одиннадцать", "двеннадцать", "тринадцать", "четырнадцать", "пятнадцать",
        "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать",
        ]

        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдеят", "восемьдесят", "девяносто"]

        scales = ["сто", "тысяч", "миллионов"]

        numwords["и"] = (1, 0)
        for idx, word in enumerate(units):  numwords[word] = (1, idx)
        for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ""
    onnumber = False
    for word in textnum.split():
            if word not in numwords:
                if onnumber:
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
            else:
                scale, increment = numwords[word]

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True

    if onnumber:
        curstring += repr(result + current)

    return curstring

f = open('text.txt', encoding='utf-8')
arr = f.read().split()
str=""
for li in arr:
    str += li
    str += " "
print(text2int(str))
