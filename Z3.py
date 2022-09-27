import random

def createlist():
    xs = []
    for i in range(10):
        xs.append(random.randint(0,20))
    return xs
list = createlist()
print(f"исходный список:\n {list}")
random.shuffle(list)
print(f"список после перемешивания:\n{list}")