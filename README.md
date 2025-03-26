# Goose Personality Customizer

A Goose extension that allows you to customize how Goose responds to you using a friendly web interface.

## Features

- Easy-to-use web interface for managing personality styles
- Multiple built-in personality styles
- Custom instructions for each style
- Persistent storage between sessions
- Real-time updates

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

## Usage

1. In Goose, type:
```
/edit_personality
```

2. This will open a web interface in your browser where you can:
   - View all personality styles
   - Add new styles
   - Edit existing styles
   - Add/remove instructions
   - Enable/disable styles
   - Delete styles

The interface is intuitive and easy to use - just click the buttons and fill in the forms!

## Built-in Styles

The extension comes with some pre-configured styles:
- **friendly**: Casual and approachable responses
- **professional**: Formal and business-like responses

You can modify these or add your own through the web interface.

## Storage

Your personality styles and instructions are automatically saved to:
```
~/.config/goose/personality-customizer/config.json
```

## Troubleshooting

If you encounter issues:

1. Check the logs at `/tmp/goose_personality.log`
2. Make sure you have Python 3 installed
3. Verify the script is executable
4. Check that no other program is using the web interface port
5. Try restarting Goose

## Development

The extension includes:
- Python backend with web server
- Modern web interface with JavaScript
- JSON storage for persistence
- Real-time updates
- Error handling and logging

## License

See [LICENSE](LICENSE) file for details.