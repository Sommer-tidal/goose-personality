# Goose Personality Extension

A simple extension for customizing Goose's personality and response style.

## Available Styles

- **Friendly**: Warm, conversational tone with occasional emojis
- **Professional**: Formal, precise, and technically detailed
- **Teacher**: Educational style with step-by-step explanations
- **Concise**: Brief and to-the-point responses

## Installation

1. Open Goose
2. Go to Settings → Extensions
3. Click "Add Custom Extension"
4. Fill in:
   - Type: Standard IO
   - ID: personality-customizer
   - Name: Personality Customizer
   - Description: Customize Goose's personality and response style
   - Command: python3 main.py

## Usage

The extension provides two commands:
- `get_styles`: Lists all available personality styles
- `set_style`: Changes to a specific style (friendly/professional/teacher/concise)
