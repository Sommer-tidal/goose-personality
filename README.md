# Goose Personality Customizer

A Goose extension that allows you to customize how Goose responds to you by creating and managing personality styles with custom instructions.

## Features

- Multiple built-in personality styles
- Custom instructions for each style
- Persistent storage between sessions
- Detailed logging for troubleshooting
- User-friendly command interface

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

### View Available Styles
```
/get_personality_styles
```
Lists all available personality styles with their descriptions and status.

### View Style Details
```
/get_style_details friendly
```
Shows all instructions and settings for a specific style.

### Set Active Style
```
/set_style friendly
```
Activates a specific personality style.

### Add Instruction
```
/add_instruction friendly "Use more emojis in responses"
```
Adds a new instruction to a style.

### Remove Instruction
```
/remove_instruction friendly friendly-1
```
Removes an instruction from a style (use the instruction ID from style details).

### Toggle Instruction
```
/toggle_instruction friendly friendly-1
```
Enables or disables an instruction (use the instruction ID from style details).

## Built-in Styles

- **friendly**: Casual and approachable responses
- **professional**: Formal and business-like responses
- **teacher**: Educational and explanatory responses
- **concise**: Brief and to-the-point responses

## Storage and Persistence

Your personality styles and instructions are stored in:
```
~/.config/goose/personality-customizer/config.json
```

## Logging

Logs are written to:
```
/tmp/goose_personality.log
```

## Troubleshooting

If you encounter issues:

1. Check the logs at `/tmp/goose_personality.log`
2. Verify the config directory exists: `~/.config/goose/personality-customizer`
3. Make sure the script is executable
4. Check that Python 3 is installed

## Technical Details

The extension implements:
- JSON-RPC 2.0 protocol
- Persistent storage using JSON
- Structured logging
- Error handling with detailed messages

### Data Structure

Each style contains:
- Name
- Description
- List of instructions
- Active status

Each instruction has:
- Unique ID
- Text content
- Creation timestamp
- Enabled status

## Development

To modify the extension:
1. Edit `src/main.py`
2. Test changes locally
3. Remove and re-add in Goose to test

### Adding New Features

To add new functionality:
1. Add new methods to `PersonalityManager` class
2. Add corresponding handlers in `PersonalityCustomizer.handle_request()`
3. Update the config save/load methods if needed

## License

See [LICENSE](LICENSE) file for details.