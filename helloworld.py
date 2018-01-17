from flask import Flask, request, jsonify, Response
from pprint import pprint
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World. This is Prasath from CH-44'

@app.route('/getUserDetails/', methods=['GET'])
def userDetails():
    argA = request.args.get('a');
    argB = request.args.get('b');
    
    return "The requested value : "  + argA + "  and " + argB

@app.route('/tax', methods=["POST"])
def taxCalculate():
    colrJosnObj = request.get_json(force = True)
    print("The json requested..%s" %pprint(colrJosnObj));
    response_message = "Success"
    response_data = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
    errors = "None"
    response1 = {
        'response message' : response_message,
        'response data': response_data,
        'errors' : errors
        }
    js = json.dumps(response1)
    resp_json = Response(js, status=200, mimetype='application/json')
    print("Response data--->##### %s" %(resp_json))
    return resp_json
