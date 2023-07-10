def powerset(inputSet):
    result = []
    backtrack(inputSet, [], result)
    return result

def backtrack(inputSet, currentSet, result):
    result.append(currentSet[:])
    for i in range(len(inputSet)):
        currentSet.append(inputSet[i])
        backtrack(inputSet[i+1:], currentSet, result)
        currentSet.pop()

