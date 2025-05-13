from flask import Flask

app = Flask(__name__)

@app.route('/helloworld', methods=['GET'])
def helloworld():
    """A simple endpoint that returns "Hello World!"
    """
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)