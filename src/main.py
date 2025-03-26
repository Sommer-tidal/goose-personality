#!/usr/bin/env python3
import json
import sys

def handle_request(request):
    try:
        if not request:
            return {"jsonrpc": "2.0", "result": {"status": "success"}, "id": None}
            
        data = json.loads(request)
        method = data.get('method', '')
        
        if method == 'initialize':
            return {
                "jsonrpc": "2.0",
                "result": {
                    "capabilities": {},
                    "serverInfo": {
                        "name": "personality-customizer",
                        "version": "1.0.0"
                    }
                },
                "id": data.get('id')
            }
        elif method == 'get_personality_styles':
            return {
                "jsonrpc": "2.0",
                "result": {
                    "styles": ["friendly", "professional", "teacher", "concise"]
                },
                "id": data.get('id')
            }
        elif method == 'set_style':
            style = data.get('params', {}).get('style', 'default')
            return {
                "jsonrpc": "2.0",
                "result": {
                    "status": f"Style set to {style}"
                },
                "id": data.get('id')
            }
        else:
            return {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                },
                "id": data.get('id')
            }
    except json.JSONDecodeError:
        return {
            "jsonrpc": "2.0",
            "error": {
                "code": -32700,
                "message": "Parse error"
            },
            "id": None
        }
    except Exception as e:
        return {
            "jsonrpc": "2.0",
            "error": {
                "code": -32603,
                "message": f"Internal error: {str(e)}"
            },
            "id": None
        }

def main():
    while True:
        try:
            # Read a line from stdin
            line = sys.stdin.readline()
            
            # Handle EOF
            if not line:
                break
                
            # Process the request
            response = handle_request(line.strip())
            
            # Send the response
            print(json.dumps(response), flush=True)
            
        except EOFError:
            break
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {str(e)}"
                },
                "id": None
            }
            print(json.dumps(error_response), flush=True)
            break

if __name__ == "__main__":
    # Handle initialization immediately
    print(json.dumps({
        "jsonrpc": "2.0",
        "result": {
            "capabilities": {},
            "serverInfo": {
                "name": "personality-customizer",
                "version": "1.0.0"
            }
        },
        "id": 1
    }), flush=True)
    
    # Then enter the main loop
    main()