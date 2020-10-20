import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def fibonacci():
    a = 1
    b = 2
    count = 0
    fibo = "1, 2, "
    while count < 48:
        conta = a + b
        fibo = fibo + str(conta) + ','
        a = b
        b = conta
        count += 1
        fibo = fibo + "<br>"
    return fibo


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

