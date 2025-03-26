#!/usr/bin/env python3
import json
import sys
import os
import logging
from dataclasses import dataclass, asdict
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import threading
import socket
from typing import Dict, List, Optional
import pkg_resources
import base64

# Set up logging
logging.basicConfig(
    filename='/tmp/goose_personality.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@dataclass
class Instruction:
    id: str
    text: str
    created_at: str
    enabled: bool = True

@dataclass
class Style:
    name: str
    description: str
    instructions: List[Instruction]
    is_active: bool = False

class PersonalityManager:
    def __init__(self):
        self.styles: Dict[str, Style] = {}
        self.config_dir = os.path.expanduser("~/.config/goose/personality-customizer")
        self.config_file = os.path.join(self.config_dir, "config.json")
        self._load_config()
        self._init_default_styles()

    def _init_default_styles(self):
        if not self.styles:
            default_styles = {
                "friendly": Style(
                    name="friendly",
                    description="Casual and approachable responses",
                    instructions=[
                        Instruction(
                            id="friendly-1",
                            text="Use casual language and friendly tone",
                            created_at=datetime.datetime.now().isoformat()
                        )
                    ]
                ),
                "professional": Style(
                    name="professional",
                    description="Formal and business-like responses",
                    instructions=[
                        Instruction(
                            id="professional-1",
                            text="Maintain formal language and professional tone",
                            created_at=datetime.datetime.now().isoformat()
                        )
                    ]
                )
            }
            self.styles.update(default_styles)
            self._save_config()

    def _ensure_config_dir(self):
        os.makedirs(self.config_dir, exist_ok=True)

    def _load_config(self):
        self._ensure_config_dir()
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    self.styles = {
                        name: Style(
                            name=style['name'],
                            description=style['description'],
                            instructions=[
                                Instruction(**inst) for inst in style['instructions']
                            ],
                            is_active=style.get('is_active', False)
                        )
                        for name, style in data['styles'].items()
                    }
        except Exception as e:
            logging.error(f"Error loading config: {e}")
            self.styles = {}

    def _save_config(self):
        self._ensure_config_dir()
        try:
            with open(self.config_file, 'w') as f:
                json.dump({
                    'styles': {
                        name: asdict(style)
                        for name, style in self.styles.items()
                    }
                }, f, indent=2)
        except Exception as e:
            logging.error(f"Error saving config: {e}")

    def get_all_data(self) -> Dict:
        return {
            'styles': {
                name: asdict(style)
                for name, style in self.styles.items()
            }
        }

    def update_style(self, style_data: Dict) -> bool:
        try:
            name = style_data['name']
            if name in self.styles:
                self.styles[name] = Style(
                    name=style_data['name'],
                    description=style_data['description'],
                    instructions=[
                        Instruction(**inst) for inst in style_data['instructions']
                    ],
                    is_active=style_data.get('is_active', False)
                )
            else:
                self.styles[name] = Style(
                    name=name,
                    description=style_data['description'],
                    instructions=[
                        Instruction(**inst) for inst in style_data['instructions']
                    ]
                )
            self._save_config()
            return True
        except Exception as e:
            logging.error(f"Error updating style: {e}")
            return False

    def delete_style(self, style_name: str) -> bool:
        if style_name in self.styles:
            del self.styles[style_name]
            self._save_config()
            return True
        return False

    def set_active_style(self, style_name: str) -> bool:
        if style_name not in self.styles:
            return False
        
        for style in self.styles.values():
            style.is_active = False
            
        self.styles[style_name].is_active = True
        self._save_config()
        return True

class WebInterface(SimpleHTTPRequestHandler):
    def __init__(self, *args, personality_manager=None, **kwargs):
        self.personality_manager = personality_manager
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_html().encode())
        elif self.path == '/styles':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.personality_manager.get_all_data()).encode())
        else:
            self.send_error(404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode())

        if self.path == '/update_style':
            success = self.personality_manager.update_style(data)
            self.send_response(200 if success else 400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': success}).encode())
        elif self.path == '/delete_style':
            success = self.personality_manager.delete_style(data['name'])
            self.send_response(200 if success else 400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': success}).encode())
        elif self.path == '/set_active':
            success = self.personality_manager.set_active_style(data['name'])
            self.send_response(200 if success else 400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': success}).encode())
        else:
            self.send_error(404)

    def get_html(self):
        return """
<!DOCTYPE html>
<html>
<head>
    <title>Goose Personality Customizer</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .header h1 {
            margin: 0;
            color: #333;
        }
        .styles-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        .style-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .style-card.active {
            border: 2px solid #4CAF50;
        }
        .style-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        .style-title {
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
        }
        .instruction {
            background: #f8f9fa;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .instruction.disabled {
            opacity: 0.5;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        }
        button:hover {
            background-color: #45a049;
        }
        button.delete {
            background-color: #f44336;
        }
        button.delete:hover {
            background-color: #da190b;
        }
        .add-style {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #4CAF50;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.5);
        }
        .modal-content {
            background-color: white;
            margin: 10% auto;
            padding: 20px;
            width: 80%;
            max-width: 500px;
            border-radius: 10px;
        }
        .close {
            float: right;
            cursor: pointer;
            font-size: 24px;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            margin: 5px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .instruction-list {
            max-height: 200px;
            overflow-y: auto;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Goose Personality Customizer</h1>
    </div>
    <div id="styles-container" class="styles-container">
        <!-- Styles will be loaded here -->
    </div>
    <div class="add-style" onclick="showAddStyleModal()">+</div>

    <!-- Add/Edit Style Modal -->
    <div id="styleModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal()">&times;</span>
            <h2 id="modalTitle">Add Style</h2>
            <input type="text" id="styleName" placeholder="Style Name">
            <textarea id="styleDescription" placeholder="Style Description"></textarea>
            <h3>Instructions</h3>
            <div id="instructionsList"></div>
            <button onclick="addInstruction()">Add Instruction</button>
            <button onclick="saveStyle()">Save Style</button>
        </div>
    </div>

    <script>
        let currentStyles = {};
        let editingStyle = null;

        function loadStyles() {
            fetch('/styles')
                .then(response => response.json())
                .then(data => {
                    currentStyles = data.styles;
                    displayStyles();
                });
        }

        function displayStyles() {
            const container = document.getElementById('styles-container');
            container.innerHTML = '';
            
            Object.entries(currentStyles).forEach(([name, style]) => {
                const card = document.createElement('div');
                card.className = `style-card ${style.is_active ? 'active' : ''}`;
                
                card.innerHTML = `
                    <div class="style-header">
                        <span class="style-title">${style.name}</span>
                        <div>
                            <button onclick="editStyle('${style.name}')">Edit</button>
                            <button onclick="setActive('${style.name}')" ${style.is_active ? 'disabled' : ''}>
                                ${style.is_active ? 'Active' : 'Activate'}
                            </button>
                            <button class="delete" onclick="deleteStyle('${style.name}')">Delete</button>
                        </div>
                    </div>
                    <p>${style.description}</p>
                    <div class="instruction-list">
                        ${style.instructions.map(inst => `
                            <div class="instruction ${!inst.enabled ? 'disabled' : ''}">
                                <span>${inst.text}</span>
                            </div>
                        `).join('')}
                    </div>
                `;
                
                container.appendChild(card);
            });
        }

        function showAddStyleModal() {
            editingStyle = null;
            document.getElementById('modalTitle').textContent = 'Add Style';
            document.getElementById('styleName').value = '';
            document.getElementById('styleDescription').value = '';
            document.getElementById('instructionsList').innerHTML = '';
            document.getElementById('styleModal').style.display = 'block';
        }

        function editStyle(name) {
            editingStyle = name;
            const style = currentStyles[name];
            document.getElementById('modalTitle').textContent = 'Edit Style';
            document.getElementById('styleName').value = style.name;
            document.getElementById('styleDescription').value = style.description;
            
            const instructionsList = document.getElementById('instructionsList');
            instructionsList.innerHTML = '';
            style.instructions.forEach(inst => {
                addInstructionToList(inst.text);
            });
            
            document.getElementById('styleModal').style.display = 'block';
        }

        function closeModal() {
            document.getElementById('styleModal').style.display = 'none';
        }

        function addInstruction() {
            addInstructionToList('');
        }

        function addInstructionToList(text) {
            const instructionsList = document.getElementById('instructionsList');
            const div = document.createElement('div');
            div.className = 'instruction';
            div.innerHTML = `
                <input type="text" value="${text}" placeholder="Instruction text">
                <button onclick="this.parentElement.remove()">Remove</button>
            `;
            instructionsList.appendChild(div);
        }

        function saveStyle() {
            const name = document.getElementById('styleName').value;
            const description = document.getElementById('styleDescription').value;
            const instructions = Array.from(document.getElementById('instructionsList').children).map(div => ({
                id: `${name}-${Math.random().toString(36).substr(2, 9)}`,
                text: div.querySelector('input').value,
                created_at: new Date().toISOString(),
                enabled: true
            }));

            const styleData = {
                name,
                description,
                instructions,
                is_active: editingStyle ? currentStyles[editingStyle].is_active : false
            };

            fetch('/update_style', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(styleData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    loadStyles();
                    closeModal();
                }
            });
        }

        function deleteStyle(name) {
            if (confirm(`Are you sure you want to delete ${name}?`)) {
                fetch('/delete_style', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({name})
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        loadStyles();
                    }
                });
            }
        }

        function setActive(name) {
            fetch('/set_active', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name})
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    loadStyles();
                }
            });
        }

        // Load styles when page loads
        loadStyles();

        // Close modal when clicking outside
        window.onclick = function(event) {
            if (event.target == document.getElementById('styleModal')) {
                closeModal();
            }
        }
    </script>
</body>
</html>
        """

class PersonalityCustomizer:
    def __init__(self):
        self.manager = PersonalityManager()
        self.server = None
        self.server_thread = None

    def start_web_interface(self):
        if self.server:
            return

        # Find an available port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 0))
        port = sock.getsockname()[1]
        sock.close()

        # Create server
        handler = lambda *args, **kwargs: WebInterface(*args, personality_manager=self.manager, **kwargs)
        self.server = HTTPServer(('localhost', port), handler)
        
        # Start server in a thread
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

        # Open browser
        webbrowser.open(f'http://localhost:{port}')

    def stop_web_interface(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.server = None
            self.server_thread = None

    def handle_request(self, request: str) -> Dict:
        try:
            if not request:
                return self._create_response({
                    "capabilities": {},
                    "serverInfo": {
                        "name": "personality-customizer",
                        "version": "1.0.0"
                    },
                    "protocolVersion": "2024-11-05"
                })

            data = json.loads(request)
            method = data.get('method', '')
            params = data.get('params', {})

            if method == 'initialize':
                return self._create_response({
                    "capabilities": {},
                    "serverInfo": {
                        "name": "personality-customizer",
                        "version": "1.0.0"
                    },
                    "protocolVersion": "2024-11-05"
                }, data.get('id'))

            elif method == 'edit_personality':
                self.start_web_interface()
                return self._create_response({
                    "status": "Web interface opened in browser"
                }, data.get('id'))

            else:
                return self._create_error(-32601, f"Method not found: {method}", data.get('id'))

        except json.JSONDecodeError:
            return self._create_error(-32700, "Parse error", None)
        except Exception as e:
            logging.error(f"Error handling request: {e}", exc_info=True)
            return self._create_error(-32603, f"Internal error: {str(e)}", None)

    def _create_response(self, result: Dict, id: Optional[int] = None) -> Dict:
        return {
            "jsonrpc": "2.0",
            "result": result,
            "id": id
        }

    def _create_error(self, code: int, message: str, id: Optional[int]) -> Dict:
        return {
            "jsonrpc": "2.0",
            "error": {
                "code": code,
                "message": message
            },
            "id": id
        }

def main():
    customizer = PersonalityCustomizer()
    
    # Send initial response
    print(json.dumps(customizer.handle_request("")), flush=True)

    while True:
        try:
            # Read a line from stdin
            line = sys.stdin.readline()
            
            # Handle EOF
            if not line:
                break
                
            # Process the request
            response = customizer.handle_request(line.strip())
            
            # Send the response
            print(json.dumps(response), flush=True)
            
        except EOFError:
            break
        except Exception as e:
            logging.error(f"Critical error: {e}", exc_info=True)
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
    main()