# Lists

number_list = [2, 3, 1]
number_list_two = [0, 1, 2, 3]

number_list.insert(3, 4)
print(number_list)


print(number_list.index(3))

number_list.extend(number_list_two)
print(number_list)



# Tuple

ice_cream_topping = ("M&M's", "Chocolate", "Caramelo", "Chocolate", "Chocolate")
print(ice_cream_topping)

number_of_chocolate = ice_cream_topping.count("Chocolate")

print(number_of_chocolate)

ice_cream_topping = ("Olá")
print(ice_cream_topping)

# Dictionary

project_dictionary = {"language": "Python", "developers": 3, "QAs": 1}
project_dictionary["PO"] = 1
print(project_dictionary)

element_of_dictionary = project_dictionary.keys()
print(element_of_dictionary)
value_of_dictionary = project_dictionary.values()
print(value_of_dictionary)

# Set

hospital_menu = {"Pescada cozida com Todos", "Frango cozido com Arroz Branco", "Sopa de Legumes"}
hospital_menu.add("Infelizmente fomos eliminados")
print(hospital_menu)
hospital_menu.discard("Cacete de agulha")
print(hospital_menu)


# String
euro = "Portugal vai ganhar isto com uma perna às costas"
print(euro[8:])