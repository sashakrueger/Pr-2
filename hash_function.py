import random

def hash_f(arg):
    number = 0
    next_num = 0
    a = 5
    b = 4
    c = random.randint(1024, 4096)
    for i in arg:
        number += int(ord(i))//len(arg)
        number_1 = int((number ** a // len(arg)))

    while number_1:
        num_2 = number_1 >> b
        next_num += num_2 % c

        return next_num

while True:

    welcome = input("\nВведите \"esc\" для выхода\nВведите сообщение для хэширования: ")

    if welcome == "esc":
        print("\nВыход")
        break

    else:

        hash_f(welcome)

    print(f"Хэш-код: {hash_f(welcome)}")
