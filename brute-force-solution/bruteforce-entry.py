from itertools import combinations
import time
import csv

# example with itertools

# L = ['a', 'b', 'c', 'd']
# length = 0

# for i in combinations(L,2):
#     print(i)
#     length = length + 1
# print(length)


# calculate percentage
# V + (P/100*V)

file = open('../DATA/dataset1.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)

actions = []
for row in csvreader:
    actions.append(row)


start = time.time()

# actions = [[20, 5], [30, 10], [50, 15],
#          [70, 20], [60, 17], [80, 25],
#          [22, 7], [26, 11], [48, 13],
#          [34, 27], [42, 17],[110, 9],
#          [38, 23], [14, 1], [18, 3],
#          [8, 8], [4, 4], [10, 14],
#          [24, 21], [114, 18]]

# this function takes as a parameter the array of actions.
# each tuple of the array contains the cost of an action et 
# the percentage gain after two years. The function adds to 
# the tuple a third value wich is the networth after two years

def calculGain(actions):
    globalArray = []
    for tuple in actions:
        v = float(tuple[1])
        p = float(tuple[2])
        result = v + (p/100 * v)
        tuple.append(result)
        globalArray.append(tuple)
    return globalArray

array = calculGain(actions)

# singleComb represente chaque combinaison

def testSampleSizeSolutions(array):
    possibleSolutions = []
    for i in reversed(range(1,9)):
        print('je suis la')
        print(i)
        for singleComb in combinations(array, i):
            # print('singleComb')
            # print(singleComb)
            sum = 0
            # y is equal to a single action
            for y in singleComb :
                sum = sum + float(y[1])
            # print("total amount : " + str(sum))
            if sum <= 500 :
                possibleSolutions.append(singleComb)
                #print(singleComb)
                # print("selected " + str(sum))
            else :
                # print('value too high')
                print('')
        if len(possibleSolutions) > 0:
            # print('voici les differentes options possibles')
            # print('dans un echantillon de :')
            # print(i)
            
            return(possibleSolutions)      

solutions = testSampleSizeSolutions(array)

# O(n3)

def findMaxGain(solutions):
    bestSolution = 0 
    for singleSolution in solutions : 
        # print(singleSolution)
        total = 0
        for action in singleSolution : 
            finalValue = float(action[3])
            total = total + finalValue
        # print('total gain')
        # print(total)
        if total >= bestSolution :
            bestSolution = total
            selectedSolution = singleSolution
    #     print(' ')
    print(selectedSolution)
    # print(bestSolution)

findMaxGain(solutions)

end = time.time()

elapsed = end - start
x = round(
elapsed, 2)

print(f'Temps d\'exécution : {x} ms')