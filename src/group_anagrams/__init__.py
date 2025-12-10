
def areAnagrams(str1: str, str2: str) -> bool:
    return sortString(str1) == sortString(str2)

def sortString(s: str) -> str:
    return ''.join(sorted(list(s)))

def isInList(myList: list, target: str) -> bool:
    index = myList.index(target) if target in myList else -1
    return index != -1

def addToHash(myHash: dict[str, list[str]],  sortedString: str, actualString: str)-> None:
    myHash.setdefault(sortedString, []).append(actualString)

def group_anagrams(strList: list[str]):
    myHash: dict[str, list[str]] = {}
    result: list[list[str]] = []

    for s in strList:
        addToHash(myHash, sortString(s), s)
    for key, value in myHash.items():
        result.append(value)
    return result
