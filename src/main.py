#!/usr/bin/env python3
import json
import sys
import os
from typing import Dict, List, Optional
import logging
from dataclasses import dataclass, asdict
import datetime

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
                ),
                "teacher": Style(
                    name="teacher",
                    description="Educational and explanatory responses",
                    instructions=[
                        Instruction(
                            id="teacher-1",
                            text="Explain concepts clearly with examples",
                            created_at=datetime.datetime.now().isoformat()
                        )
                    ]
                ),
                "concise": Style(
                    name="concise",
                    description="Brief and to-the-point responses",
                    instructions=[
                        Instruction(
                            id="concise-1",
                            text="Keep responses brief and focused",
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

    def get_styles(self) -> List[Dict]:
        return [
            {
                "name": style.name,
                "description": style.description,
                "is_active": style.is_active,
                "instruction_count": len(style.instructions)
            }
            for style in self.styles.values()
        ]

    def get_style_details(self, style_name: str) -> Optional[Dict]:
        style = self.styles.get(style_name)
        if style:
            return asdict(style)
        return None

    def set_style(self, style_name: str) -> bool:
        if style_name not in self.styles:
            return False
        
        # Deactivate all styles
        for style in self.styles.values():
            style.is_active = False
            
        # Activate the selected style
        self.styles[style_name].is_active = True
        self._save_config()
        return True

    def add_instruction(self, style_name: str, instruction_text: str) -> Optional[Dict]:
        if style_name not in self.styles:
            return None
            
        instruction = Instruction(
            id=f"{style_name}-{len(self.styles[style_name].instructions) + 1}",
            text=instruction_text,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.styles[style_name].instructions.append(instruction)
        self._save_config()
        return asdict(instruction)

    def remove_instruction(self, style_name: str, instruction_id: str) -> bool:
        if style_name not in self.styles:
            return False
            
        style = self.styles[style_name]
        original_length = len(style.instructions)
        style.instructions = [i for i in style.instructions if i.id != instruction_id]
        
        if len(style.instructions) < original_length:
            self._save_config()
            return True
        return False

    def toggle_instruction(self, style_name: str, instruction_id: str) -> Optional[bool]:
        if style_name not in self.styles:
            return None
            
        for instruction in self.styles[style_name].instructions:
            if instruction.id == instruction_id:
                instruction.enabled = not instruction.enabled
                self._save_config()
                return instruction.enabled
        return None

class PersonalityCustomizer:
    def __init__(self):
        self.manager = PersonalityManager()

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

            elif method == 'get_personality_styles':
                return self._create_response({
                    "styles": self.manager.get_styles()
                }, data.get('id'))

            elif method == 'get_style_details':
                style_name = params.get('style')
                if not style_name:
                    return self._create_error(-32602, "Invalid params: style name required", data.get('id'))
                
                details = self.manager.get_style_details(style_name)
                if not details:
                    return self._create_error(-32602, f"Style not found: {style_name}", data.get('id'))
                
                return self._create_response({"style": details}, data.get('id'))

            elif method == 'set_style':
                style = params.get('style')
                if not style:
                    return self._create_error(-32602, "Invalid params: style required", data.get('id'))
                
                if self.manager.set_style(style):
                    return self._create_response({"status": f"Style set to {style}"}, data.get('id'))
                else:
                    return self._create_error(-32602, f"Invalid style: {style}", data.get('id'))

            elif method == 'add_instruction':
                style = params.get('style')
                instruction = params.get('instruction')
                
                if not style or not instruction:
                    return self._create_error(-32602, "Invalid params: style and instruction required", data.get('id'))
                
                result = self.manager.add_instruction(style, instruction)
                if result:
                    return self._create_response({"instruction": result}, data.get('id'))
                else:
                    return self._create_error(-32602, f"Invalid style: {style}", data.get('id'))

            elif method == 'remove_instruction':
                style = params.get('style')
                instruction_id = params.get('instruction_id')
                
                if not style or not instruction_id:
                    return self._create_error(-32602, "Invalid params: style and instruction_id required", data.get('id'))
                
                if self.manager.remove_instruction(style, instruction_id):
                    return self._create_response({"status": "Instruction removed"}, data.get('id'))
                else:
                    return self._create_error(-32602, "Instruction not found", data.get('id'))

            elif method == 'toggle_instruction':
                style = params.get('style')
                instruction_id = params.get('instruction_id')
                
                if not style or not instruction_id:
                    return self._create_error(-32602, "Invalid params: style and instruction_id required", data.get('id'))
                
                result = self.manager.toggle_instruction(style, instruction_id)
                if result is not None:
                    return self._create_response({"enabled": result}, data.get('id'))
                else:
                    return self._create_error(-32602, "Instruction not found", data.get('id'))

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