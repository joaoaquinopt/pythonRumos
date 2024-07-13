def print_pair_numbers():
    """
    Exercise: Pair Numbers
    Print pair numbers from 1 to 20.
    """
    counter = 1
    pair_number = []

    while counter <= 20:
        if counter % 2 == 0:
            pair_number.append(counter)
        counter += 1

    return print(pair_number)


# print_pair_numbers()


def sum_odd_numbers():
    """
    Exercise: Sum Odd Numbers
    Sum odd numbers from 1 to 50.
    """
    counter = 1
    sum = 0
    odd_number = []

    while counter <= 50:
        if counter % 2 != 0:
            sum = sum + counter
            odd_number.append(counter)
        counter += 1

    print(sum)
    print(odd_number)


# sum_odd_numbers()

def is_palindrome(word):
    """
    Exercise: Is Palindrome
    Confirm if the word given is read starting either from 1 letter or last letter.
    Print True if it is a palindrome, False if not
    Examples of palindromes: ana, radar, abba
    """
    # word = input("qual a palavra?")
    reverse_word = word[::-1]
    if word == reverse_word:
        print(f'It is a palindrome : {word} = {reverse_word}')
    else:
        print("It is not a palindrome")


is_palindrome("ANa")


def counting_vowels(phrase):
    """
    Exercise: Counting All Vowels
    Print the number of vowels in a given phrase
    """
    pass


def is_prime(number):
    """
    Exercise: Is Prime
    Print if a number is prime or not.
    """
    pass


def get_biggest_number(numbers):
    """
    Exercise: What is the highest number?
    From the given numbers list, find out the biggest number
    """
    pass


def factorial_of(number):
    """
    Exercise: Factorial of
    Given an integer number return his factorial.
    Factorial is the multiplication of all integers until the given one.
    Eg Factorial of 5 will be: 5 * 4 * 3 * 2 * 1
    """
    pass


def add_to_shopping_list():
    """
    Exercise: Add To Shopping List
    Create a 3 products list and try to add a new one.
    Only add it if it doesn't is already available
    If it is already there print that the element has already there
    """
    pass


def average_of(numbers):
    """
    Exercise: Average of Numbers List
    From a given numbers list, print the average
    """
    pass


def count_digits(number):
    """
    Exercise: How many digits?
    From a given integer, return the digits count.
    Eg 10 = 2 digits
    """
    pass


def sort_numbers(numbers):
    """
    Exercise: Sort it
    Sort the numbers list
    """
    pass


def are_words_with_the_same_letters(word_one, word_two):
    """
    Exercise: Words with same letters?
    Print True if words have the same letters.
    Eg Roma and Amor, Lapa and Pala
    """
    pass


def convert_length_to_km(value, length_unit):
    """
    Exercise: Convert to KM
    Convert any value in Centimeters or Decimeters or Meters to Kilometers
    """
    pass


def minimum_amount_of_coins_in_change(price, cash_given):
    """
    Exercise: Give minimum numbers of coins change in a transaction
    Coins are unlimited but only for 1 and 0.05 - which means price can only end as .00 or .05
    Eg price = 14.5 and cash_given = 20 should return 5 of 1 and 10 of 0.05
    """
    pass


def fizz_buzz():
    """
    Exercise: FizzBuzz
    Print numbers from 1 to 200 except if:
        the number is divided by 3 then print "Fizz"
        the number is divided by 5 then print "Buzz"
        the number is divided by 3 and 5 then print "FizzBuzz"
    """
    pass