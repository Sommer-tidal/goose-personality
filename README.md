# Goose Personality Extension

A customizable extension for modifying Goose's personality and response style. This extension allows you to switch between predefined styles or create your own custom personality styles through a web interface.

## Installation

There are three ways to install this extension:

### Method 1: Direct Installation (Recommended)

1. Open Goose
2. Go to Settings → Extensions
3. Click "Add Custom Extension"
4. Fill in:
   - Type: Standard IO
   - ID: `personality-customizer`
   - Name: `Personality Customizer`
   - Description: `Customize Goose's personality and response style`
   - Command: `/bin/bash`
   - Arguments: `-c "wget -qO- https://raw.githubusercontent.com/Sommer-tidal/goose-personality/main/src/main.py | python3"`
   - Environment Variables: (leave empty)
   - Timeout: 300

### Method 2: Alternative Direct Installation

If Method 1 doesn't work, try these settings:
   - Type: Standard IO
   - ID: `personality-customizer`
   - Name: `Personality Customizer`
   - Description: `Customize Goose's personality and response style`
   - Command: `sh`
   - Arguments: `-c curl -s https://raw.githubusercontent.com/Sommer-tidal/goose-personality/main/src/main.py > /tmp/goose_personality.py && python3 /tmp/goose_personality.py`
   - Environment Variables: (leave empty)
   - Timeout: 300

### Method 3: Local Repository

If the above methods don't work, you can install locally:

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

[Rest of README remains the same...]