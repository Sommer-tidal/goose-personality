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
   - Command: `python3 -c "import urllib.request; urllib.request.urlretrieve('https://raw.githubusercontent.com/Sommer-tidal/goose-personality/main/src/main.py', '/tmp/main.py'); __import__('sys').exit(__import__('os').system('python3 /tmp/main.py'))"`
   - Environment Variables: (leave empty)
   - Timeout: 30

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
   - Timeout: 30

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

If you get an error about not finding the main.py file, make sure you're using one of the installation methods above. The command needs to either:
1. Download the script directly from GitHub (Method 1)
2. Point to the correct path after cloning the repository (Method 2)

## License

MIT License - See LICENSE file for details