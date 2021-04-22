import json

class Database:
    def load(self, filename="result.json"):
        with open(filename, 'r') as fp:
            return json.load(fp)