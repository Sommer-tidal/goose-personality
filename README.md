# Goose Personality Extension

A customizable extension for modifying Goose's personality and response style. This extension allows you to switch between predefined styles or create your own custom personality styles through a web interface.

## Installation

1. First, clone the repository:
```bash
cd ~
git clone https://github.com/Sommer-tidal/goose-personality.git
```

2. Find your Python path:
```bash
which python3
```
Note: It's typically `/Library/Developer/CommandLineTools/usr/bin/python3` on macOS

3. In Goose:
   - Go to Settings → Extensions
   - Click "Add Custom Extension"
   - Fill in EXACTLY as shown (adjust paths if needed):
     - Type: Standard IO
     - ID: `personality-customizer`
     - Name: `Personality Customizer`
     - Description: `Customize Goose's personality and response style`
     - Command: `/Library/Developer/CommandLineTools/usr/bin/python3`
     - Arguments: `/Users/YOUR_USERNAME/goose-personality/src/main.py`
     - Environment Variables: (leave empty)
     - Timeout: 300

   Replace `YOUR_USERNAME` with your actual username.

## Troubleshooting

### Common Installation Issues

1. **Wrong Python Path**
   - Run `which python3` in terminal to find your Python path
   - Use that full path in the Command field

2. **Wrong Script Path**
   - Make sure to replace YOUR_USERNAME with your actual username
   - Verify the file exists: `ls -l ~/goose-personality/src/main.py`
   - Use `echo $HOME` to find your home directory

3. **Repository Issues**
   - If files are missing, clone again:
     ```bash
     cd ~
     rm -rf goose-personality
     git clone https://github.com/Sommer-tidal/goose-personality.git
     ```

4. **Permission Issues**
   - Check file permissions: `ls -l ~/goose-personality/src/main.py`
   - Should show read permissions (r) for your user

[Rest of README remains the same...]