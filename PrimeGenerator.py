'''Sito Eratostenesa.
Sprawdza czy liczba przekazana przez uzytkownika jest liczba pierwsza.
'''

def create_list(limit):
    numbers = [x for x in range(2, limit+1)]
    return numbers


def remove_multiples(value_set):
    position = 0
    limit =  max(value_set)
    while position < len(value_set):
        multiplier = 2
        x = 0
        while multiplier < len(value_set) and x < limit:
            x = value_set[position]*multiplier
            try:
                value_set.remove(x)
            except:
                pass
            multiplier += 1
        position += 1

n = eval(input())
my_list = create_list(n)
remove_multiples(my_list)

if n in my_list:
    print("TAK")
else:
    print("NIE")

print(len(my_list))