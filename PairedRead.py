class PairedRead:
    def __init__(self, fileName):
        self.fileName = fileName

    def createPairedKmers(self):
        list1 = list()
        list2 = list()
        pairedReadFile = open(self.fileName)
        lines = pairedReadFile.readlines()
        lineNumber = 0
        gapSize = None
        kSize = None
        for line in lines:
            if lineNumber == 0:
                kSize, gapSize = line.strip().split()
                kSize = int(kSize)
                gapSize = int(gapSize)
                lineNumber += 1
            else:
                read = line.strip().split('|')
                list1.append(''.join([read[0][: kSize - 1], read[1][: kSize - 1]]))
                list2.append(''.join([read[0][1: kSize], read[1][1: kSize]]))
        return list1, list2, kSize, gapSize

    @staticmethod
    def prefixSuffix(path, kSize):
        suffixList = list()
        prefixList = list()
        for item in path:
            prefixList.append(item[:kSize - 1])
            suffixList.append(item[kSize - 1:])
        return prefixList, suffixList

    @staticmethod
    def reconstructGenome(prefixList, suffixList):
        prefix = list()
        suffix = list()
        for i in range(len(prefixList)):
            if i != len(prefixList) - 1:
                prefix.append(prefixList[i][0])
                suffix.append(suffixList[i][0])
            else:
                prefix.append(prefixList[i])
                suffix.append(suffixList[i])
        prefix = ''.join(prefix)
        suffix = ''.join(suffix)

        return prefix, suffix

    @staticmethod
    def finalGenome(prefix, suffix, k, d):
        suffixLength = len(suffix) - (k + d)
        return prefix + suffix[suffixLength:]
