from fastapi import WebSocket, WebSocketDisconnect
import logging

logger = logging.getLogger(__name__)

# Track active WebSocket connections
active_connections = set()

async def handle_audio_stream(websocket: WebSocket):
    """Handle WebSocket audio streaming with Exotel integration."""
    await websocket.accept()
    active_connections.add(websocket)
    logger.info(f"WebSocket connection established. Active connections: {len(active_connections)}")
    
    try:
        while True:
            # Receive audio bytes from Exotel (or test client)
            audio_data = await websocket.receive_bytes()
            logger.info(f"Received audio data: {len(audio_data)} bytes")
            
            # TODO: Add Pipecat pipeline integration here
            # For now, echo back the audio data for testing
            await websocket.send_bytes(audio_data)
            logger.info("Audio data echoed back to client")
            
    except WebSocketDisconnect:
        active_connections.discard(websocket)
        logger.info(f"WebSocket disconnected. Active connections: {len(active_connections)}")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        active_connections.discard(websocket)
        await websocket.close()

async def close_all_connections():
    """Close all active WebSocket connections gracefully."""
    logger.info(f"Closing {len(active_connections)} active connections")
    for connection in list(active_connections):
        try:
            await connection.close()
        except Exception as e:
            logger.error(f"Error closing connection: {e}")
    active_connections.clear() 