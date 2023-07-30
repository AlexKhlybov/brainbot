# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


def delimet_91():
    numbers = range(11, 90)

    while True:
        num = random.choice(numbers)
        rslt = str(num/91)[:8]
        print("=" * 40)
        numbs = input(f"Сколько будет ({num}:91) = ")
        if numbs == "exit":
            break
        if rslt == str(numbs)[:8]:
            print(f"Отлично! Ты великолепен!")
        else:
            print(f"К сожалению не верно!")
            print(f"Ответ: {rslt}")

        print("=" * 40, "\n")

def sort_letter():
    while True:
        print("=" * 40)

        world = str(input(f"Введите слово: ")).lower()
        if world == "exit":
            break

        rslt = str(input(f"Введите ответ: ")).lower()
        if rslt == "exit":
            break

        world_sort = "".join(sorted(list(world)))

        if world_sort == rslt:
            print(f"Отлично, ответ верный! Ты великолепен!")
        else:
            print(f"Ответ: {world_sort}")
            print(f"К сожалению не верно! Попробуй ещё раз!")
        print("=" * 40, "\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # delimet_91()
    sort_letter()
