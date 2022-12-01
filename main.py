from PairedRead import PairedRead
from SingleRead import SingleRead


def startEndPoint(firstList, secondList):
    startPoint = list(set(firstList) - set(secondList))
    endPoint = list(set(secondList) - set(firstList))
    return startPoint[0], endPoint[0]


def findingPath(firstList, secondList, starPoint, endPoint):
    path = list()
    path.append(starPoint)
    while starPoint != endPoint:
        for i in range(len(firstList)):
            if starPoint == firstList[i]:
                path.append(secondList[i])
                starPoint = secondList[i]
    return path


def showResults(firstList, secondList, start, end, path, prefix, suffix, result, readOutput):
    print('list 1:', firstList)
    print('list 2:', secondList)
    print('Start Point:', start)
    print('End Point:', end)
    if prefix != '' and suffix != '':
        print('Prefix:', prefix)
        print('Suffix:', suffix)
    print('Path:', path)
    print('Final Genome:', result)
    print('Read Output :', readOutput)


if __name__ == '__main__':
    print('1) Single Read \n2) Paired Read \nYour Choice: ')
    choice = int(input())
    if choice == 1:
        singleReadFileName = 'test_cases/p2/SingleReadsInput.txt'
        singleRead = SingleRead(singleReadFileName)
        list1, list2 = singleRead.createKmers()
        startPoint, endPoint = startEndPoint(list1, list2)
        path = findingPath(list1, list2, startPoint, endPoint)
        finalGenome = singleRead.constructGenome(path)
        readOutput = open('test_cases/SingleReadsOutput.txt').readline().strip()
        showResults(list1, list2, startPoint, endPoint, path, '', '', finalGenome, readOutput)

    elif choice == 2:
        pairedReadFileName = 'test_cases/p2/ReadPairsInput.txt'
        pairedRead = PairedRead(pairedReadFileName)
        list1, list2, kSize, gapSize = pairedRead.createPairedKmers()
        startPoint, endPoint = startEndPoint(list1, list2)
        path = findingPath(list1, list2, startPoint, endPoint)
        prefixList, suffixList = pairedRead.prefixSuffix(path, kSize)
        prefix, suffix = pairedRead.reconstructGenome(prefixList, suffixList)
        finalGenome = pairedRead.finalGenome(prefix, suffix, kSize, gapSize)
        readOutput = open('test_cases/ReadPairsOutput.txt').readline().strip()
        showResults(list1, list2, startPoint, endPoint, path, prefix, suffix, finalGenome, readOutput)
