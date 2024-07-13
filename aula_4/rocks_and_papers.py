import random

CHOICES = ("pedra", "papel", "tesoura")
#scoreboard = {"cpu" : 0 , "user" : 0}
cpu_wins = 0
user_wins = 0


def update_scoreboard(winner):
    global cpu_wins, user_wins
    if winner == "CPU":
        #scoreboard["cpu"] += 1
        cpu_wins += 1
    elif winner == "User":
        #scoreboard["user"] += 1
        user_wins += 1
    else:
        print("Deu Empate")


def single_game():
    user_option = get_user_option()
    cpu_option = get_cpu_option()
    winner = who_is_winner(user_option, cpu_option)
    print(cpu_option)
    print(winner)
    update_scoreboard(winner)


def get_user_option():
    option = input("Escreve apenas uma das opções: Pedra, Papel ou Tesoura?").lower()
    while option not in CHOICES:
        option = input("Opção inválida. Escreve apenas uma das opções: Pedra, Papel ou Tesoura?").lower()
    return option


def get_cpu_option():
    return random.choice(CHOICES)


def who_is_winner(user, cpu):
    if user == cpu:
        return "Empate"
    elif user == CHOICES[0] and cpu == CHOICES[2]:
        return "User"
    elif user == CHOICES[2] and cpu == CHOICES[1]:
        return "User"
    elif user == CHOICES[1] and cpu == CHOICES[0]:
        return "User"
    else:
        return "CPU"


#while scoreboard["cpu"] < 3 and scoreboard["user"] < 3:
while cpu_wins < 3 and user_wins < 3:
    single_game()
    print("CPU "  + str(cpu_wins) + " | " + "User " + str(user_wins))
    #print(scoreboard)