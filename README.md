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
   - Open Settings
   - Click "Add Custom Extension"
   - Fill in the fields EXACTLY as shown below:

   ```
   Type: Standard IO
   ID: personality-customizer
   Name: Personality Customizer
   Description: Customize how Goose responds to you
   Command: python3 /Users/sommer/goose-personality/src/main.py --initialize
   Timeout: 30
   ```

   ⚠️ IMPORTANT: In the Command field above, replace `/Users/sommer` with your own home directory path where you cloned the repository.

   - Click "Add" to save the extension

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

1. Make sure you copied the Command field exactly as shown, including the `--initialize` at the end
2. Check that the path in the Command field matches where you cloned the repository
3. Ensure Python 3 is installed and accessible
4. Verify the script has execute permissions
5. If it still doesn't work, check the logs at `/tmp/goose_personality.log`

## Development

The extension consists of:
- `src/main.py`: Python script that handles the personality customization logic
- Logs are written to `/tmp/goose_personality.log` for debugging

To modify the extension:
1. Edit the Python script to add new functionality
2. Test locally before pushing changes
3. If you make changes, you'll need to remove and re-add the extension in Goose settings

## License

See [LICENSE](LICENSE) file for details.