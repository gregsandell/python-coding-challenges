import re

def findMaxWord(countDict: dict[str, int]) -> str:
    if not countDict:
        return ""  # handle empty dict
    return max(countDict, key=countDict.get)

def makeWordCountMap(textList: list[str]) -> dict:
    wordMap = { }
    for word in textList:
        if word in wordMap:
            wordMap[word] += 1
        else:
            wordMap[word] = 1
    return wordMap

def filterStopWords(textList: list[str], stopwords: set[str] | None = None) -> list[str]:
    if stopwords is None:
        stopwords = set()

    def not_stopword(word: str) -> bool:
        return word not in stopwords

    filteredText = list(filter(not_stopword, textList))
    return filteredText

sanitize = lambda text: re.findall(r"[a-z']+", text.lower())

def most_common_word(text: str, stopwords: set[str] | None = None) -> str | None:
    cleaned_words = sanitize(text)
    filtered_words = filterStopWords(cleaned_words, stopwords)
    word_counts = makeWordCountMap(filtered_words)
    result = findMaxWord(word_counts)

    return None if result == "" else result

