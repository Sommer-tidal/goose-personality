# Goose Personality Extension

A customizable extension for modifying Goose's personality and response style. This extension allows you to switch between predefined styles or create your own custom personality styles through a web interface.

## Installation

There are two ways to install this extension:

### Method 1: Direct Installation (Recommended)

1. Open Goose
2. Go to Settings → Extensions
3. Click "Add Custom Extension"
4. Fill in these fields EXACTLY as shown (copy and paste recommended):
   - Type: Standard IO
   - ID: `personality-customizer`
   - Name: `Personality Customizer`
   - Description: `Customize Goose's personality and response style`
   - Command: `python3`
   - Arguments: `-c import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/Sommer-tidal/goose-personality/main/src/main.py').read().decode())`
   - Environment Variables: (leave empty)
   - Timeout: 300

IMPORTANT: Do not add any extra quotes around the Arguments field. Copy and paste it exactly as shown above.

### Method 2: Local Repository

If the direct installation doesn't work, you can install locally:

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
   - Command: `python3`
   - Arguments: `~/goose-personality/src/main.py`
   - Environment Variables: (leave empty)
   - Timeout: 300

## Troubleshooting

### Common Installation Issues

1. **Syntax Error or Quote Issues**
   - Make sure you copy the Arguments field exactly as shown
   - Do not add any extra quotes
   - Do not modify the command string

2. **Python Not Found**
   - Ensure Python 3 is installed on your system
   - Try using the full path: `/usr/bin/python3` in the Command field

3. **Connection Issues**
   - Verify you can access GitHub
   - Check your internet connection
   - Make sure you can access raw.githubusercontent.com

4. **Permission Issues**
   - Try Method 2 (Local Repository) if you have permission issues
   - Make sure Python has network access

[Rest of README remains the same...]