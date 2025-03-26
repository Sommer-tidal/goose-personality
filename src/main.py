#!/usr/bin/env python3
import json
print(json.dumps({"jsonrpc": "2.0", "result": {"status": "success"}, "id": 1}), flush=True)
while True:
    try:
        line = input()
        print(json.dumps({"jsonrpc": "2.0", "result": {"status": "success"}, "id": 1}), flush=True)
    except EOFError:
        break