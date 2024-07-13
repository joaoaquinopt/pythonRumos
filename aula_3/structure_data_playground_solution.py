# Lists
number_list = [2, 3, 1]

number_list.append(4)
number_list.sort()

print("---Lista---")
print(number_list)

# Tuple
ice_cream_topping = ("M&M's", "Chocolate", "Caramelo")

print("---Tuplo---")
print(ice_cream_topping)
print(ice_cream_topping.index("Chocolate"))

# Dictionary
project_dictionary = {"language": "Python", "developers": 3, "QAs": 1}

project_dictionary["designers"] = 1

print("---Dicionário---")
print(project_dictionary)

# Set
hospital_menu = {"Pescada cozida com Todos", "Frango cozido com Arroz Branco", "Sopa de Legumes"}

hospital_menu.clear()
hospital_menu.add("Pizza")

print("---Set---")
print(hospital_menu)

# String
euro = "Portugal vai ganhar isto com uma perna às costas"

euro = euro.replace("ganhar", "perder")

print("---Strings---")
print(euro)
