import json
import datetime

def log_to_file(log, file_path):
    log['timestamp'] = datetime.datetime.utcnow().isoformat()
    with open('config.json', 'a') as file:
        file.write(json.dumps(log) + '\n')

# Example usage:
log = {
    "level": "error",
    "log_string": "Inside the Search API",
    "metadata": {
        "source": "log3.log"
    }
}
log_to_file(log, 'log3.log')
