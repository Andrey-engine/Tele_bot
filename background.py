# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 21:16:43 2023

@author: android
"""

from flask import Flask
from flask import request
from threading import Thread
import time
import requests


app = Flask('')

@app.route('/')
def home():
  return "I'm alive"

def run():
  app.run(host='0.0.0.0', port=80)

def keep_alive():
  t = Thread(target=run)
  t.start()