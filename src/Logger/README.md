# Logger
This was a code challenge given me in Dev 2025 as part of an interview with
Fox Studios.  It was one of a group of five challenges.  It was later evaulated
in a panel interview zoom meeting with Crystal Maginnes, Aaron Stephanus and Natalia Buscaglia.

The instructions were very brief:
> **Task 3 – OOP Design & API Thinking**
> Create a Logger class with log, get_logs, and search using a dummy API or Open API.

That was all!  ChatGpt helped me infer what they were really after.

## Part 1: Logger code
This is in ___init__.py_ and is tested with `testpy -v`.

## Part 2: HTTP Rest Service API

Steps to test the API (`App/main.py`):

In terminal:
2. go to directory src/task3_logger/App
2. Run `uvicorn main:app --reload`

> Note: entered logs do not persist beyond the current uvicorn session

Testing with Curl:
Add a log line with the `/log` PUT endpoint:

1. View stored logs with the `/logs` GET endpoint:
> curl --location 'http://127.0.0.1:8000/logs'

2. Add a log with the `/log` PUT endpoint:
```javascript
curl --location 'http://127.0.0.1:8000/log' \
--header 'Content-Type: application/json' \
--data '{ "message": "Hello world, how are you?", "level": "INFO"}'
```
3. Search logs with the `/logs/search` GET endpoint:
  * Search by message:
```javascript
curl --location 'http://127.0.0.1:8000/logs/search?keyword=world&field=message'
``` 
  * Search by level (e.g. INFO, ERROR, DEBUG)
```javascript
curl --location 'http://127.0.0.1:8000/logs/search?keyword=world&field=message'
``` 

