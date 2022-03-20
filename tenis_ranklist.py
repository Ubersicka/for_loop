import math

tournament_count = int(input())
start_point_in_list = int(input())

total_points_from_tournament = 0
win_tournament = 0

for tournamets in range(tournament_count):
    level_of_the_tournament = input()
    if level_of_the_tournament == "W":
        total_points_from_tournament += 2000
        win_tournament += 1
    elif level_of_the_tournament == "F":
        total_points_from_tournament += 1200
    elif level_of_the_tournament == "SF":
        total_points_from_tournament += 720
    else:
        pass
total_points = total_points_from_tournament + start_point_in_list
avarage_points = total_points_from_tournament / tournament_count
win_tournament_percent = (win_tournament / tournament_count) * 100

print(f"Final points: {total_points}")
print(f'Average points: {math.floor(avarage_points)}')
print(f"{win_tournament_percent:.2f}%")
