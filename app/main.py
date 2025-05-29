from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from app.routes.audio import handle_audio_stream, close_all_connections
from app.utils.logging import setup_logging
import uvicorn
import logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Vachas Backend",
    description="FastAPI backend for real-time audio streaming with Exotel and Pipecat integration",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Root endpoint returning basic info."""
    return {
        "message": "Vachas Backend API",
        "status": "running",
        "version": "1.0.0",
        "websocket_endpoint": "/ws/audio"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "vachas-backend"}

@app.websocket("/ws/audio")
async def websocket_audio_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time audio streaming."""
    await handle_audio_stream(websocket)

@app.get("/test", response_class=HTMLResponse)
async def test_websocket():
    """Simple HTML page to test WebSocket connection."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>WebSocket Audio Test</title>
    </head>
    <body>
        <h1>WebSocket Audio Test</h1>
        <button onclick="testWebSocket()">Test Audio WebSocket</button>
        <div id="status"></div>
        <div id="log"></div>
        
        <script>
            function testWebSocket() {
                const status = document.getElementById('status');
                const log = document.getElementById('log');
                
                status.innerHTML = 'Connecting...';
                
                const ws = new WebSocket('ws://localhost:8000/ws/audio');
                
                ws.onopen = function(event) {
                    status.innerHTML = 'Connected';
                    log.innerHTML += '<p>Connected to WebSocket</p>';
                    
                    // Send test audio data (dummy bytes)
                    const testData = new Uint8Array([1, 2, 3, 4, 5]);
                    ws.send(testData);
                    log.innerHTML += '<p>Sent test audio data</p>';
                };
                
                ws.onmessage = function(event) {
                    log.innerHTML += '<p>Received audio data: ' + event.data.size + ' bytes</p>';
                };
                
                ws.onerror = function(error) {
                    status.innerHTML = 'Error';
                    log.innerHTML += '<p>Error: ' + error + '</p>';
                };
                
                ws.onclose = function(event) {
                    status.innerHTML = 'Disconnected';
                    log.innerHTML += '<p>Connection closed</p>';
                };
            }
        </script>
    </body>
    </html>
    """

@app.on_event("shutdown")
async def shutdown_event():
    """Gracefully close all WebSocket connections on shutdown."""
    logger.info("Shutting down application...")
    await close_all_connections()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) 