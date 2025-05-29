#!/usr/bin/env python3
"""
Test script for WebSocket audio endpoint.
Run this after starting the FastAPI server to test audio streaming.
"""
import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_websocket_audio():
    """Test the WebSocket audio endpoint with dummy audio data."""
    uri = "ws://localhost:8000/ws/audio"
    
    try:
        async with websockets.connect(uri) as websocket:
            logger.info("Connected to WebSocket audio endpoint")
            
            # Send dummy audio data
            test_audio_data = b"dummy_audio_data_12345"
            await websocket.send(test_audio_data)
            logger.info(f"Sent audio data: {len(test_audio_data)} bytes")
            
            # Receive echoed data
            response = await websocket.recv()
            logger.info(f"Received response: {len(response)} bytes")
            
            # Verify echo
            if response == test_audio_data:
                logger.info("✅ Audio echo test PASSED!")
            else:
                logger.error("❌ Audio echo test FAILED!")
            
            # Send multiple chunks to test streaming
            for i in range(3):
                chunk = f"audio_chunk_{i}".encode()
                await websocket.send(chunk)
                response = await websocket.recv()
                logger.info(f"Chunk {i}: Sent {len(chunk)} bytes, received {len(response)} bytes")
            
            logger.info("✅ WebSocket audio streaming test completed!")
            
    except Exception as e:
        logger.error(f"❌ WebSocket test failed: {e}")

if __name__ == "__main__":
    print("Testing WebSocket audio endpoint...")
    print("Make sure the FastAPI server is running on http://localhost:8000")
    print("-" * 50)
    asyncio.run(test_websocket_audio()) 