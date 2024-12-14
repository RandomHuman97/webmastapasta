#flask

import flask
import requests
import json
app = flask.Flask(__name__)
modeltimeout = 60
menu_items = ["Young Thug Pasta","Sauce it Up Soup","Signature Mushroom Chicken", "Popcorn Pizza", "Fried Chicken"]

@app.route('/search/<query>')
def index(query):
    query = query.replace("+", " ")
    prompt = f"ONLY RETURN JSON:From {menu_items}, find one matching '{query}' and return ONLY A JSON STRING : {{\"menu_item\": \"<the exact name from the list>\", \"reason\": \"<Brief Reason with proper grammar> like :The ITEM is great for a {query} meal!\"}}"
    payload = {'model': 'llama3.2',
                'prompt': prompt,
                  "stream": False,}
    print(payload)
    try:
        response = requests.post('http://localhost:11434/api/generate', json=payload, timeout=modeltimeout)
        data = response.json()['response']
        #remove square brackets
        data = data.replace("[","").replace("]","")
        print(data)
        
        data = json.loads(data)
        if data['menu_item'] not in menu_items:
            data = {"error": "Model returned an invalid menu item"}

    except requests.exceptions.Timeout:
        data = {"error": "Model took too long to respond"}
    except json.decoder.JSONDecodeError:
        data = {"error": "Model returned an invalid response"}

    return flask.jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)
