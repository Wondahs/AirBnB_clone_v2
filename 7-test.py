#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import state
from models import storage


states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
for state in states:
    print(state.name)
