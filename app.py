from flask import Flask, request, jsonify
from datetime import datetime

import logging
import os
import pytz
import subprocess
import sys

app = Flask(__name__)


@app.route("/helloworld", methods=["GET"])
def helloworld():
    """
    Returns a "Hello World!" message.
    Optionally accepts a tz query parameter to return the current time in a specific timezone.
    """
    message = "Hello World!"
    tz_param = request.args.get("tz")

    if tz_param:
        try:
            tz = pytz.timezone(tz_param)
            # Example format: 2025-05-12 19:30:00 PDT-0700
            current_time_str = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z%z")
            message = f"Hello World! It is {current_time_str} in timezone {tz_param}."
        except pytz.exceptions.UnknownTimeZoneError:
            return jsonify({"error": "Invalid timezone designator: {tz_param}"}), 400

    accept_header = request.headers.get("Accept")
    if accept_header == "application/json":
        return jsonify({"message": message})
    return message


@app.route("/unravel", methods=["POST"])
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


@app.route("/roll", methods=["GET"])
def roll():
    """Pull latest code and reboot server"""
    git_pull_command = ["git", "pull", "origin", "main"]
    process = subprocess.run(
        git_pull_command, capture_output=True, text=True, check=True, cwd=os.getcwd()
    )
    logging.info(f"Git pull successful:\n{process.stdout}")

    return jsonify(
        {
            "status": "success",
            "message": "Update received, server restarting...",
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
