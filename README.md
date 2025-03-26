# Goose Personality Extension

A customizable extension for modifying Goose's personality and response style. This extension allows you to switch between predefined styles or create your own custom personality styles through a web interface.

## Installation

### Local Installation (Recommended)

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
     - Command: `python3`
     - Arguments: `-u ~/goose-personality/src/main.py`
     - Environment Variables: (leave empty)
     - Timeout: 300

Note: Replace `~` with your actual home directory path if needed (e.g., `/Users/yourusername`).

### Alternative Installation

If you prefer not to clone the repository, you can try this method:

1. In Goose, go to Settings → Extensions
2. Click "Add Custom Extension"
3. Fill in:
   - Type: Standard IO
   - ID: `personality-customizer`
   - Name: `Personality Customizer`
   - Description: `Customize Goose's personality and response style`
   - Command: `python3`
   - Arguments: `-c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/Sommer-tidal/goose-personality/main/src/main.py').read().decode())"`
   - Environment Variables: (leave empty)
   - Timeout: 300

## Troubleshooting

### Common Installation Issues

1. **Path Issues**
   - Make sure to replace `~` with your actual home directory path if needed
   - Example: `/Users/yourusername/goose-personality/src/main.py`
   - Use `echo $HOME` in terminal to find your home directory

2. **Python Issues**
   - Make sure Python 3 is installed: `python3 --version`
   - Try using full path: `/usr/bin/python3` instead of just `python3`

3. **Permission Issues**
   - Check file permissions: `ls -l ~/goose-personality/src/main.py`
   - Should show read permissions (r) for your user

4. **Repository Issues**
   - Verify the repository was cloned: `ls ~/goose-personality`
   - Try cloning again if files are missing

[Rest of README remains the same...]