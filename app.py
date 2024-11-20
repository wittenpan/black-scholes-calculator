from flask import Flask, render_template, request, jsonify
from models.black_scholes import BlackScholesModel
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    try:
        model = BlackScholesModel(
            time_to_maturity=data['time_to_maturity'],
            risk_free_rate=data['risk_free_rate'],
            volatility=data['volatility'],
            current_price=data['current_price'],
            strike_price=data['strike_price']
        )
        result = model.calculate()
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/generate_heatmap', methods=['POST'])
def generate_heatmap():
    try:
        data = request.get_json()
        
        #create price and volatility ranges
        prices = np.linspace(float(data['current_price']) * 0.5, 
                            float(data['current_price']) * 1.5, 50)
        vols = np.linspace(float(data['volatility']) * 0.5, 
                          float(data['volatility']) * 1.5, 50)
        
        #calculate option prices for each combination
        Z = np.zeros((len(prices), len(vols)))
        for i, price in enumerate(prices):
            for j, vol in enumerate(vols):
                model = BlackScholesModel(
                    time_to_maturity=data['time_to_maturity'],
                    risk_free_rate=data['risk_free_rate'],
                    volatility=vol,
                    current_price=price,
                    strike_price=data['strike_price']
                )
                Z[i, j] = model.calculate()
        
        #create heatmap
        plt.clf()
        fig = plt.figure(figsize=(10, 8))
        plt.imshow(Z, extent=[vols[0], vols[-1], prices[0], prices[-1]], aspect='auto', origin='lower')
        plt.colorbar(label='Option Price')
        plt.xlabel('Volatility')
        plt.ylabel('Stock Price')
        plt.title('Black-Scholes Option Price Heatmap')
        
        #convert plot to base64 string
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        plt.close(fig)
        
        return jsonify({'image': base64.b64encode(img.getvalue()).decode()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) 