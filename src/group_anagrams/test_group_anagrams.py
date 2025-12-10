from group_anagrams import (
    group_anagrams,
    isInList,
    addToHash,
    sortString,
    areAnagrams,
)

def test_sortString():
    input: str = "fbcadge"
    expected: str = "abcdefg"
    assert(sortString(input)) == expected

def test_areAnagrams():
   str1: str = "fbcadge"
   str2: str = "abcdefg"
   assert(areAnagrams(str1, str2))

def test_isInList():
    myList: list[str] = ['a', 'u', '5']
    assert(isInList(myList, 'u'))
    assert(isInList(myList, 'x')) == False

def test_addToHash():
    myHash: dict[str, list[str]] = { }
    addToHash(myHash, "foo", "bar")
    assert("foo" in myHash)
    assert(myHash) == { "foo": ["bar"]}
    addToHash(myHash, "foo", "wow")
    assert(isInList(myHash["foo"], "bar"))
    assert(isInList(myHash["foo"], "wow"))

def test_group_anagrams():
    assert(group_anagrams(['foo'])) == [["foo"]]

    input: list[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected: list[list[str]] = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert(group_anagrams(input)) == expected

def test_group_anagramsEmptyInput():
    assert(group_anagrams([])) == []

def test_group_anagramsRepeatedWords():
    input: list[str] = ["eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea"]
    expected: list[list[str]] = [["eat", "tea", "ate", "eat", "tea"], ["tan", "nat"], ["bat"]]

    assert(group_anagrams(input)) == expected
