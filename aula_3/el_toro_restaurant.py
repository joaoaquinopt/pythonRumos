# numbers = [1, 2, 3, 4]
# for numbers in numbers:
#     print(numbers)

# person = {"Name": "Paulo", "age": 30, "city": "Porto"}
# for key in person:
#     value = person[key]
#     print(key + ": " + str(value))

# total = 0
# for number in range(1, 11):
#  total += number
# print("Sum for 1 to 10 is: ", total)

# lucky_number = 7
# inputed = int(input("Lucky Number: "))
# while inputed != lucky_number:
#  inputed = int(input("Lucky Number: "))
# print("You got lucky!")

# counter = 0
# while counter < 5:
#  print("Count :", counter)
#  counter += 1
# print("Loop finished!")

# for number in range(1, 11):
#  if number == 2 :
#  continue
#  print(number)
#
# for number in range(1, 11):
#  if number == 3 :
#  break
#  print(number)
#
# for number in range(1, 11):
#  pass

import random


def loop_one(chef_name):
    # for list
    # chef go through the ingredients available in the fridge and use only the first letter from each
    # should be print a message like "Chef Lino a pegar no T"
    fridge = ["Tomate", "Alface", "Salpicão", "Curgete", "Ananás"]
    for ingredientes in fridge:
        print(f'{chef_name} a pegar no ' + ingredientes[0])


def loop_two(chef_name):
    # for dictionary
    # chef should find "Faca" and print something like "Chef Lino encontrou a Faca no " + cabinet
    kitchen_cabinets = {"FRIGORÍFICO": "Garfo", "ARMÁRIO": "Concha", "CHÃO": "Faca"}
    for key in kitchen_cabinets:
        if kitchen_cabinets[key] == "Faca":
            value = kitchen_cabinets[key]
            print(f'{chef_name} encontrou {value} no {key}')


def loop_three(chef_name):
    # for range
    # chef should chop everything three times from 1 to 3
    # each time should be print a message like "Chef Lino cortou 1" with number being incremented

    for corte in range(1, 4):
        print(f'{chef_name} cortou {corte}')


def loop_four(chef_name):
    # while counter
    # should be printed the microwave countdown from 5 until 0
    # after this count down a message should print as the following "Chef Lino acabou de preparar o prato!"

    counter = 5
    while counter >= 0:
        print(f'Microwave Countdown {counter}')
        counter -= 1

    print(f'Tim! {chef_name} acabou de aquecer o prato!')


# Do not change anything on this method
def is_salted():
    return random.choice([True, False])


def loop_five(chef_name):
    # while state not met
    # if the food needs more salt it is print something like - use method is_salted
    # "Cliente: Eish... o Chef Lino esqueceu-se do sal. Tenho que colocar mais!"
    # when the loop finishes it should be print "Cliente: A comida está perfeita!"
    esta_salgado = is_salted()

    while (esta_salgado == False):
        print("Cliente: Eish... o Chef Lino esqueceu-se do sal. Tenho que colocar mais!")
        esta_salgado = is_salted()

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