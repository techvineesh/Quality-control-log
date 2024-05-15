import json

def search_logs(query):
    results = []
    with open(query['log1.log'], 'r') as file:
        for line in file:
            log = json.loads(line)
            if all(log.get(key) == value for key, value in query.items()):
                results.append(log)
    return results