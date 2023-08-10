from itertools import combinations
import time

# example with itertools

# L = ['a', 'b', 'c', 'd']
# length = 0

# for i in combinations(L,2):
#     print(i)
#     length = length + 1
# print(length)


# calculate percentage
# V + (P/100*V)


# mesure execution time START 
start = time.time()

actions = [[20, 5], [30, 10], [50, 15],
         [70, 20], [60, 17], [80, 25],
         [22, 7], [26, 11], [48, 13],
         [34, 27], [42, 17],[110, 9],
         [38, 23], [14, 1], [18, 3],
         [8, 8], [4, 4], [10, 14],
         [24, 21], [114, 18]]

# this function takes as a parameter the array of actions.
# each tuple of the array contains the cost of an action and
# the percentage gain after two years. The function adds to 
# the tuple a third value wich is the networth after two years

def calculateGain(actions):
    globalArray = []
    for tuple in actions:
        v = tuple[0]
        p = tuple[1]
        result = v + (p/100 * v)
        tuple.append(result)
        globalArray.append(tuple)
    return globalArray

array = calculateGain(actions)
print(array)

# singleComb represente chaque combinaison

def testSampleSizeSolutions(array):
    possibleSolutions = []
    for i in reversed(range(1,21)):
        # print(i)
        for singleComb in combinations(array, i):
            # print(singleComb)
            sum = 0
            # y is equal to a single action
            for y in singleComb :
                # print(y[0])
                sum = sum + y[0]
            print("total amount : " + str(sum))
            if sum <= 500 :
                possibleSolutions.append(singleComb)
                return(possibleSolutions) 
            print(possibleSolutions)    

solutions = testSampleSizeSolutions(array)
print('single solution')
print(solutions[0])

# mesure execution time END
end = time.time()

elapsed = end - start
x = round(
elapsed, 2)

print(f'Temps d\'exécution : {x} ms')