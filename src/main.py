#!/usr/bin/env python3
import json
import sys
import os
import logging
from dataclasses import dataclass, asdict
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import threading
import socket
from typing import Dict, List, Optional

# Set up logging with more detail
logging.basicConfig(
    filename='/tmp/goose_personality.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log startup
logging.info("Starting personality customizer extension")

[... rest of the file remains the same ...]