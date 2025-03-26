# Goose Personality Customizer

A Goose extension that allows you to customize how Goose responds to you by setting different personality styles.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Sommer-tidal/goose-personality.git
```

2. Make sure the Python script is executable:
```bash
chmod +x goose-personality/src/main.py
```

3. In Goose Desktop:
   - Open Settings
   - Click "Add Custom Extension"
   - Fill in the fields EXACTLY as shown below:

   ```
   Type: Standard IO
   ID: personality-customizer
   Name: Personality Customizer
   Description: Customize how Goose responds to you
   Command: python3 /Users/sommer/goose-personality/src/main.py
   Timeout: 30
   ```

   ⚠️ IMPORTANT: In the Command field above, replace `/Users/sommer` with your own home directory path where you cloned the repository.

## Available Commands

Once installed, you can use:

1. Get available styles:
```
/get_personality_styles
```

2. Set a style:
```
/set_style friendly
```

Available styles:
- friendly: Casual and approachable responses
- professional: Formal and business-like responses
- teacher: Educational and explanatory responses
- concise: Brief and to-the-point responses

## Troubleshooting

If you get installation errors:

1. Double-check the path in the Command field matches your clone location
2. Make sure the script is executable (chmod +x)
3. Verify Python 3 is installed and in your PATH
4. Check the logs at `/tmp/goose_personality.log` if available

## Technical Details

The extension implements the Model Context Protocol (MCP) with JSON-RPC 2.0:

### Initialization Response
```json
{
    "jsonrpc": "2.0",
    "result": {
        "capabilities": {},
        "serverInfo": {
            "name": "personality-customizer",
            "version": "1.0.0"
        },
        "protocolVersion": "2024-11-05"
    },
    "id": 1
}
```

### Command Response Format
```json
{
    "jsonrpc": "2.0",
    "result": {
        "status": "success",
        "data": {...}
    },
    "id": 1
}
```

## Development

The extension uses:
- Python 3 for the implementation
- JSON-RPC 2.0 protocol for Goose communication
- Standard IO for data transfer
- MCP (Model Context Protocol) for extension integration

To modify:
1. Edit `src/main.py`
2. Test locally
3. Remove and re-add in Goose to test changes

## License

See [LICENSE](LICENSE) file for details.