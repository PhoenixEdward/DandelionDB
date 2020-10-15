from flask import Flask, request, jsonify

app : Flask = Flask(__name__)

from app import views