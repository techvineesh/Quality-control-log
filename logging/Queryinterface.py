import json

def search_logs(query):
    results = []
    with open(query['error.log'], 'r') as file:
        for line in file:
            log = json.loads(line)
            if all(log.get(key) == value for key, value in query.items()):
                results.append(log)
    return results

# Example usage:
query = {
    "level": "error",
    "metadata": {
        "source": "log3.log"
    }
}
results = search_logs(query)
for result in results:
    print(result)
