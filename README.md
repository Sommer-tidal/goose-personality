# Goose Personality Extension

A simple extension for customizing Goose's personality and response style.

## Installation

1. First, clone the repository:
```bash
cd ~
git clone https://github.com/Sommer-tidal/goose-personality.git
```

2. In Goose:
   - Go to Settings → Extensions
   - Click "Add Custom Extension"
   - Fill in:
     - Type: Standard IO
     - ID: `personality-customizer`
     - Name: `Personality Customizer`
     - Description: `Customize Goose's personality and response style`
     - Command: `/Library/Developer/CommandLineTools/usr/bin/python3`
     - Arguments: `/Users/YOURUSERNAME/goose-personality/src/main.py`
     - Environment Variables: (leave empty)
     - Timeout: 30

   **Important**: Replace `YOURUSERNAME` with your actual username.
   For example, if your username is "john", the Arguments field would be:
   `/Users/john/goose-personality/src/main.py`

## Available Commands

### 1. Get Available Styles
```
get_personality_styles
```
Lists all available personality styles.

### 2. Set a Style
```
set_style [style_name]
```
Changes Goose's personality to the specified style. For example:
```
set_style professional
```

## Built-in Styles

Currently supports four basic styles:
1. **friendly** - Casual and warm communication
2. **professional** - Formal and precise communication
3. **teacher** - Educational and explanatory approach
4. **concise** - Brief and to-the-point responses

## Troubleshooting

### Common Installation Issues

1. **Wrong Username**
   - Make sure to replace YOURUSERNAME with your actual username
   - Run `echo $USER` in terminal to find your username
   - The path must match where you cloned the repository

2. **File Not Found**
   - Make sure you cloned the repository to your home directory
   - Verify the file exists: `ls -l ~/goose-personality/src/main.py`
   - If the file is missing, clone the repository again

3. **Python Issues**
   - The command path should work on most Macs
   - If it doesn't, try finding your Python path: `which python3`
   - Use that path in the Command field instead

4. **Permission Issues**
   - Check file permissions: `ls -l ~/goose-personality/src/main.py`
   - Should show read permissions (r) for your user
   - Try running: `chmod +r ~/goose-personality/src/main.py`

## Current Status

This is a simplified version of the extension focusing on basic functionality. Future updates will add:
- Custom style creation
- Web interface for configuration
- Style persistence
- More detailed personality customization

## Contributing

Feel free to contribute by:
1. Testing and reporting issues
2. Suggesting improvements
3. Submitting pull requests

## License

MIT License - See LICENSE file for details