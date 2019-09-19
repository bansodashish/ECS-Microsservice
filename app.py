from flask import Flask
import json
import os

app = Flask(__name__)

@app.route("/")

def reverse_slicing(s):
    return s[::-1]

input_str = 'ABç∂EF'

if __name__ == "__main__":
    print('Reverse String using slicing =', reverse_slicing(input_str))