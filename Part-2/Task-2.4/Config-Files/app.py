from flask import Flask, jsonify
import os
import socket
import redis
from datetime import datetime

app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    # Increment visit counter
    try:
        visits = redis_client.incr('visits')
    except redis.exceptions.ConnectionError:
        visits = "Cannot connect to Redis"

    return jsonify({
        "message": "Hello from DevOps Training!",
        "hostname": socket.gethostname(),
        "version": "2.0",
        "visits": visits,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    try:
        redis_client.ping()
        redis_status = "connected"
    except:
        redis_status = "disconnected"
    
    return jsonify({
        "status": "healthy",
        "redis": redis_status
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)