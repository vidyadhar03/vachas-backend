# Vachas Backend

A FastAPI backend application for real-time audio streaming with WebSocket support, designed for integration with Exotel telephony and Pipecat AI pipeline.

## 🚀 Features

- ✅ **FastAPI Framework** - Modern, fast web framework for building APIs
- ✅ **WebSocket Support** - Real-time audio streaming via WebSocket connections
- ✅ **Audio Echo Testing** - Built-in audio echo functionality for testing
- ✅ **Connection Management** - Track and manage multiple WebSocket connections
- ✅ **Structured Logging** - Comprehensive logging for debugging and monitoring
- ✅ **Interactive Testing** - Built-in HTML test page for WebSocket testing
- ✅ **API Documentation** - Auto-generated Swagger UI and ReDoc documentation
- 🔄 **Exotel Integration** - (Planned for Step 3)
- 🔄 **Pipecat AI Pipeline** - (Planned for Step 4)

## 📁 Project Structure

```
vachas-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application with WebSocket endpoint
│   ├── routes/
│   │   ├── __init__.py
│   │   └── audio.py         # WebSocket audio streaming logic
│   ├── services/
│   │   ├── __init__.py
│   │   └── exotel.py        # Exotel integration service (placeholder)
│   └── utils/
│       ├── __init__.py
│       └── logging.py       # Logging configuration
├── venv/                    # Python virtual environment
├── test_websocket.py        # WebSocket testing script
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Git

### 1. Clone & Navigate
```bash
cd D:\Projects\vachas-backend
```

### 2. Create & Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Server
```bash
uvicorn app.main:app --reload
```

## 🌐 API Endpoints

### HTTP Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint with API info |
| GET | `/health` | Health check endpoint |
| GET | `/test` | Interactive WebSocket test page |
| GET | `/docs` | Swagger UI documentation |
| GET | `/redoc` | ReDoc documentation |

### WebSocket Endpoints

| Type | Endpoint | Description |
|------|----------|-------------|
| WebSocket | `/ws/audio` | Real-time audio streaming endpoint |

## 🧪 Testing

### 1. Basic HTTP Testing
```bash
# Test root endpoint
curl http://localhost:8000/

# Test health endpoint
curl http://localhost:8000/health
```

### 2. WebSocket Testing

#### Option A: Browser Test (Recommended)
1. Open: `http://localhost:8000/test`
2. Click "Test Audio WebSocket" button
3. Check the connection logs on the page

#### Option B: Python Test Script
```bash
python test_websocket.py
```

#### Option C: Manual Python Test
```python
import asyncio
import websockets

async def test():
    async with websockets.connect('ws://localhost:8000/ws/audio') as ws:
        await ws.send(b'test_audio_data')
        response = await ws.recv()
        print(f'Received: {len(response)} bytes')

asyncio.run(test())
```

### 3. API Documentation
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📝 Usage Examples

### WebSocket Audio Streaming

```python
import asyncio
import websockets

async def audio_client():
    uri = "ws://localhost:8000/ws/audio"
    async with websockets.connect(uri) as websocket:
        # Send audio data
        audio_data = b"your_audio_bytes_here"
        await websocket.send(audio_data)
        
        # Receive processed audio
        response = await websocket.recv()
        print(f"Received {len(response)} bytes")

asyncio.run(audio_client())
```

### HTTP API Usage

```python
import requests

# Get API info
response = requests.get("http://localhost:8000/")
print(response.json())

# Check health
health = requests.get("http://localhost:8000/health")
print(health.json())
```

## 🔧 Development

### Project Structure Explained

- **`app/main.py`** - Main FastAPI application with all endpoints
- **`app/routes/audio.py`** - WebSocket connection handling and audio processing
- **`app/services/exotel.py`** - Placeholder for Exotel telephony integration
- **`app/utils/logging.py`** - Centralized logging configuration

### Key Features

1. **Connection Management**: Tracks active WebSocket connections
2. **Audio Echo**: Currently echoes received audio data back (for testing)
3. **Error Handling**: Graceful WebSocket disconnection handling
4. **Logging**: Comprehensive logging for all operations
5. **Shutdown Handling**: Graceful shutdown with connection cleanup

## 📋 Current Status

### ✅ Completed (Step 2)
- [x] FastAPI application setup
- [x] WebSocket endpoint for audio streaming
- [x] Connection management
- [x] Audio echo functionality
- [x] Structured project organization
- [x] Comprehensive logging
- [x] Interactive testing interface
- [x] API documentation

### 🔄 Next Steps

#### Step 3: Exotel Integration
- [ ] Configure Exotel API credentials
- [ ] Implement incoming call handling
- [ ] Set up audio forwarding from Exotel to WebSocket
- [ ] Add call management features

#### Step 4: Pipecat AI Pipeline
- [ ] Integrate Pipecat for AI-powered audio processing
- [ ] Add speech-to-text capabilities
- [ ] Implement text-to-speech responses
- [ ] Add conversation context management

#### Step 5: Advanced Features
- [ ] Call recording and storage
- [ ] Real-time transcription
- [ ] Multi-language support
- [ ] Performance monitoring

## 🔍 Troubleshooting

### Common Issues

1. **WebSocket Connection Refused**
   - Ensure FastAPI server is running on port 8000
   - Check virtual environment is activated
   - Verify no firewall blocking the connection

2. **Import Errors**
   - Activate virtual environment: `venv\Scripts\activate`
   - Install dependencies: `pip install -r requirements.txt`

3. **Server Won't Start**
   - Check for port conflicts: `netstat -an | findstr :8000`
   - Verify Python path and virtual environment

## 📞 Support

For issues and questions:
1. Check the logs in the FastAPI server terminal
2. Test basic HTTP endpoints first
3. Use the built-in test page at `/test`
4. Check API documentation at `/docs`

---

**Server Status**: ✅ Ready for Development  
**WebSocket**: ✅ Functional  
**Next Step**: Exotel Integration (Step 3) 