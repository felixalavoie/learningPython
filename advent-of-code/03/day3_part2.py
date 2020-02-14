input = open('input.txt', 'r')
input_list = input.read().splitlines()
input.close()

input_cable1 =  input_list[0].split(',')
input_cable2 =  input_list[1].split(',')

def get_points(cable) :
    x = 0
    y = 0
    answer = set()
    for pos in cable :
        operator = pos[0]
        distance = int(pos[1:])
        dx = {'L':-1, 'R':1, 'U':0, 'D':0}
        dy = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

        for i in range(distance) :
            x += dx[operator]
            y += dy[operator]
            answer.add((x,y))

    return answer

all_pos_cable1 = get_points(input_cable1)
all_pos_cable2 = get_points(input_cable2)
join = all_pos_cable1&all_pos_cable2

commons = [(x,y) for (x,y) in join]
list_cable1 = list(all_pos_cable1)
list_cable2 = list(all_pos_cable2)

def get_steps(coords) :
    index1 = list_cable1.index(coords)
    index2 = list_cable2.index(coords)
    total_steps = len(list_cable1[:index1]) + len(list_cable2[:index2])
    return total_steps

step_counts = set()
for coords in commons :
    steps = get_steps(coords)
    step_counts.add(steps)

answer = min(step_counts)
print(answer)


