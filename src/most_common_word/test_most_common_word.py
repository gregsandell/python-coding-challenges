from most_common_word import sanitize, filterStopWords, makeWordCountMap, findMaxWord, most_common_word

class TestFindMaxWord:
    def test_winner(self):
        assert(findMaxWord({ "now": 8, "is": 6, "the": 10, "time": 2})) == "the"
    def test_firstWinnerWins(self):
        assert(findMaxWord({ "now": 2, "is": 1, "the": 1, "time": 2})) == "now"
    def test_emptyInput(self):
        assert(findMaxWord({ })) == ""

class TestFilterStopWords:
    def test_no_stopwords(self):
        assert filterStopWords(["now", "is", "the", "time"]) == ["now", "is", "the", "time"]
    def test_empty_list_makes_empty_list(self):
        assert filterStopWords([]) == []
    def test_some_stopwords(self):
        stopwords = set(["frank", "not"])
        assert filterStopWords(["now", "frank", "is", "not", "the", "time"], stopwords) == ["now", "is", "the", "time"]
    def test_everyWordIsInStopwords(self):
        assert filterStopWords(["now", "is", "the", "time"], set(["now", "is", "the", "time"])) == []
    def test_emptySetStopwords(self):
        stopwords = set([])
        assert filterStopWords(["now", "frank", "is", "not", "the", "time"], stopwords) == ["now", "frank", "is", "not", "the", "time"]

class TestMakeWordCountMap:
    def test_no_repeated_words(self):
        assert(makeWordCountMap(["now", "is", "the", "time"])) == { "now": 1, "is": 1, "the": 1, "time": 1}
    def test_some_repeated_words(self):
        assert(makeWordCountMap(["now", "now", "is", "the", "time", "time"])) == { "now": 2, "is": 1, "the": 1, "time": 2}
    def test_empty_list_makes_empty_object(self):
        assert(makeWordCountMap([])) == { }

class TestSanitize:
    def test_lower_case_words(self):
        assert sanitize("now is the time") == ["now", "is", "the", "time"]

    def test_punctuation(self):
        assert sanitize("now; is! the,, time") == ["now", "is", "the", "time"]

    def test_capitals(self):
        assert sanitize("nOw iS tHe TiMe") == ["now", "is", "the", "time"]

    def test_allows_apostrophes(self):
        assert sanitize("now's is the time's") == ["now's", "is", "the", "time's"]

    def test_spaces(self):
        assert sanitize("now    is      the time    ") == ["now", "is", "the", "time"]

class TestMostCommonWord:
    def test_winner(self):
        input = "now now now now now now now now is is is is is is the the the the the the the the the the time time"
        assert(most_common_word(input)) == "the"

    def testFirstWordWins_withStopwords(self):
        stopwords = set(["frank", "not"])
        assert most_common_word("now frank is not the time frank", stopwords) == "now"
    def testFirstWordWins_noStopwords(self):
        assert most_common_word("now frank is not the time frank") == "frank"
    def testAllInputIsStopwords(self):
        stopwords = set(["now", "frank", "is", "not", "the", "time"])
        assert most_common_word("now frank is not the time frank", stopwords) == None
    def testIgnoreNonAlphanumerics(self):
        assert most_common_word("now, frank! is@ not     the    time frank*") == "frank"



