import random

one = []
two = []
three = []
four = []
five = []
six = []

lenOne = 0
lenTwo = 0
lenThree = 0
lenFour = 0
lenFive = 0
lenSix = 0

throwingDiceTimes = input("Ange antal kast: ")
throwingDiceTimes = int(throwingDiceTimes)

for z in range(throwingDiceTimes):
    randomNumber = random.randint(1, 6)
    if randomNumber == 1:
        one.append(randomNumber)
    elif randomNumber == 2:
        two.append(randomNumber)
    elif randomNumber == 3:
        three.append(randomNumber)
    elif randomNumber == 4:
        four.append(randomNumber)
    elif randomNumber == 5:
        five.append(randomNumber)
    elif randomNumber == 6:
        six.append(randomNumber)

    print(z, randomNumber)

lenOne = len(one)
lenTwo = len(two)
lenThree = len(three)
lenFour = len(four)
lenFive = len(five)
lenSix = len(six)

print(one, two, three, four, five, six)

print("-----------------------------------------------------------------------")

print("Ett ",len(one), (lenOne / throwingDiceTimes) * 100, "%")
print("Två ",len(two), (lenTwo / throwingDiceTimes) * 100, "%")
print("tre ",len(three), (lenThree / throwingDiceTimes) * 100, "%")
print("Fyra ",len(four), (lenFour / throwingDiceTimes) * 100, "%")
print("Fem ",len(five), (lenFive / throwingDiceTimes) * 100, "%")
print("Sex ",len(six), (lenSix / throwingDiceTimes) * 100, "%")