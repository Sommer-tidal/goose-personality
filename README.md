# Goose Personality Customizer

A Goose extension that allows you to customize how Goose responds to you by setting different personality styles.

## Features

- Multiple personality styles: friendly, professional, teacher, and concise
- Easy to switch between styles
- Customizable responses

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
   - Open Settings (gear icon in top right)
   - Go to the Extensions section
   - Click "Add Extension"
   - Select "From Directory"
   - Choose the `goose-personality` directory you just cloned

## Usage

Once installed, you can use the following commands:

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

If you encounter installation issues:

1. Check the logs at `/tmp/goose_personality.log`
2. Ensure Python 3 is installed and accessible
3. Verify the script has execute permissions
4. Make sure the paths in `extension.yaml` match your installation directory

## Development

The extension consists of:
- `extension.yaml`: Extension configuration and tool definitions
- `src/main.py`: Python script that handles the personality customization logic
- `install.sh`: Helper script for installation

To modify the extension:
1. Edit the Python script to add new functionality
2. Update the `extension.yaml` to expose new tools
3. Test locally before pushing changes

## License

See [LICENSE](LICENSE) file for details.