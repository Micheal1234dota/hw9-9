from flask import Flask
from flask import render_template
from flask import request
import random

app=Flask(__name__)

@app.route('/')
def show_quotes():
    fp=open('../inspiration.txt','r')
    line=random.randint(0,len(fp.readlines())-1)
    fp.seek(0)
    quote=fp.readlines()[line]
    fp.close()
    return render_template(
            'quote.html',
            quote=quote
            )
