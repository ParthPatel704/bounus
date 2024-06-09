from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_exe():
    try:
        exe_path = os.path.join(os.path.dirname(__file__), 'focus1.exe')
        result = subprocess.run([exe_path], capture_output=True, text=True)
        output = result.stdout
        return render_template('index.html', output=output)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
