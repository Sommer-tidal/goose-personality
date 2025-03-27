#!/usr/bin/env python3
import json
import sys
import logging
import webbrowser
import http.server
import threading

# Set up logging
logging.basicConfig(
    filename='/tmp/goose_personality.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SimpleServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Goose Personality Editor</title>
            <style>
                body { 
                    font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                    max-width: 800px;
                    margin: 40px auto;
                    padding: 20px;
                    background: #f5f5f5;
                }
                .container {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                h1 { color: #333; margin-top: 0; }
                .style-card {
                    background: #f8f9fa;
                    padding: 20px;
                    margin: 10px 0;
                    border-radius: 5px;
                    border-left: 4px solid #4CAF50;
                }
                button {
                    background: #4CAF50;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover { background: #45a049; }
                input, textarea {
                    width: 100%;
                    padding: 8px;
                    margin: 5px 0;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    box-sizing: border-box;
                }
                .instructions {
                    margin: 10px 0;
                    padding: 10px;
                    background: #fff;
                    border-radius: 4px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Goose Personality Editor</h1>
                <div id="styles">
                    <div class="style-card">
                        <h3>Friendly Style</h3>
                        <div class="instructions">
                            <p>Current instructions:</p>
                            <ul>
                                <li>Use casual language</li>
                                <li>Include emojis occasionally</li>
                                <li>Be conversational and approachable</li>
                            </ul>
                        </div>
                        <button onclick="alert('Coming soon!')">Edit Instructions</button>
                    </div>
                    
                    <div class="style-card">
                        <h3>Professional Style</h3>
                        <div class="instructions">
                            <p>Current instructions:</p>
                            <ul>
                                <li>Use formal language</li>
                                <li>Maintain professional tone</li>
                                <li>Focus on clarity and precision</li>
                            </ul>
                        </div>
                        <button onclick="alert('Coming soon!')">Edit Instructions</button>
                    </div>
                </div>
                <p style="margin-top: 20px; color: #666;">
                    This is a preview of the personality editor. Full functionality coming soon!
                </p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

def handle_request(request: str) -> dict:
    try:
        if not request:
            return {
                "jsonrpc": "2.0",
                "result": {
                    "capabilities": {
                        "commands": [{
                            "name": "edit_personality",
                            "description": "Open the personality editor"
                        }]
                    },
                    "serverInfo": {
                        "name": "personality-customizer",
                        "version": "1.0.0"
                    },
                    "protocolVersion": "2024-11-05"
                },
                "id": None
            }

        data = json.loads(request)
        method = data.get('method', '')
        
        if method == 'initialize':
            logging.info("Handling initialize request")
            return {
                "jsonrpc": "2.0",
                "result": {
                    "capabilities": {
                        "commands": [{
                            "name": "edit_personality",
                            "description": "Open the personality editor"
                        }]
                    },
                    "serverInfo": {
                        "name": "personality-customizer",
                        "version": "1.0.0"
                    },
                    "protocolVersion": "2024-11-05"
                },
                "id": data.get('id')
            }
        elif method == 'edit_personality':
            logging.info("Handling edit_personality command")
            try:
                # Start web server
                port = 8765
                server = http.server.HTTPServer(('localhost', port), SimpleServer)
                thread = threading.Thread(target=server.serve_forever)
                thread.daemon = True
                thread.start()
                logging.info(f"Started web server on port {port}")
                
                # Open browser
                webbrowser.open(f'http://localhost:{port}')
                logging.info("Opened browser")
                
                return {
                    "jsonrpc": "2.0",
                    "result": {"status": "Opened personality editor"},
                    "id": data.get('id')
                }
            except Exception as e:
                logging.error(f"Failed to start web interface: {e}")
                return {
                    "jsonrpc": "2.0",
                    "error": {
                        "code": -32603,
                        "message": str(e)
                    },
                    "id": data.get('id')
                }
        else:
            logging.warning(f"Unknown method: {method}")
            return {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                },
                "id": data.get('id')
            }
    except Exception as e:
        logging.error(f"Error handling request: {e}")
        return {
            "jsonrpc": "2.0",
            "error": {
                "code": -32603,
                "message": str(e)
            },
            "id": None
        }

def main():
    logging.info("Starting personality customizer")
    print(json.dumps(handle_request("")), flush=True)
    
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                logging.info("Received EOF, exiting")
                break
                
            logging.debug(f"Received request: {line.strip()}")
            response = handle_request(line.strip())
            logging.debug(f"Sending response: {response}")
            print(json.dumps(response), flush=True)
            
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            print(json.dumps({
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": str(e)
                },
                "id": None
            }), flush=True)
            break

if __name__ == "__main__":
    main()