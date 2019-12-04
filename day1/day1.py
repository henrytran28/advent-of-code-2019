#!/usr/bin/env python3

class FuelCalculator:
    def __init__(self, fileName):
        self.fileName = fileName
        with open(fileName, 'r') as reader:
            self.moduleMasses = reader.readlines()

    def findFuelNaive(self):
        totalFuel = 0
        for mass in self.moduleMasses:
            totalFuel += int(mass) // 3 - 2

        return totalFuel

    def findFuel(self):
        totalFuel = 0
        for mass in self.moduleMasses:
            fuel = int(mass) // 3 - 2
            while fuel > 0:
                totalFuel += fuel
                fuel = fuel // 3 - 2

        return totalFuel


fuelCalculator = FuelCalculator('input.txt')
print(fuelCalculator.findFuelNaive())
print(fuelCalculator.findFuel())
