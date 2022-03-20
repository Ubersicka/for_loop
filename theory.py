# При определяне на диапазон използваме само цели числа.
# Използваме for цикъл, само когато знаем колко точно итерации трябва да направи --> range().
# Винаги имаме крайна стойност на итерациите.
# Променлива, която променя стойността си при всяка итерация.
# Работи само с цели числа.

# for number in range(x, y, z):     # X е старт  Y е край   Z e стъпка (start, end, step)
#     pass                          # for number in range (10) - това е само крайната стойност
                                    # for number in range (0, 10) - това е ако решим да изписваме 0, но може и горния пример


# for number in range(x, y):     # За променливата (number) в диапазона
# for number in range(y):        # x който го няма в този приммер, започва от 0


# for number in range(1, 10):   # if 1 <= number < 10 това цялото нещо изпълнява същата функция
#     print(number)

# for number in range(10):        # Изписвайки само крайната стойност, стартовата стойност е 0
#     print (number)

# for number in range(10):        # Изписва 10 пъти Hello
#     print("Hello")

# for number in range(1, 20, 1):    #Ще изпиши нормално от 1 до 19
#     print(number)

# for number in range(2, 20, 2):      #Ще принтира само четните числа, стъпка 2
#     print(number)

#for number in range (20, 1, 2):     # Няма да се изпълни този цикъл.
#for number in range (20, 1, -2):     # с тази стъпка -2, ще започне от 20 и ще изважда -2 към крайна стойност 1.
#    print(number)

# for number in range (1, 10 +1)       # Крайната стойност ще е 10
#     print(number)

# for number in range (1,10 +1):
#     print(number)
#     number += 100
#     print(number)

# for number in range (1,10 +1):        # 10 пъти ще повтаря операцията в цикъла.
#     number2 = 10
#     print(number2)
#     number2 += 100
#     print(number2)

# for number in range (1, 200):
#     if number % 2 == 0:
#         print(number)
#         continue           # Използва се само в тялото на цикъла. Означава не се интересувай какво има надолу а продължи пак от горе.
#         break              # Обратното на continue. Спира и нито надолу, нито нагоре.
#     print("Number is odd")

# text = input()
# print(text)

# text = input()           #отпечатва въвдените букви на текста
# for letter in text:
#     print(letter)

# text = input()           #Работа с индекс. Първата буква на текста започва от 0.
# print(text[0])
# print(text[4])
# print(text[5])

# text = input()
# for index, character in enumerate(text):                 #Извърта цикъла едновремено индекса и символа
#     print(f'Index->{index}, character ->{character}')
