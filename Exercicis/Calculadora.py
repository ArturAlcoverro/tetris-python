import sys

# Llibreria que utilitzem per la funcio "reduce", la qual ens serveix per convinar els valors de les llistes
import functools

# Operacions
MULT = "multiplicar"
DIV = "dividir"
SUM = "sumar"
REST = "restar"
EXP = "exponent"

operaciones = [MULT, DIV, SUM, REST, EXP]


# Funció per printar els resultat
def print_resultat(nums, resultat, simbol):
    print(nums.pop(0), end="")
    for num in nums:
        print(f" {simbol} {num}", end="")
    print(f" = {resultat}")


# Funció que calcula la suma i printa el resultat
def suma(nums):
    r = functools.reduce(lambda a, b: a + b, nums)
    print_resultat(nums, r, "+")


# Funció que calcula la resta i printa el resultat
def resta(nums):
    r = functools.reduce(lambda a, b: a - b, nums)
    print_resultat(nums, r, "-")


# Funció que calcula la multiplicació i printa el resultat
def mult(nums):
    r = functools.reduce(lambda a, b: a * b, nums)
    print_resultat(nums, r, "*")


# Funció que calcula la divisio i printa el resultat
def div(nums):
    r = functools.reduce(lambda a, b: a / b, nums)
    print_resultat(nums, r, "/")


# Funció que calcula l'exponent i printa el resultat
def exp(nums):
    r = functools.reduce(lambda a, b: a ** b, nums)
    print_resultat(nums, r, "^")


if __name__ == '__main__':
    try:

        # Agafem el valors rebuts per parametre i comprobem que siguin valids
        operacio = sys.argv[1].lower()
        if operacio not in operaciones:
            raise Exception('')
        nums = []
        for i in range(2, len(sys.argv)):
            nums.append(int(sys.argv[i]))

        # Segons l'operacio rebuda per parametre executem una funcio
        if operacio == MULT:
            mult(nums)
        elif operacio == DIV:
            div(nums)
        elif operacio == SUM:
            suma(nums)
        elif operacio == REST:
            resta(nums)
        elif operacio == EXP:
            exp(nums)

    # Excepcions
    except ValueError as e:
        print("Numero invalid!")
    except ZeroDivisionError as e:
        print("No pots dividir entre 0")
    except Exception as e:
        print("Operació invalida!")
