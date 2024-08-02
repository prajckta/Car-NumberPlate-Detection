
from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_detection')
def start_detection():
    try:
        subprocess.run(['python', 'main.py'])
        # return redirect(url_for('detected_number'))  # Redirect to detected_number.html
        
    except Exception as e:
        return f'Error starting detection: {str(e)}'

# @app.route('/detected_number')
# def detected_number():
#     # You can pass any necessary data to the detected_number.html template here
#     detected_number = "ABC123"  # Example detected number
#     return render_template('detected_number.html', detected_number=detected_number)

if __name__ == '__main__':
    app.run(debug=True)
