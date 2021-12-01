# Get data for challenge 
# ** Could not automate via http request:
# Url same for everyone but data is different. 
# There may be some args to add that would provide access
 
dataFile = open('advent1/advent1_data.txt', 'r')

dataIntList = []
for line in dataFile.readlines():
    dataIntList.append(int(line))

def countIncreases(intList):
    result = 0
    for i in range(len(intList)):
        if i > 0:
            if intList[i] > intList[i-1]:
                result += 1
    return result

print(countIncreases(dataIntList))

def countIncreasesSlidingWindow(intList):
    result = 0
    for i in range(len(intList)):
        # break if at the last window
        if i == len(intList) - 3:
            break

        firstWindow = list(intList[ix] for ix in [i, (i+1), (i+2)])
        secondWindow = list(intList[ix] for ix in [(i+1), (i+2), (i+3)])

        if sum(firstWindow) < sum(secondWindow):
            result += 1
    return result

print(countIncreasesSlidingWindow(dataIntList))