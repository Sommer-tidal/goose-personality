#!/usr/bin/env python3
import sys
import json
import logging

# Set up logging
logging.basicConfig(
    filename='/tmp/goose_personality.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def handle_request():
    # Read from stdin
    try:
        # Log that we're starting
        logging.debug("Starting request handling")
        
        # For initialization, just return success immediately
        if not sys.stdin.isatty() and sys.stdin.readable():
            input_text = sys.stdin.read()
            if not input_text.strip():
                logging.info("Initialization request detected")
                return {"status": "initialized"}
            
            input_data = json.loads(input_text)
            logging.debug(f"Received command: {input_data}")
            
            command = input_data.get('command', '')
            
            if command == 'get_personality_styles':
                return {"styles": ["friendly", "professional", "teacher", "concise"]}
            elif command == 'set_style':
                style = input_data.get('params', {}).get('style', 'default')
                return {"status": f"Style set to {style}"}
            else:
                return {"error": f"Unknown command: {command}"}
        else:
            logging.info("No input detected, assuming initialization")
            return {"status": "initialized"}
            
    except json.JSONDecodeError as e:
        logging.info(f"JSON decode error (probably initialization): {e}")
        return {"status": "initialized"}
    except Exception as e:
        logging.error(f"Error handling request: {e}", exc_info=True)
        return {"error": str(e)}

if __name__ == "__main__":
    try:
        result = handle_request()
        print(json.dumps(result), flush=True)
        logging.debug(f"Sent response: {result}")
    except Exception as e:
        logging.error(f"Critical error: {e}", exc_info=True)
        print(json.dumps({"error": str(e)}), flush=True)