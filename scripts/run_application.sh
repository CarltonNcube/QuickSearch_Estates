#!/bin/bash

# Define absolute paths
ROOT_DIR="/QuickSearch_Estates"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"

# Install backend dependencies
echo "Step 1: Installing backend dependencies..."
cd $BACKEND_DIR
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start the backend server
echo "Step 2: Starting the backend server..."
nohup python3 app.py &

# Start the Express.js server
echo "Step 3: Starting the Express.js server..."
cd $ROOT_DIR
node $BACKEND_DIR/app.js &

# Install frontend dependencies and build
echo "Step 4: Installing frontend dependencies and building..."
cd $FRONTEND_DIR
npm install
npm run build

# Start the frontend server
echo "Step 5: Starting the frontend server..."
npm start

# Restart nginx, quicksearch-estates, and gunicorn
echo "Step 6: Restarting nginx, quicksearch-estates, and gunicorn..."
sudo systemctl restart nginx
sudo systemctl restart quicksearch-estates
sudo systemctl restart gunicorn
sudo systemctl status nginx
sudo systemctl status quicksearch-estates

