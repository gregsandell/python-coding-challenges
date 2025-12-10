from Logger import Logger

def test_newLogger():
    myLogger = Logger()
    assert(isinstance(myLogger, Logger))

def test_log():
    myLogger = Logger()
    assert(myLogger.log("this is my message")) == None

def test_get_logs():
    myLogger = Logger()
    myLogger.log("this is my message")
    logs = myLogger.get_logs()
    assert(logs[0]["message"]) == "this is my message"

def test_search_on_message():
    myLogger = Logger()
    mesg1 = "hello now"
    mesg2 = "now is the time"
    mesg3 = "hello later"
    myLogger.log(mesg1, 'INFO')
    myLogger.log(mesg2, 'DEBUG')
    myLogger.log(mesg3, 'ERROR')
    result = myLogger.search(keyword="now")
    assert(any(mesg1 in obj["message"] for obj in result))
    assert(any(mesg2 in obj["message"] for obj in result))
    assert(any(mesg3 in obj["message"] for obj in result)) == False

def test_search_on_level():
    myLogger = Logger()
    myLogger.log("anything", "INFO")
    myLogger.log("anything", 'ERROR')
    myLogger.log("anything", "INFO")
    result = myLogger.search(keyword="INFO", field="level")
    assert(len(result)) == 2
    assert(item == "INFO" for item.level in result)

def test_wildcard_everything():
    myLogger = Logger()
    myLogger.log("anything", "INFO")
    myLogger.log("anything", 'ERROR')
    myLogger.log("anything", "INFO")
    result = myLogger.search()
    assert(len(result)) == 3

