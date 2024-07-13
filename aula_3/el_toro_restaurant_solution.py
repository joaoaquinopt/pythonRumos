import random


def loop_one(chef_name):
    # for list
    # chef go through the ingredients available in the fridge and use only the first letter from each
    # should be print a message like "Chef Lino a pegar no T"
    fridge = ["Tomate", "Alface", "Salpicão", "Curgete", "Ananás"]

    for ingredient in fridge:
        print(chef_name + " a pegar no " + ingredient[0])


def loop_two(chef_name):
    # for dictionary
    # chef should find "Faca" and print something like "Chef Lino encontrou a Faca no " + cabinet
    kitchen_cabinets = {"FRIGORÍFICO": "Garfo", "ARMÁRIO": "Concha", "CHÃO": "Faca"}

    for cabinet in kitchen_cabinets:
        if "Faca" in kitchen_cabinets[cabinet]:
            print(chef_name + " encontrou a Faca no " + cabinet)
            break


def loop_three(chef_name):
    # for range
    # chef should chop everything three times from 1 to 3
    # each time should be print a message like "Chef Lino cortou 1" with number being incremented
    for iteration in range(1, 4):
        print(chef_name + " cortou " + str(iteration))


def loop_four(chef_name):
    # while counter
    # should be printed the microwave countdown from 5 until 0
    # after this count down a message should print as the following "Chef Lino acabou de preparar o prato!"
    counter = 5
    while counter >= 0:
        print(counter)
        counter -= 1

    print(chef_name + " acabou de preparar o prato!")


# Do not change anything on this method
def is_salted():
    return random.choice([True, False])



def loop_five(chef_name):
    # while state not met
    # if the food needs more salt it is print something like
    # "Cliente: Eish... o Chef Lino esqueceu-se do sal. Tenho que colocar mais!"
    # when the loop finishes it should be print "Cliente: A comida está perfeita!"
    while not is_salted():
        print("Cliente: Eish... o " + chef_name + " esqueceu-se do sal. Tenho que colocar mais!")
    print("Cliente: A comida está perfeita!")


def kitchen_process(chef_name):
    print("--------------------------------El Toro--------------------------------")
    print("Empregado: " + chef_name + ", temos aqui o primeiro pedido - uma Salada à lá Progratomática")
    print(chef_name + ": a ir buscar os ingredientes")
    loop_one(chef_name)
    print(chef_name + ": Agora preciso da faca... Onde a deixei?")
    loop_two(chef_name)
    print(chef_name + ": Vamos lá cortar isto")
    loop_three(chef_name)
    print(chef_name + ": Agora só falta ir ao microondas...")
    loop_four(chef_name)
    print(chef_name + ": Empregado pode levar o pedido 352")
    loop_five(chef_name)


kitchen_process("Chef Lino")
