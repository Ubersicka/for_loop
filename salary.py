open_tab_number = int(input())
salary = int(input())

fine = 0

for open_tab in range(open_tab_number):
    site = input()
    if site == "Facebook":
        fine += 150
    elif site == 'Instagram':
        fine += 100
    elif site == 'Reddit':
        fine += 50
    else:
        continue

salary_after_fine = salary - fine
if salary_after_fine <= 0:
    print('You have lost your salary.')
else:
    print(salary_after_fine)

