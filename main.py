from SingleRead import SingleRead


def showResults(firstList, secondList, start, end, path, result):
    print('list 1:', firstList)
    print('list 2:', secondList)
    print('Start Point:', start)
    print('End Point:', end)
    print('Path:', path)
    print('Result:', result)


if __name__ == '__main__':
    singleReadFile = 'SingleReadInput.txt'
    singleRead = SingleRead(singleReadFile)
    list1, list2 = singleRead.createKmers()
    start, end = singleRead.startEndPoint(list1, list2)
    path = singleRead.findingPath(list1, list2, start, end)
    finalGenome = singleRead.constructGenome(path)
    showResults(list1, list2, start, end, path, finalGenome)
