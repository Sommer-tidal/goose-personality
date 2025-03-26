# Goose Personality Extension

A customizable extension for modifying Goose's personality and response style. This extension allows you to switch between predefined styles or create your own custom personality styles through a web interface.

## Installation

1. First, clone the repository:
```bash
cd ~
git clone https://github.com/Sommer-tidal/goose-personality.git
```

2. Find your username:
```bash
echo $USER
```
This will show your username (you'll need it in step 3)

3. In Goose:
   - Go to Settings → Extensions
   - Click "Add Custom Extension"
   - Fill in these fields (replace USERNAME with your actual username from step 2):
     - Type: Standard IO
     - ID: `personality-customizer`
     - Name: `Personality Customizer`
     - Description: `Customize Goose's personality and response style`
     - Command: `/Library/Developer/CommandLineTools/usr/bin/python3`
     - Arguments: `/Users/USERNAME/goose-personality/src/main.py`
     - Environment Variables: (leave empty)
     - Timeout: 300

   For example, if your username is "john", the Arguments field would be:
   `/Users/john/goose-personality/src/main.py`

## Troubleshooting

### Common Installation Issues

1. **Wrong Username**
   - The most common error is not replacing USERNAME with your actual username
   - Run `echo $USER` in terminal to find your correct username
   - The path must exactly match where you cloned the repository

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

[Rest of README remains the same...]