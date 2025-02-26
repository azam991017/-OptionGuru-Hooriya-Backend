from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "OptionGuru Hooriya Backend is running!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))  # Render dynamic port
    app.run(host='0.0.0.0', port=port, debug=True)
