from flask import Flask, jsonify, request
import json
from scheduler_status import check_scheduler_status
from upcoming_meetings import fetch_upcoming_meetings
from config_manager import update_config

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def get_status():
    status = check_scheduler_status()
    
    return jsonify({'status': 'OK'})

@app.route('/meetings', methods=['GET'])
def get_meetings():
    meetings = fetch_upcoming_meetings()
    
    return jsonify({'meetings': []})

@app.route('/config', methods=['GET', 'POST'])
def manage_config():
    if request.method == 'POST':
        config_data = request.get_json()
        update_config(config_data)
        
        return jsonify({'message': 'Config updated'}), 200
    else:
        # Implement logic to get config.json
        with open('config.json', 'r') as f:
            config = json.load(f)
        return jsonify(config)

if __name__ == '__main__':
    app.run(debug=True)