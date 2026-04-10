# Setup Guide - Code Generation Model using LLM

## Quick Start Guide

This guide will help you set up and run the Code Generation Model project on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11 or higher**
  - Download from: https://www.python.org/downloads/
  - Verify: `python --version`

- **Node.js 16+ and Yarn**
  - Download Node.js from: https://nodejs.org/
  - Install Yarn: `npm install -g yarn`
  - Verify: `node --version` and `yarn --version`

- **MongoDB**
  - Download from: https://www.mongodb.com/try/download/community
  - Or use MongoDB Atlas (cloud): https://www.mongodb.com/cloud/atlas
  - Verify: `mongod --version`

- **API Key**
  - Emergent LLM Key (provided in project) OR
  - Your own OpenAI API Key from: https://platform.openai.com/api-keys

## Step-by-Step Installation

### 1. Clone/Download the Project

```bash
# If using Git
git clone <your-repository-url>
cd code-generation-llm

# Or extract the downloaded ZIP file
```

### 2. MongoDB Setup

**Option A: Local MongoDB**
```bash
# Start MongoDB service
mongod --dbpath /path/to/your/data/directory

# MongoDB will run on mongodb://localhost:27017
```

**Option B: MongoDB Atlas (Cloud)**
1. Create free account at https://www.mongodb.com/cloud/atlas
2. Create a cluster
3. Get connection string
4. Update `MONGO_URL` in backend/.env

### 3. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Configure Backend Environment

Create/edit `backend/.env` file:

```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=code_generation_db
CORS_ORIGINS=*
EMERGENT_LLM_KEY=sk-emergent-77999D08250Da31B9F
```

**Note**: Replace with your own API key if needed.

#### Start Backend Server

```bash
# Make sure you're in /backend directory
uvicorn server:app --host 0.0.0.0 --port 8001 --reload

# Server will start at http://localhost:8001
# API docs available at http://localhost:8001/docs
```

### 4. Frontend Setup

Open a **NEW terminal window**:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
yarn install
```

#### Configure Frontend Environment

Create/edit `frontend/.env` file:

```env
REACT_APP_BACKEND_URL=http://localhost:8001
WDS_SOCKET_PORT=443
ENABLE_HEALTH_CHECK=false
```

#### Start Frontend Server

```bash
# Make sure you're in /frontend directory
yarn start

# Application will open at http://localhost:3000
```

## Verification

### 1. Check Backend is Running

Open browser and visit:
- http://localhost:8001/api/ - Should show: `{"message": "Code Generation Model API"}`
- http://localhost:8001/docs - Should show API documentation

### 2. Check Frontend is Running

Open browser and visit:
- http://localhost:3000 - Should show the Code Generation Model interface

### 3. Test Code Generation

1. Select a programming language (e.g., Python)
2. Enter a prompt: "Create a function to add two numbers"
3. Click "Generate Code"
4. You should see generated code with syntax highlighting

## Troubleshooting

### Backend Issues

**Error: ModuleNotFoundError**
```bash
# Make sure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

**Error: MongoDB connection failed**
```bash
# Check if MongoDB is running
# On Windows: Check Services
# On macOS/Linux: ps aux | grep mongod

# Verify MONGO_URL in .env is correct
```

**Error: EMERGENT_LLM_KEY invalid**
- Check if key is correctly copied in .env
- No quotes around the key
- No extra spaces

### Frontend Issues

**Error: Cannot connect to backend**
- Verify backend is running on port 8001
- Check REACT_APP_BACKEND_URL in frontend/.env
- Check browser console for CORS errors

**Error: Module not found**
```bash
# Clear node_modules and reinstall
rm -rf node_modules yarn.lock
yarn install
```

**Port 3000 already in use**
```bash
# Kill process on port 3000
# On macOS/Linux:
lsof -ti:3000 | xargs kill -9
# On Windows:
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

## Production Deployment

### Backend Deployment

```bash
# Build for production
cd backend

# Using Gunicorn (recommended)
pip install gunicorn
gunicorn server:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001
```

### Frontend Deployment

```bash
# Build for production
cd frontend
yarn build

# Serve the build folder using any static server
# Example with serve:
npm install -g serve
serve -s build -l 3000
```

### Environment Variables for Production

**Backend (.env)**
```env
MONGO_URL=<your-production-mongodb-url>
DB_NAME=code_generation_prod
CORS_ORIGINS=https://yourdomain.com
EMERGENT_LLM_KEY=<your-api-key>
```

**Frontend (.env.production)**
```env
REACT_APP_BACKEND_URL=https://api.yourdomain.com
```

## Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v
```

### Frontend Tests
```bash
cd frontend
yarn test
```

## API Key Management

### Using Emergent LLM Key (Provided)
- Key is already configured in the project
- Works with OpenAI GPT-5.2, Claude, and Gemini
- Check your balance at: https://emergent.sh/profile

### Using Your Own OpenAI Key
1. Get API key from: https://platform.openai.com/api-keys
2. Replace `EMERGENT_LLM_KEY` in backend/.env
3. Modify code to use OpenAI SDK directly (if needed)

## Additional Resources

- **Project Documentation**: Available in the web interface
- **API Documentation**: http://localhost:8001/docs (when backend is running)
- **MongoDB Compass**: GUI tool for MongoDB - https://www.mongodb.com/products/compass
- **Postman**: API testing - https://www.postman.com/

## Next Steps

After successful setup:

1. **Explore Documentation**: Read all 10 academic sections in the left pane
2. **Test Code Generation**: Try different programming languages
3. **Check History**: View generated code history via API
4. **Customize**: Modify prompts, add new languages, enhance UI
5. **Learn**: Study the code to understand LLM integration

## Support

If you encounter issues:
1. Check this setup guide
2. Review error messages carefully
3. Verify all prerequisites are installed
4. Check environment variables
5. Consult the main README.md

## Quick Command Reference

```bash
# Backend
cd backend
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
uvicorn server:app --reload

# Frontend
cd frontend
yarn start

# MongoDB
mongod --dbpath /path/to/data

# Tests
pytest tests/              # Backend
yarn test                  # Frontend
```

Happy Coding! 🚀