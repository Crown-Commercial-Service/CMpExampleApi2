import os
import sys
import uuid

from datetime import datetime

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from psutil import cpu_count, virtual_memory

from ccsexampleapi2.api_config import ApiConfig

app = Flask(__name__)

@app.route("/")
def healthcheck():
    return "OK"

@app.route("/systeminfo")
def systeminfo():
    result_map = {
        'all': (id, date_time, properties, environment, available_processors, total_memory, max_memory, free_memory),
        'properties': (id, date_time, properties, available_processors, total_memory, max_memory, free_memory),
        'environment': (id, date_time, environment, available_processors, total_memory, max_memory, free_memory),
        'basic': (id, date_time)
    }

    results = {}
    methods = result_map[request.args.get('detail', 'basic')]
    for method in methods:
        key, value = method()
        results[key] = value

    return jsonify(results)

    
def id():
    return ('id', uuid.uuid4())

def date_time():
    return ('dateAndTime', datetime.utcnow().strftime("%A, %d. %B %Y %I:%M%p"))

def properties():
    properties = {
        'platform': sys.platform,
        'path': sys.path,
        'modules': list(sys.modules.keys())
    }
    return ('properties', properties)

def environment():
    return ('environment', {k: v for k, v in os.environ.items()})

def available_processors():
    return ('availableProcessors', cpu_count())

def total_memory():
    return ('totalMemory', virtual_memory().total)

def max_memory():
    return ('maxMemory', virtual_memory().available)

def free_memory():
    return ('freeMemory', virtual_memory().free)