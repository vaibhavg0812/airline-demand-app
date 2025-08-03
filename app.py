from flask import Flask, render_template, request, redirect
import pandas as pd
import os
from datetime import datetime
from collections import Counter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            df = pd.read_csv(filepath, parse_dates=['Date'])
            df['Route'] = df['Origin'] + " → " + df['Destination']

            daily_demand = df.groupby('Date')['Passengers'].sum().reset_index()
            top_routes = df.groupby('Route')['Passengers'].sum().nlargest(5).reset_index()
            summary = df.groupby('Route')['Passengers'].agg(['sum', 'mean']).reset_index()
            summary.columns = ['Route', 'Total Passengers', 'Average Passengers']

            return render_template('results.html',
                                   daily_labels=daily_demand['Date'].dt.strftime('%Y-%m-%d').tolist(),
                                   daily_values=daily_demand['Passengers'].tolist(),
                                   route_labels=top_routes['Route'].tolist(),
                                   route_values=top_routes['Passengers'].tolist(),
                                   table=summary.to_dict(orient='records'))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
