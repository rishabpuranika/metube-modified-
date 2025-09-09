#!/bin/bash
set -e

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Installing Node.js dependencies..."
cd ui
npm install

echo "Building Angular application..."
node_modules/.bin/ng build

echo "Build completed successfully!"
cd ..
