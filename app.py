from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/run_exe', methods=['GET'])
def run_exe():
    try:
        # Path to your .exe file
        exe_path = './focus1.exe'
        
        # Run the .exe file
        result = subprocess.run([exe_path], capture_output=True, text=True)
        
        # Return the output of the .exe file
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
