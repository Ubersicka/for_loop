actor_name = input()
total_points = float(input())
number_of_jury = int(input())
#is_nominated = False  Също става
for current_grade in range(number_of_jury): #range(1, number_of_jury+1)
    current_name = input()
    current_points = float(input())
    current_final_points = len(current_name) * current_points / 2
    total_points += current_final_points
    if total_points > 1250.5:
        #is_nominated = True също става
        break
if total_points > 1250.5:   #if is_nominated също става
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    difference = 1250.5 - total_points
    print(f'Sorry, {actor_name} you need {difference:.1f} more!')
