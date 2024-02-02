import os
import subprocess
import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_command():
    # Issue B301: Avoid using pickle to deserialize untrusted data
    try:
        file = request.files['file'].read()
        data = pickle.loads(file)
    except Exception as e:
        return f"Error: {str(e)}"

    # Issue B602: Avoid subprocess call with shell=True
    try:
        subprocess.run(data, check=True)
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {str(e)}"

    return "Command executed successfully\n"

@app.route('/execute_safe', methods=['POST'])
def execute_command_safe():
    # Issue B605: Avoid using os.system with untrusted input
    command = request.form.get('cmd')
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {str(e)}"

    return "Command executed successfully\n"

if __name__ == '__main__':
    # Issue B201: Avoid running Flask app with debug=True in production
    app.run(debug=False, host='0.0.0.0', port=5000)
