
import flask
from flask import Flask
from flask import jsonify 
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


spells = json.load(open("files/spells.json"))


app=Flask(__name__)
CORS(app)



@app.route('/')



def home():
    allspellnames = []

    for spell in spells:
        allspellnames.append(spell)
    
    return jsonify(allspellnames)

# def home():
#     return a


if __name__ == "__main__":
    app.run(debug=True)


#to run a flask app
#flask run 