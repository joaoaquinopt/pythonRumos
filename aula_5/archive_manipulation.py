import os

file_path = os.path.abspath("text.txt")


def count_total_words(file_path):

    total_words = 0

    with open("text.txt", "r") as db:
        lines = db.readlines()
        total_words = counting_words(lines)
    return total_words


def overwrite_text(file_path, line):

    with open(file_path, "w") as db:
        db.write(line)
    return file_path, line



def counting_words(lines):

    total_words = 0

    for line in lines:
        words = line.split(",")
        total_words += len(words)

    return total_words



def main():

    file_path = "text.txt"
    total_words = count_total_words(file_path)
    print(f"Número total de palavras: {total_words}")

    text = "H E L L O"
    overwrite_text(file_path, text)

    total_words = count_total_words(file_path)
    print(f"Número total de palavras: {total_words}")


main()
