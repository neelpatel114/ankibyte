#!/bin/bash

# AnkiByte Startup Script

# Exit immediately if a command exits with a non-zero status
set -e

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

echo "Welcome to AnkiByte! This script will help you set up the development environment."

# Check for required tools
if ! command_exists python3; then
    echo "Python 3 is not installed. Please install it and run this script again."
    exit 1
fi

if ! command_exists node; then
    echo "Node.js is not installed. Please install it and run this script again."
    exit 1
fi

if ! command_exists npm; then
    echo "npm is not installed. Please install it and run this script again."
    exit 1
fi

if ! command_exists psql; then
    echo "PostgreSQL is not installed. Please install it and run this script again."
    exit 1
fi

# Set up backend
echo "Setting up the backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set up database
echo "Setting up the database..."
read -p "Enter your PostgreSQL username: " pg_username
read -s -p "Enter your PostgreSQL password: " pg_password
echo
psql -U $pg_username -c "CREATE DATABASE visionbyte;"
psql -U $pg_username -c "CREATE USER visionbyte WITH PASSWORD 'your_db_password_here';"
psql -U $pg_username -c "ALTER ROLE visionbyte SET client_encoding TO 'utf8';"
psql -U $pg_username -c "ALTER ROLE visionbyte SET default_transaction_isolation TO 'read committed';"
psql -U $pg_username -c "ALTER ROLE visionbyte SET timezone TO 'UTC';"
psql -U $pg_username -c "GRANT ALL PRIVILEGES ON DATABASE visionbyte TO visionbyte;"

# Set up environment variables
echo "Setting up environment variables..."
cp .env.example .env
echo "Please update the .env file with your specific configurations."

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Set up frontend
echo "Setting up the frontend..."
cd ../frontend
npm install

echo "Setup complete! To start the development servers:"
echo "1. For the backend: cd backend && source venv/bin/activate && python manage.py runserver"
echo "2. For the frontend: cd frontend && npm start"
echo "3. Make sure to start your PostgreSQL server and Redis server if you're using Celery."
echo "Happy coding!"