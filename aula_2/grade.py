def grade_is(percentage):
    grade = None
    if 0 > percentage <= 19:
        grade = 'Fraco'
    elif 20 <= percentage <= 49:
        grade = 'Não Satisfaz'
    elif 50 <= percentage <= 54:
        grade = 'Satisfaz pouco'
    elif 55 <= percentage <= 64:
        grade = 'Satisfaz'
    elif 65 <= percentage <= 69:
        grade = 'Satisfaz Bastante'
    elif 70 <= percentage <= 74:
        grade = 'Bom'
    elif 75 <= percentage <= 89:
        grade = 'Muito Bom'
    else:
        grade = 'Excelente'
    return grade

def graduated(grade):
    if grade in ["Satisfaz", "Satisfaz Bastante", "Bom", "Muito Bom", "Excelente"]:
        return True
    else:
        return False


percentage = int(input("Qual a nota do Aluno [0 - 100]? "))
student_grade = str(grade_is(percentage))
print("Menção Qualitativa: " + student_grade)
print("Passou? " + str(graduated(student_grade)))
