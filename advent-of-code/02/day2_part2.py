# Modèlisage de l'input
input = open("input_intcode.txt", "r").read()

# strip() retire le \n
# split(',') transforme en list, séparant les éléments aux ','
list_input = input.strip().split(',')
# transforme tout les éléments en int
origin_list_input = [int(i) for i in list_input]

# "Machine"
stop = False
for noun in range(0,100) :
    for verb in range(0,100) :
        position = 0

        # Refresh de la list
        del list_input
        list_input = origin_list_input.copy()
        list_input[1] = noun
        list_input[2] = verb

        while True :

            operator = list_input[position]

            pos_a = position + 1
            pos_b = position + 2
            pos_c = position + 3

            val_a = list_input[pos_a]
            val_b = list_input[pos_b]
            val_c = list_input[pos_c]

            # Add
            if operator == 1 :
                output = list_input[val_a] + list_input[val_b]
                list_input[val_c] = output

            # Mult
            if operator == 2 :
                output = list_input[val_a] * list_input[val_b]
                list_input[val_c] = output

            # End
            if operator == 99 :
                break

            position += 4

        if list_input[0] == 19690720 :
            print("Solution noun=%s verb=%s", (noun, verb))
            stop = True
            break
        else:
            print(noun, verb, list_input[0])
            # print(list_input)
            # print(" ")
            verb = verb + 1
    if stop == True :
        break
    else:
        noun = noun + 1






