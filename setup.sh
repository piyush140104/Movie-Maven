#!/bin/bash

# Exit on error
set -e

# Create a virtual environment (optional)
echo "Creating virtual environment..."
python -m venv venv
source venv/bin/activate

# Install necessary packages
echo "Installing dependencies..."
pip install -r requirements.txt

# Set environment variables (optional)
# Uncomment and modify the lines below as needed
# heroku config:set KEY=VALUE


