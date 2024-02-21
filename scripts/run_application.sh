#!/bin/bash

# Clone the GitHub repository
echo "Step 1: Cloning the GitHub repository..."
git clone https://github.com/CarltonNcube/QuickSearch_Estates.git
cd QuickSearch_Estates

# Install backend dependencies
echo "Step 2: Installing backend dependencies..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start the backend server
echo "Step 3: Starting the backend server..."
nohup python3 app.py &

# Install frontend dependencies and build
echo "Step 4: Installing frontend dependencies and building..."
cd ../frontend
npm install
npm run build

# Start the frontend server
echo "Step 5: Starting the frontend server..."
npm start

