#Libraries
from flask import Flask, request, jsonify, render_template
import numpy as np
from load import joblib
import os
from werkzeug.utils import secure_filename


#Load model
dt = joblib.load('dt1.joblib')

#Create Flask app
server = Flask(__name__)

#Define a route to send a JSON data
@server.route('/predictjason', methods=['POST'])
