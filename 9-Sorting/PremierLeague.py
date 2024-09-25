inputs = input("Enter Input : ").split("/")
team_stat = []

for team_data in inputs:
    name, wins, loss, draws, scored, conceded = team_data.split(",")
    points = 3*int(wins) + 0*int(loss) + 1*int(draws)
    gd = int(scored) - int(conceded)
    team_stat.append([name, points, gd])

def bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j][1] < lst[j + 1][1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            elif lst[j][1] == lst[j + 1][1]:
                if lst[j][2] < lst[j + 1][2]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

sorted_team = bubble_sort(team_stat)
print("== results ==")

for data in sorted_team:
    print([data[0], {"points": data[1]}, {"gd": data[2]}])