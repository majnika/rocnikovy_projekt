import json

from client_py.client import Client
from pattern_py.pattern import Pattern

client = Client()

with open(r"proto\patterns\ping-pong.json") as f:
    print(json.load(f))
    f.seek(0)
    print(client.add_pattern(Pattern(json.load(f))))

print(client._patterns)
