from flask import Flask, jsonify, request
from services.armazenamento import Armazenamento
from models.cliente import Cliente
from models.produto import Produto

if __name__ == "__main__":
    app.run(debug=True, port=5000)
