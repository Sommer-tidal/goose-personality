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
    logging.debug("Starting request handling")
    
    # Immediately return for initialization
    if len(sys.argv) > 1 and sys.argv[1] == "--initialize":
        logging.info("Initialization flag detected")
        return {"status": "initialized"}
    
    # Check if there's any input
    if not sys.stdin.isatty():
        try:
            input_text = sys.stdin.readline()
            if not input_text.strip():
                logging.info("Empty input - returning initialized")
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
                
        except json.JSONDecodeError as e:
            logging.info(f"JSON decode error: {e}")
            return {"status": "initialized"}
        except Exception as e:
            logging.error(f"Error handling request: {e}", exc_info=True)
            return {"error": str(e)}
    else:
        logging.info("No input - returning initialized")
        return {"status": "initialized"}

if __name__ == "__main__":
    try:
        logging.info("Script started")
        result = handle_request()
        json_result = json.dumps(result)
        logging.debug(f"Sending response: {json_result}")
        print(json_result, flush=True)
        logging.info("Script completed successfully")
    except Exception as e:
        logging.error(f"Critical error: {e}", exc_info=True)
        print(json.dumps({"error": str(e)}), flush=True)