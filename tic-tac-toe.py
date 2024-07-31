row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
counter = 0


def display():
    print(row1)
    print(row2)
    print(row3)


def user_choice():
    choice = input("Please enter a number (1-9): ")
    while not choice.isdigit() or (int(choice) not in range(1, 10)):
        print("Choice is not valid.")
        choice = input("Please enter a number (1-9): ")
    return int(choice)


def getCurrentSymbol():
    global counter
    symbol = ["X", "O"]
    counter += 1
    return symbol[counter % 2]


def update_table(index):
    if index in range(1, 4):
        if row1[index - 1] == " ":
            row1[index - 1] = getCurrentSymbol()
            return True
        else:
            return False
    elif index in range(4, 7):
        if row2[index % 3 - 1] == " ":
            row2[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False
    elif index in range(7, 10):
        if row3[index % 3 - 1] == " ":
            row3[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False


def check_winning():
    player_1_wins = False
    player_2_wins = False

    # row 1
    if (row1[0] == row1[1] and row1[1] == row1[2]) and (" " not in row1):
        if row1[0] == "O":
            player_1_wins = True
        else:
            player_2_wins = True

    # row 2
    if (row2[0] == row2[1] and row2[1] == row2[2]) and (" " not in row2):
        if row2[0] == "O":
            player_1_wins = True
        else:
            player_2_wins = True

    # row 3
    if (row3[0] == row3[1] and row3[1] == row3[2]) and (" " not in row3):
        if row3[0] == "O":
            player_1_wins = True
        else:
            player_2_wins = True

    # column 1
    if (row1[0] == row2[0] and row2[0] == row3[0]) and (row1[0] != " "):
        if row1[0] == "O":
            player_1_wins = True
        else:
            player_2_wins = True

    # column 2
    if (row1[1] == row2[1] and row2[1] == row3[1]) and (row1[1] != " "):
        if row1[1] == "O":
            player_1_wins = True
        else:
            player_2_wins = True

    # column 3
    if (row1[2] == row2[2] and row2[2] == row3[2]) and (row1[2] != " "):
        if row1[2] == "O":
            player_1_wins = True
        else:
            player_2_wins = True

    # diagonal (left top - right bottom)
    if (row1[0] == row2[1] and row2[1] == row3[2]) and (row1[0] != " "):
        if row1[0] == "O":
            player_1_wins = True
        else:
            player_2_wins = True

    # diagonal (left bottom - right top)
    if (row3[0] == row2[1] and row2[1] == row1[2]) and (row3[0] != " "):
        if row3[0] == "O":
            player_1_wins = True
        else:
            player_2_wins = True

    if player_1_wins:
        return "player 1 wins"
    elif player_2_wins:
        return "player 2 wins"
    else:
        return "no one wins"


def start_game():
    while True:
        display()
        while True:
            choice = user_choice()
            if update_table(choice):
                break
            else:
                print("wrong position")
        who_win = check_winning()
        match who_win:
            case "player 1 wins":
                display()
                print("player 1 wins")
                return
            case "player 2 wins":
                display()
                print("player 2 wins")
                return
            case "no one wins":
                if counter == 9:
                    display()
                    print("no one wins")
                    return


start_game()
