class SingleRead:
    def __init__(self, fileName):
        self.fileName = fileName

    def createKmers(self):
        list1 = list()
        list2 = list()
        singleReadFile = open(self.fileName)
        Lines = singleReadFile.readlines()
        lineNumber = 0
        size = None
        for line in Lines:
            if lineNumber == 0:
                size = int(line.strip())
                lineNumber += 1
                continue
            first = line[:size - 1]
            second = line[1:size]
            list1.append(first)
            list2.append(second)
        return list1, list2

    @staticmethod
    def constructGenome(path):
        finalGenome = list()
        for i in range(len(path)):
            if i == 0:
                finalGenome.append(path[0])
            else:
                finalGenome.append(path[i][-1])

        finalGenome = ''.join(finalGenome)
        return finalGenome
