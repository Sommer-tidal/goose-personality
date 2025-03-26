#!/usr/bin/env python3
import sys
import json

def handle_request():
    # Read the input from stdin
    try:
        input_data = json.loads(sys.stdin.read())
        command = input_data.get('command', '')
        params = input_data.get('params', {})
        
        if command == 'set_style':
            style = params.get('style', 'default')
            return set_style(style)
        elif command == 'get_styles':
            return get_available_styles()
        else:
            return {"error": "Unknown command"}
            
    except Exception as e:
        return {"error": str(e)}

def set_style(style):
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
    
    if style not in styles:
        return {
            "error": f"Style '{style}' not found. Available styles: {', '.join(styles.keys())}"
        }
    
    return {
        "style": style,
        "instructions": styles[style]['instructions']
    }

def get_available_styles():
    return {
        "styles": [
            "friendly",
            "professional",
            "teacher",
            "concise"
        ]
    }

if __name__ == "__main__":
    result = handle_request()
    print(json.dumps(result))