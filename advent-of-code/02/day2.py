# Modèlisage de l'input
input = open("input_intcode.txt", "r").read()

# strip() retire le \n
# split(',') transforme en list, séparant les éléments aux ','
list_input = input.strip().split(',')
# transforme tout les éléments en int
list_input = [int(i) for i in list_input]

# set un pointeur de position
position = 0

# Insert les valeurs données
list_input[1] = 12
list_input[2] = 2

# "Machine"
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
        
print(list_input)