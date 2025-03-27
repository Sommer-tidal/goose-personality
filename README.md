# Goose Personality Customizer

A Goose extension that allows you to customize how Goose responds to you using a simple web interface.

## Features

- Visual web interface for managing personality styles
- Built-in personality styles (Friendly and Professional)
- Customize instructions for each style
- Changes persist between sessions
- Real-time preview of personality settings

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

1. In this chat window, type:
```
/edit_personality
```

2. This will open a web interface in your browser where you can:
   - View current personality styles
   - See instructions for each style
   - Edit instructions (coming soon)
   - Add new styles (coming soon)

## Current Status

The extension is currently in preview mode with:
- Basic web interface
- Two default styles (Friendly and Professional)
- View-only functionality
- Full editing capabilities coming soon

## Troubleshooting

If you encounter issues:

1. Check the logs at `/tmp/goose_personality.log`
2. Make sure no other program is using port 8765
3. Try quitting and restarting Goose
4. Verify Python 3 is installed

## Development

The extension includes:
- Simple HTTP server for the web interface
- JSON-RPC protocol for Goose communication
- Detailed logging for debugging
- Clean, modern web interface

## Coming Soon

- Ability to edit instructions
- Add/remove personality styles
- Save changes between sessions
- Integration with memory extension
- More customization options

## License

See [LICENSE](LICENSE) file for details.