#flask
from google import genai
from config import API_KEY #define your api key in config.py
import flask
import json
app = flask.Flask(__name__)
menu_items = ["Young Thug Pasta","Sauce it Up Soup","Signature Mushroom Chicken", "Popcorn Pizza", "Fried Chicken"]

@app.route('/search/<query>')
def index(query):
    
    query = query.replace("+", " ")
    prompt = f"ONLY RETURN JSON:From {menu_items}, find one matching '{query}' and return ONLY A JSON STRING WITHOUT FORMATTING : {{\"menu_item\": \"<the exact name from the list>\", \"reason\": \"<Brief Reason with proper grammar> like :The ITEM is great for a {query} meal!\"}}"
    
    try:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        print(response.text.splitlines()[1])
        data = json.loads(response.text.splitlines()[1])
        if data['menu_item'] not in menu_items:
            data = {"error": "Model returned an invalid menu item"}

    except json.decoder.JSONDecodeError:
        data = {"error": "Model returned an invalid response"}

    return flask.jsonify(data)
if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
