
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# from flask import Flask,request,render_template
# app = Flask(__name__)


@app.route("/",methods=["GET","POST"])

def main():
    if request.method=="POST":
        resp = request.form
        a = resp.get('nm')
        b = resp.get('fnum')
        c = resp.get('snum')
        d = resp.get('tnum')
        e = resp.get('frnum')

        result = model.predict([[a,b,c,d,e]])

        return render_template("input.html",final = result,value1=a,value2=b,value3=c,value4=d,value5=e)

    else:
        return render_template("input.html")

if __name__ == '__main__':
    app.run(debug=True)
