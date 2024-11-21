from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return 'HOLA!!!!!!!!!!!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)