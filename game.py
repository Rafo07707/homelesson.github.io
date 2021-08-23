
import random
player_score = 0
computer_score = 0
choices = ["qar", "tuxt", "mkrat"]
print("Камень давит ножницы. Ножницы режут бумагу. Бумага накрывает камень.")
player = input("Выберите: qar, tuxt, kam mkrat (exit)? ")
while player != "exit":                 
    player = player.lower()             
    computer = random.choice(choices)   
    print("Твой выбор " +player+ ", компьютер выбрал " +computer+ ".")
    if player == computer:
        print("Ничья")
    elif player == "qar":
        if computer == "mkrat":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        print ("Обший счёт: у вас ", player_score, "у компьютера ", computer_score)
    elif player == "tuxt":
        if computer == "qar":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        print ("Обший счёт: у вас ", player_score, "у компьютера ", computer_score)
    elif player == "mkrat":
        if computer == "tuxt":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        print ("Обший счёт: у вас", player_score, "у компьютера", computer_score)
    else:
        print("По-моему, произошла ошибка...")
    print()                             
    player = input("Выберите: qar, tuxt, kam mkrat (exit)? ")


