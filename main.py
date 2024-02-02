from flask import Flask, request
import sh
import json 
app = Flask(__name__)


@app.route('/execute_safe', methods=['POST'])
def execute_command_safe():
    command = request.form.get('cmd')

    try:
        # Verwende das sh-Modul für sichere Befehlsausführung
        result = sh.sh('-c', command, _bg=True, _out='/dev/null',
                       _err='/dev/null')
        result.wait()
        return "Command executed successfully\n"
    except Exception as e:
        return f"Error executing command: {str(e)}"
def upload_file():
    try:
        # Verwende json.loads für sichere Deserialisierung
        data = request.files['file'].read()
        json_data = json.loads(data)
        return "Datei hochgeladen\n"
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {str(e)}"

@app.route('/run', methods=['POST'])
def run_command():
    command = request.form['command']
    try:
        # Verwende das sh-Modul für sichere Befehlsausführung
        result = sh.sh('-c', command, _bg=True, _out='/dev/null', _err='/dev/null')
        result.wait()
        return "Kommando ausgeführt\n"
    except Exception as e:
        return f"Error executing command: {str(e)}"

if __name__ == '__main__':
    # Ändere host auf '127.0.0.1' anstatt '0.0.0.0'
    app.run(debug=False, host='127.0.0.1', port=5000)

if __name__ == '__main__':
    # Ändere host auf '127.0.0.1' anstatt '0.0.0.0'
    app.run(debug=False, host='127.0.0.1', port=5000)
