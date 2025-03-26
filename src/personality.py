def set_my_style(style=None):
    """
    Change how Goose talks to you
    
    Args:
        style: The style you want (like 'friendly', 'professional', 'simple')
    """
    styles = {
        'friendly': {
            'tone': 'casual and warm',
            'format': 'conversational'
        },
        'professional': {
            'tone': 'formal and precise',
            'format': 'structured'
        },
        'simple': {
            'tone': 'clear and basic',
            'format': 'step-by-step'
        }
    }
    
    return {"style": style, "settings": styles.get(style, {})}
