from flask import Flask, request, jsonify 
import json 
from core.handling import get_entity


app = Flask(__name__) 


@app.route('/named-entity', methods=['POST'])
def get_named_entity():
    data = request.json 

    if data != None:
        text = data["sentence"]
        entities = get_entity(text) 
        return json.dumps(entities, default=str)
    
    else:
        return jsonify({"message": "Give proper input"}), 422



if __name__ == "__main__":
    app.run(debug=True)