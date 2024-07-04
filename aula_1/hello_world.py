#def imprimir(nome, sobrenome):
    #return (nome + sobrenome)

#nomeSobrenome = imprimir('Joao ', 'Aquino')
#print(nomeSobrenome)

# name = str(input('Qual é o teu primeiro nome: '))
# surname = str(input('Qual é o teu apelido: '))
# print(name + " " + surname)

# fazer função/método que imprima um texto
# criar uma variável com um valor e imprimi-la posteriormente


def imprimirTexto():
    name = str(input('Qual é o teu primeiro nome? '))
    surname = str(input('Qual é o teu apelido? '))
    return name + " " + surname


name_surname = imprimirTexto()
print(name_surname)


