# simple-rest-api
This repository contains my solution to the Breakthrough Energy contrails coding exercise.

# Prerequsites
Install ngrok. On macOS, run `brew install --cask ngrok`

# To run the Flask application:
1. Install the project dependencies using:
    ```bash
    make install
    ```
2.  Run the Flask development server using one of the following commands:
    ```bash
    make run
    ```
3.  Once the server is running, open your web browser and navigate to `http://127.0.0.1:5000/helloworld` to see the "Hello World!" message.

# API Endpoints
# # /helloworld
Returns a "Hello World!" message. Optionally accepts a tz query parameter to return the current time in a specific timezone.

Example Requests:

Get a plain "Hello World!" message:
```bash
curl http://127.0.0.1:5000/helloworld
```

Get a JSON response with the "Hello World!" message:
```bash
curl -H "Accept: application/json" http://127.0.0.1:5000/helloworld
```

Get the current time in a specific timezone (e.g. America/New_York):
```bash
curl -X GET -H "Accept: application/json" 'http://127.0.0.1:5000/helloworld?tz=America/New_York'
```

# # /unravel
Takes a JSON object as input and returns a flattened list of keys and values.

Example Request

Unravel a JSON object:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"key1": {"keyA": ["foo", 0, "bar"]}, "some other key": 2, "finally": "end"}' http://127.0.0.1:5000/unravel
```
This should return a JSON response with the flattened list of keys and values.
```bash
["key1","keyA","foo",0,"bar","some other key",2,"finally","end"]
```

# # /roll
When called, it will pull the latest code available at the HEAD of your main GitHub branch and restart the app.







