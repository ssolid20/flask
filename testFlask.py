from flask import Flask, jsonify,request
from flask_cors import CORS,cross_origin
from sympy import Integral, Symbol,sympify,S,diff,exp,nonlinsolve,linsolve,Abs, solve,Derivative,Limit,simplify,cos,sin,log, latex,pprint
import sys, json
from sympy.solvers.inequalities import reduce_abs_inequality
import sympy
import math 
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# configuration

# instantiate the app
app = Flask(__name__)
#app.config.from_object(__name__)

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

@app.route('/',methods=['GET'])
def origin():
    return "<h1>Welcome to our server !!</h1>"

@app.route('/python', methods=['POST','GET'])
@cross_origin()
def all_books():
    if request.method == 'POST':
        post_data = request.get_data()
        print(post_data)
        g= str(post_data)
        print(g)
        g = g[1:]
        print( g )
        try:
            b=post_data.replace('}',')')
            b=b.replace('sin{','sin(')
            b=b.replace('cos{','cos(')
            b=b.replace('tan{','tan(')
           
            x = eval(b)
            x= str(x)
            print(x)
            x = x.replace('sqrt','√')
            x = x.replace('**','^') 
            x = x.replace('I','√(-1)')
            x = x.replace('exp(','e^(')
            x = x.replace('oo','∞')
            x = x.replace('>=','⩾')
            x = x.replace('<=','⩽')
            x=x.replace('3.14159265358979','π')
            x=x.replace('2.71828182845905','e')
        except:
            x= "Couldn't regonise problem or there are no solutions, try again"   
        finally:
            x = x.replace('sqrt','√')
            x = x.replace('**','^') 
            x = x.replace('I','√(-1)')
            x = x.replace('exp(','e^(')
            x = x.replace('oo','∞')
            x = x.replace('>=','⩾')
            x = x.replace('<=','⩽')
            x=x.replace('3.14159265358979','π')
            x=x.replace('2.71828182845905','e')
        
        #x= eval(post_data)
        #response_object=x
 
    return jsonify(x)
if __name__ == '__main__':
    app.run(threaded=True)
