# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request
import requests
import json
import pandas as pd
import numpy as np
from utils.scrapping import url_to_string

# Initialization of the Flask App
app = Flask(__name__)

# Index
@app.route('/')
def homepage():
    return render_template('index.html')

# url homepage
@app.route('/home')
def home():
    return render_template('scrapper.html')

# Retrieve url (POST method)
@app.route('/get_article', methods=['POST','GET'])
def get_url():

    # When the user clicks on submit
    if request.method == 'POST':

        url = request.form['text']
        article = url_to_string(url)



    return render_template('scrapper.html', article=article)
