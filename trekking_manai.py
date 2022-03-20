group_number = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for number in range(group_number):   # range(1, count_of_number +1) (0, count_of_number)
    climbers_number = int(input())
    if climbers_number <= 5:
        musala += climbers_number
    elif climbers_number <= 12:
        monblan += climbers_number
    elif climbers_number <= 25:
        kilimandjaro += climbers_number
    elif climbers_number <= 40:
        k2 += climbers_number
    else:     # current_number >- 800
        everest += climbers_number
total_climbers_number = musala + monblan + kilimandjaro + k2 + everest
print(f'{musala / total_climbers_number * 100:.2f}%')
print(f'{monblan / total_climbers_number * 100:.2f}%')
print(f'{kilimandjaro / total_climbers_number * 100:.2f}%')
print(f'{k2 / total_climbers_number * 100:.2f}%')
print(f'{everest / total_climbers_number * 100:.2f}%')
