# -*- coding: utf-8 -*-

__all__ = ['app']

from flask import request
from rfid import RFID

from flask import (
    Flask,
    request
)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! Marco'


@app.route('/read_tag', methods=['GET'])
def read():
    
    rfid = RFID()
    
    tag_id, tag_text = rfid.read_no_block()
    
    return {
        'id': str(tag_id),
        'text': tag_text.strip() if tag_text else tag_text
    }


@app.route('/write_tag', methods=['POST'])
def write():
    
    status = False
    text = request.json.get('text')
    
    tag_id = None
    tag_text = None
    
    if text is not None:
        
        status = True
    
        rfid = RFID()    
        tag_id, tag_text = rfid.write(text=text)
    
    return {
        'id': str(tag_id),
        'text': tag_text.strip() if tag_text else tag_text,
        'status': status
    }
