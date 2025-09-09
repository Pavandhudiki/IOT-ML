from flask import Flask
from model import generateAi
import pickle

generateAI()
ai=pickle.load(open("ai.pkl","rb"))
app=Flask(__name__)

app.route("/")
def homepage():
    return "Server Running"

@app.route("/predict")#/predict?it=0
def predict():
    ir=request.args.get("ir")
    ir=int(ir)
    data=[[ir]]
    result=ai.predict(data)[0]#["object"]
    return result

if(__name__)=="__main__":
    app.run(host='0.0.0.0',port=3000)