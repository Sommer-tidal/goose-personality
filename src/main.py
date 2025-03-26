#!/usr/bin/env python3
import sys
import json
import logging
import select

# Set up logging
logging.basicConfig(
    filename='/tmp/goose_personality.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def handle_request(input_text):
    logging.debug(f"Handling request: {input_text}")
    
    try:
        if not input_text.strip():
            logging.info("Empty input - returning initialized")
            return {"status": "initialized"}
        
        input_data = json.loads(input_text)
        logging.debug(f"Parsed JSON: {input_data}")
        
        method = input_data.get('method', '')
        
        if method == 'initialize':
            return {"status": "initialized"}
        elif method == 'get_personality_styles':
            return {"styles": ["friendly", "professional", "teacher", "concise"]}
        elif method == 'set_style':
            style = input_data.get('params', {}).get('style', 'default')
            return {"status": f"Style set to {style}"}
        else:
            return {"error": f"Unknown method: {method}"}
            
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")
        return {"error": f"Invalid JSON: {str(e)}"}
    except Exception as e:
        logging.error(f"Error handling request: {e}", exc_info=True)
        return {"error": str(e)}

def main():
    logging.info("Script started - entering main loop")
    
    while True:
        try:
            # Check if there's input available
            if select.select([sys.stdin], [], [], 0.1)[0]:
                input_text = sys.stdin.readline()
                if not input_text:  # EOF
                    logging.info("Received EOF, exiting")
                    break
                    
                result = handle_request(input_text)
                json_result = json.dumps(result)
                logging.debug(f"Sending response: {json_result}")
                print(json_result, flush=True)
            
        except KeyboardInterrupt:
            logging.info("Received KeyboardInterrupt, exiting")
            break
        except Exception as e:
            logging.error(f"Critical error in main loop: {e}", exc_info=True)
            print(json.dumps({"error": str(e)}), flush=True)
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)