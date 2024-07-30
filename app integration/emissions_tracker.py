"""This program includes code that can be integrated into the university app to track emissions from food orders."""

from flask import Flask, request, jsonify
import pandas as pd 

app = Flask(__name__)

# Load the emissions data
data = pd.read_csv('../data/food_emissions.csv')