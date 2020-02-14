import random
import curses

input('Le jeu se joue avec les touches WASD, appuyez sur ENTER pour débuter')

# Initialisation de curses
crs = curses.initscr()

# Disable le curseur
curses.curs_set(0)
# Disable l'Affichage de la touche appuyée
curses.noecho()
curses.cbreak()

# Retourne les dimensions maximales que peut avoir la fenetre
screen_height, screen_width = crs.getmaxyx()

# Initialise la fenêtre
window = curses.newwin(screen_height, screen_width, 0, 0)

# Accept les entrées de clavier
window.keypad(1)

# Refreshrate
window.timeout(100)

# Position de départ du snake
snake_y = screen_height//2
snake_x = screen_width//4

# List contenant la "queue" du snake (list de positions)
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1]
]

# Objet de la pomme au centre de la page
apple = [screen_height//2, screen_width//2]

# Ajout de l'objet à la fenêtre
window.addch(apple[0], apple[1], curses.ACS_DIAMOND)

# Boucle qui gère le jeux ----------------------------------------------------------------------
key = curses.KEY_RIGHT

while True:
    # Lecture d'une entrée (une seule entrée gardée en mémoire en même temps)
    next_key = window.getch()
    # Garde la même key si aucune autre n'a été appuyée depuis le dernier refresh
    key = key if next_key == -1 else next_key

    # Vérifie si le joueur à perdu -------------------------------------------------------------
    # Si le joueur sort du jeux
    if snake[0][0] in [0, screen_height-1] or snake[0][1] in [0, screen_width-1] :
        curses.endwin()
        print('Vous avez perdu')
        quit()

    # Si le joueur se mange lui-même
    if snake[0] in snake[1] :
        curses.endwin()
        print('Vous avez perdu')
        quit()


    # Mouvement du snake ----------------------------------------------------------------------
    new_pos = [snake[0][0], snake[0][1]]

    # W = 119, S = 115, A = 97, D = 100
    if key == 119 :
        new_pos[0] -= 1
    if key == 115:
        new_pos[0] += 1
    if key == 97 :
        new_pos[1] -= 1
    if key == 100 :
        new_pos[1] += 1

    # Insert la nouvelle position en premier, pop la dernière
    snake.insert(0, new_pos)

    # Si snake mange la pomme -----------------------------------------------------------------
    if snake[0] == apple :
        # Suprime la pomme
        apple = None

        # Initialise une nouvelle pomme
        while apple is None:
            new_apple = [
                random.randint(5, screen_height - 5),
                random.randint(5, screen_width - 5)
            ]
            #Vérifie que la nouvelle pomme n'est pas dans le snake, sinon repart l'init
            apple = new_apple if new_apple not in snake else None

        window.addch(apple[0], apple[1], curses.ACS_DIAMOND)
    else:
        # On pop juste si snake n'a pas mangé la pomme pour simuler le mouvement.
        # S'il a manger la pomme, le manque de pop fait comme un ajout
        old_pos = snake.pop()
        # Remplacer la dernière position de la queue du snake par un espace vide
        window.addch(old_pos[0], old_pos[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)