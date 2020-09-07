from flask import Flask, jsonify,request
from flask_cors import CORS,cross_origin
from sympy import Integral, Symbol,sympify,S, solve,Derivative,Limit,simplify,cos,sin,log, latex,pprint
import sys, json
import sympy
import math 
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

CORS(app)

def calc(a):
    #Since our input would only be having one line, parse our JSON data from that
    x = eval(a)
    x= str(x)
    x = x.replace('sqrt','√')
    x = x.replace('**','^') 
    x=x.replace('I','√(-1)')
    x =x.replace('oo','∞')
    x = x.replace('>=','⩾')
    x = x.replace('<=','⩽')
    return x

@app.route('/python', methods=['POST','GET'])
@cross_origin()
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_data()
        print(post_data)
        g= str(post_data)
        print(g)
        g = g[1:]
        print( g )
        x = eval(post_data)
        x= str(x)
        print(x)
        x = x.replace('sqrt','√')
        x = x.replace('**','^') 
        x = x.replace('I','√(-1)')
        x = x.replace('oo','∞')
        x = x.replace('>=','⩾')
        x = x.replace('<=','⩽')
        
        #x= eval(post_data)
        #response_object=x
 
    return jsonify(x)
if __name__ == '__main__':
    app.run()