text = input()

len_text = len(text)
sum = 0
for letter in text:          #за всяка буква от тези избраните
    if letter == 'a':
        sum += 1
    elif letter == 'e':
        sum += 2
    elif letter == 'i':
        sum += 3
    elif letter == 'o':
        sum += 4
    elif letter == 'u':
        sum += 5

print(sum)
