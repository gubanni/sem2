import re
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = input(f"{inputText}")
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def digit_sum(sequence):
    return sum(int(d) for d in re.findall('\d', sequence)) 
num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {digit_sum(num)}")