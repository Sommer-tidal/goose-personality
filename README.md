# Goose Personality Extension

A customizable extension for modifying Goose's personality and response style. This extension allows you to switch between predefined styles or create your own custom personality styles through a web interface.

## Installation

There are two ways to install this extension:

### Method 1: Direct Installation (Recommended)

1. Open Goose
2. Go to Settings → Extensions
3. Click "Add Custom Extension"
4. Fill in:
   - Type: Standard IO
   - ID: `personality-customizer`
   - Name: `Personality Customizer`
   - Description: `Customize Goose's personality and response style`
   - Command: `curl -s https://raw.githubusercontent.com/Sommer-tidal/goose-personality/main/src/main.py > /tmp/goose_personality.py && python3 /tmp/goose_personality.py`
   - Environment Variables: (leave empty)
   - Timeout: 300

### Method 2: Local Repository

1. Clone the repository:
```bash
cd ~
git clone https://github.com/Sommer-tidal/goose-personality.git
```

2. In Goose, go to Settings → Extensions
3. Click "Add Custom Extension"
4. Fill in:
   - Type: Standard IO
   - ID: `personality-customizer`
   - Name: `Personality Customizer`
   - Description: `Customize Goose's personality and response style`
   - Command: `python3 ~/goose-personality/src/main.py`
   - Environment Variables: (leave empty)
   - Timeout: 300

## Available Commands

### 1. Get Available Styles
```
get_personality_styles
```
Lists all available personality styles (both built-in and custom).

### 2. Set a Style
```
set_style [style_name]
```
Changes Goose's personality to the specified style. For example:
```
set_style professional
```

### 3. Customize Personality
```
customize_personality
```
Opens a web interface where you can:
- Create new personality styles
- Add custom instructions
- View existing styles

## Built-in Styles

1. **friendly**
   - Warm, conversational tone
   - Occasional emojis
   - Simple explanations
   - Everyday examples

2. **professional**
   - Formal language
   - Precise and accurate
   - Structured with headers
   - Technical details included

3. **teacher**
   - Step-by-step explanations
   - Uses analogies
   - Interactive with checking questions
   - Lots of examples

4. **concise**
   - Brief and to-the-point
   - Bullet points
   - Key information only
   - Minimal examples

## Features

- **Style Persistence**: Your style preferences are saved using Goose's memory extension
- **Custom Styles**: Create and save your own personality styles
- **Web Interface**: Easy-to-use configuration interface for creating styles
- **Multiple Styles**: Switch between different styles as needed

## Creating Custom Styles

1. Run `customize_personality` to open the configuration interface
2. Enter a name for your new style
3. Add instructions that define the style
4. Click "Save Style"
5. Use `set_style [your-style-name]` to activate it

## Integration with Memory Extension

The extension automatically saves your style preferences using Goose's memory extension. This means your preferred style persists across conversations.

## Performance

This extension has minimal performance impact:
- Low memory usage (< 1MB for style storage)
- No background processes
- Configuration interface only runs when explicitly called
- Styles are loaded only when needed

## Contributing

Feel free to contribute by:
1. Creating and sharing custom styles
2. Suggesting improvements
3. Reporting issues
4. Submitting pull requests

## Troubleshooting

### Common Issues

1. **File Not Found Error**
   - Make sure you're using the exact command from Method 1 or Method 2
   - If using Method 2, verify that the repository was cloned to your home directory

2. **Permission Denied**
   - Try running `chmod +x /tmp/goose_personality.py` if you get permission errors

3. **Python Not Found**
   - Ensure Python 3 is installed on your system
   - Try using `python` instead of `python3` if your system uses that command

4. **Timeout Issues**
   - If you get timeout errors, try increasing the timeout value in the extension settings

If you continue to have issues, please:
1. Check that you can access the GitHub repository
2. Verify your internet connection (needed for Method 1)
3. Make sure Python 3 is installed and accessible from the command line

## License

MIT License - See LICENSE file for details