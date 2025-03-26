#!/usr/bin/env python3
import sys
import json

def handle_request():
    # Immediate initialization response
    if len(sys.argv) > 1 and sys.argv[1] == "--init":
        return {"status": "initialized"}
    
    # Read command from stdin
    try:
        input_data = json.loads(sys.stdin.read())
        command = input_data.get('command', '')
        
        if command == 'get_personality_styles':
            return {"styles": ["friendly", "professional", "teacher", "concise"]}
        elif command == 'set_style':
            style = input_data.get('params', {}).get('style', 'default')
            return {"status": f"Style set to {style}"}
        else:
            return {"error": f"Unknown command: {command}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    result = handle_request()
    print(json.dumps(result), flush=True)