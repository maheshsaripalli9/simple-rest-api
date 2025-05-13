from flask import Flask, request, jsonify
from datetime import datetime

import pytz

app = Flask(__name__)

@app.route('/helloworld', methods=['GET'])
def helloworld():
    """
    Returns a "Hello World!" message. 
    Optionally accepts a tz query parameter to return the current time in a specific timezone.
    """
    message = "Hello World!"
    tz_param = request.args.get('tz')

    if tz_param:
        try:
            tz = pytz.timezone(tz_param)
            # Example format: 2025-05-12 19:30:00 PDT-0700
            current_time_str = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')
            print(current_time_str)
            message = f"Hello World! It is {current_time_str} in timezone {tz_param}."
        except pytz.exceptions.UnknownTimeZoneError:
            return jsonify({"error": "Invalid timezone designator: {tz_param}"}), 400

    accept_header = request.headers.get('Accept')
    if accept_header == 'application/json':
        return jsonify({"message": message})
    return message

@app.route('/unravel', methods=['POST'])
def unravel():
    """
    Takes a JSON body in the request and returns a flat list
    of its keys and values in the order they appear.
    """
    data = request.get_json()
    result = []
    def unravel_helper(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                result.append(k)
                unravel_helper(v)
        elif isinstance(obj, list):
            for item in obj:
                unravel_helper(item)
        else:
            result.append(obj)
    unravel_helper(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
