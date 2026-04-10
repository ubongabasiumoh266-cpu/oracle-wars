from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Let's pretend the current price is $70,000
    # A 'Winning' bot would fetch the real price here!
    current_price = 70000 
    
    # We add a tiny random 'wiggle' (between -5 and +5)
    prediction = current_price + random.uniform(-5, 5)
    
    return jsonify({"price": round(prediction, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
