#!/usr/bin/env python3

class ShipComputer:
    def __init__(self, fileName):
        self.fileName = fileName
        with open(fileName, 'r') as reader:
            self.code = [int(x) for x in reader.readline().split(',')]

    def runProgram(self):
        codeCopy = self.code
        for i in range(0, len(codeCopy) - 3, 4):
            op, a, b, c = codeCopy[i], codeCopy[i+1], codeCopy[i+2], codeCopy[i+3]
            if op == 99:
                break
            elif op == 1:
                codeCopy[c] = codeCopy[a] + codeCopy[b]
            else:
                codeCopy[c] = codeCopy[a] * codeCopy[b]

        return codeCopy[0]

    def setAlarmState(self, noun, verb):
        self.code[1] = noun
        self.code[2] = verb

    def getInputsFromTarget(self, target):
        for i in range(99):
            for j in range(99):
                self.setAlarmState(i, j)
                if shipComputer.runProgram() == target:
                    return i, j
        return -1, -1

# Part 1
shipComputer = ShipComputer('input.txt')
shipComputer.setAlarmState(12, 2)
output = shipComputer.runProgram()
print(output)

# Part 2
noun, verb = shipComputer.getInputsFromTarget(19690720)
print(noun, verb)



