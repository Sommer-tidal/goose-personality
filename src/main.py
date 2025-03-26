#!/usr/bin/env python3
import sys
import json
import os
import http.server
import webbrowser
from urllib.parse import urlparse, parse_qs

# Store custom styles in a JSON file
STYLES_FILE = os.path.join(os.path.dirname(__file__), 'custom_styles.json')

def load_custom_styles():
    if os.path.exists(STYLES_FILE):
        with open(STYLES_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_custom_styles(styles):
    with open(STYLES_FILE, 'w') as f:
        json.dump(styles, f, indent=2)

class ConfigHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/save-style':
            # Handle saving new style
            query = parse_qs(parsed_path.query)
            if 'data' in query:
                style_data = json.loads(query['data'][0])
                custom_styles = load_custom_styles()
                custom_styles[style_data['name']] = {
                    'instructions': style_data['instructions']
                }
                save_custom_styles(custom_styles)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Style saved successfully")
            return
        
        # Serve the config.html file
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(os.path.join(os.path.dirname(__file__), 'config.html'), 'rb') as f:
            self.wfile.write(f.read())

def handle_request():
    try:
        input_data = json.loads(sys.stdin.read())
        command = input_data.get('command', '')
        params = input_data.get('params', {})
        
        if command == 'configure':
            # Start the configuration server
            port = 8000
            server = http.server.HTTPServer(('localhost', port), ConfigHandler)
            webbrowser.open(f'http://localhost:{port}')
            server.handle_request()  # Handle one request then close
            return {"status": "configuration_complete"}
            
        elif command == 'set_style':
            style = params.get('style', 'default')
            result = set_style(style)
            if 'error' not in result:
                memory_cmd = {
                    "command": "remember_memory",
                    "category": "personality",
                    "data": f"preferred_style: {style}",
                    "tags": ["style", "personality"],
                    "is_global": True
                }
                print(json.dumps(memory_cmd))
            return result
            
        elif command == 'get_styles':
            return get_available_styles()
            
        else:
            return {"error": "Unknown command"}
            
    except Exception as e:
        return {"error": str(e)}

def set_style(style):
    # Built-in styles
    styles = {
        'friendly': {
            'instructions': """
            - Use a warm, conversational tone
            - Include emojis occasionally
            - Keep explanations simple and relatable
            - Use everyday examples
            """
        },
        'professional': {
            'instructions': """
            - Maintain formal language
            - Focus on precision and accuracy
            - Structure responses with clear headers
            - Include relevant technical details
            """
        },
        'teacher': {
            'instructions': """
            - Break down complex topics into simple steps
            - Use analogies to explain difficult concepts
            - Ask checking questions to ensure understanding
            - Provide examples and practice opportunities
            """
        },
        'concise': {
            'instructions': """
            - Keep responses brief and to the point
            - Use bullet points when possible
            - Focus on key information only
            - Minimize examples unless requested
            """
        }
    }
    
    # Add custom styles
    custom_styles = load_custom_styles()
    styles.update(custom_styles)
    
    if style not in styles:
        return {
            "error": f"Style '{style}' not found. Available styles: {', '.join(styles.keys())}"
        }
    
    return {
        "style": style,
        "instructions": styles[style]['instructions']
    }

def get_available_styles():
    built_in = ["friendly", "professional", "teacher", "concise"]
    custom = list(load_custom_styles().keys())
    return {
        "styles": built_in + custom
    }

if __name__ == "__main__":
    result = handle_request()
    print(json.dumps(result))