#!/usr/bin/env python3
def findFuel(fileName):
    totalFuel = 0
    with open(fileName, 'r') as reader:
        for mass in reader.readlines():
            totalFuel += int(mass) // 3 - 2

    return totalFuel

def findActualFuel(fileName):
    totalFuel = 0
    with open(fileName, 'r') as reader:
        for mass in reader.readlines():
            fuel = int(mass) // 3 - 2
            while fuel > 0:
                totalFuel += fuel
                fuel = fuel // 3 - 2

    return totalFuel


output = findFuel('input.txt')
output2 = findActualFuel('input.txt')
print(output)
print(output2)
