# DevOps Assessment - Complete Infrastructure Setup Guide

[![Linux](https://img.shields.io/badge/Linux-Server-blue)](https://www.linux.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-blue)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue)](https://kubernetes.io/)
[![Flask](https://img.shields.io/badge/Flask-Python-green)](https://flask.palletsprojects.com/)

**Author:** Shachiru  
**Repository:** devops-assessment  
**Server IP:** 172.104.178.72

---

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Part 1: Linux Server Administration](#part-1-linux-server-administration)
  - [Task 1.1: Server Setup & User Management](#task-11-server-setup--user-management)
  - [Task 1.2: Package Installation & Configuration](#task-12-package-installation--configuration)
  - [Task 1.3: Web Application Deployment](#task-13-web-application-deployment)
  - [Task 1.4: System Monitoring](#task-14-system-monitoring)
- [Part 2: Docker Containerization](#part-2-docker-containerization)
  - [Task 2.1: Docker Installation](#task-21-docker-installation)
  - [Task 2.2: Dockerfile Creation](#task-22-dockerfile-creation)
  - [Task 2.3: Container Testing](#task-23-container-testing)
  - [Task 2.4: Docker Compose Multi-Container Setup](#task-24-docker-compose-multi-container-setup)
- [Part 3: Kubernetes Orchestration](#part-3-kubernetes-orchestration)
  - [Task 3.1: Minikube Setup](#task-31-minikube-setup)
  - [Task 3.2: Kubernetes Deployment](#task-32-kubernetes-deployment)
  - [Task 3.3: Service Verification](#task-33-service-verification)
- [Part 4: CI/CD Pipeline](#part-4-cicd-pipeline)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)
- [References](#references)

---

## 🎯 Overview

This repository contains a comprehensive DevOps assessment demonstrating proficiency in:

- **Linux System Administration** - User management, service configuration, and system monitoring
- **Web Application Deployment** - Flask application with Gunicorn and Nginx reverse proxy
- **Containerization** - Docker and Docker Compose for multi-container applications
- **Container Orchestration** - Kubernetes deployments with Minikube
- **Monitoring & Automation** - System health monitoring with automated scripts

The project showcases a complete infrastructure pipeline from bare-metal server setup to containerized microservices orchestration.

---

## 📁 Project Structure

```
devops-assessment/
├── README.md
├── AI_USAGE.txt
│
├── Part-1/                          # Linux Server Administration
│   ├── Task-1.1/                    # Server Setup & User Management
│   │   ├── Config-Files/
│   │   ├── Other-Details/
│   │   └── Verifications/
│   ├── Task-1.2/                    # Package Installation
│   │   ├── Config-Files/
│   │   └── Verifications/
│   ├── Task-1.3/                    # Web Application Deployment
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── Config-Files/
│   │   │   ├── nginx-config
│   │   │   └── webapp.service
│   │   └── Verifications/
│   └── Task-1.4/                    # System Monitoring
│       ├── Config-Files/
│       │   └── monitor.sh
│       └── Verifications/
│
├── Part-2/                          # Docker Containerization
│   ├── Task-2.1/                    # Docker Installation
│   │   ├── Config-Files/
│   │   │   └── install_notes.txt
│   │   ├── Other-Details/
│   │   └── Verifications/
│   ├── Task-2.2/                    # Dockerfile Creation
│   │   ├── Config-Files/
│   │   │   └── Dockerfile
│   │   └── Verifications/
│   ├── Task-2.3/                    # Container Testing
│   │   └── Verifications/
│   └── Task-2.4/                    # Docker Compose Setup
│       ├── Config-Files/
│       │   ├── app.py
│       │   ├── docker-compose.yaml
│       │   └── requirements.txt
│       └── Verifications/
│
├── Part-3/                          # Kubernetes Orchestration
│   ├── Task-3.1/                    # Minikube Setup
│   │   ├── Config-Files/
│   │   └── Verifications/
│   ├── Task-3.2/                    # Kubernetes Deployment
│   │   ├── Config-Files/
│   │   │   ├── redis-deployment.yaml
│   │   │   ├── redis-service.yaml
│   │   │   ├── webapp-deployment.yaml
│   │   │   └── webapp-service.yaml
│   │   └── Verifications/
│   └── Task-3.3/                    # Service Verification
│
└── Part-4/                          # CI/CD Pipeline
    └── Task-4.1/
        ├── Config-Files/
        ├── Other-Details/
        └── Verifications/
```

---

## 🔧 Prerequisites

### Server Requirements

- **OS:** Ubuntu 20.04+ / Debian 11+
- **RAM:** Minimum 4GB (8GB recommended for Kubernetes)
- **CPU:** 2+ cores
- **Storage:** 20GB+ available
- **Network:** Public IP with SSH access

### Local Machine Requirements

- SSH client
- Web browser for verification
- Basic knowledge of Linux, Docker, and Kubernetes

---

## 🐧 Part 1: Linux Server Administration

### Task 1.1: Server Setup & User Management

**Objective:** Initial server configuration with secure user setup

#### Steps Performed:

1. **SSH Access Configuration**

   ```bash
   ssh root@172.104.178.72
   ```

2. **User Creation**

   ```bash
   # Create webapp user
   useradd -m -s /bin/bash webapp

   # Set password
   passwd webapp

   # Grant sudo privileges
   usermod -aG sudo webapp
   ```

3. **Directory Structure Setup**

   ```bash
   mkdir -p /opt/webapp/{app,logs,venv}
   chown -R webapp:webapp /opt/webapp
   chmod 755 /opt/webapp
   ```

4. **Security Configuration**
   ```bash
   # Configure firewall
   ufw allow OpenSSH
   ufw allow 80/tcp
   ufw allow 5000/tcp
   ufw enable
   ```

#### Verification:

- User `webapp` created successfully
- Directory permissions set correctly
- Firewall rules active

---

### Task 1.2: Package Installation & Configuration

**Objective:** Install and configure required system packages

#### Packages Installed:

```bash
# Update system
apt update && apt upgrade -y

# Install essential packages
apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    nginx \
    curl \
    git \
    vim \
    htop \
    net-tools
```

#### Python Environment Setup:

```bash
# Create virtual environment
cd /opt/webapp
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip
```

#### Verification:

- All packages installed successfully
- Python virtual environment operational
- Nginx service running

---

### Task 1.3: Web Application Deployment

**Objective:** Deploy Flask web application with Gunicorn and Nginx

#### Application Details:

**File:** `Part-1/Task-1.3/app.py`

```python
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from DevOps Training!",
        "hostname": socket.gethostname(),
        "version": "1.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

#### Dependencies (`requirements.txt`):

```
blinker==1.9.0
click==8.3.1
Flask==3.1.2
gunicorn==23.0.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
packaging==25.0
Werkzeug==3.1.3
```

#### Deployment Steps:

1. **Install Dependencies**

   ```bash
   cd /opt/webapp
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure Systemd Service**

   **File:** `Part-1/Task-1.3/Config-Files/webapp.service`

   ```ini
   [Unit]
   Description=Gunicorn instance to serve webapp
   After=network.target

   [Service]
   User=webapp
   Group=webapp
   WorkingDirectory=/opt/webapp/app
   Environment="PATH=/opt/webapp/venv/bin"
   ExecStart=/opt/webapp/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 app:app --access-logfile /opt/webapp/logs/access.log --error-logfile /opt/webapp/logs/error.log
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

   ```bash
   # Copy service file
   cp webapp.service /etc/systemd/system/

   # Reload systemd
   systemctl daemon-reload

   # Start and enable service
   systemctl start webapp
   systemctl enable webapp
   ```

3. **Configure Nginx Reverse Proxy**

   **File:** `Part-1/Task-1.3/Config-Files/nginx-config`

   ```nginx
   server {
       listen 80;
       server_name _;

       location / {
           proxy_pass http://127.0.0.1:5000;
           include proxy_params;
       }
   }
   ```

   ```bash
   # Copy nginx configuration
   cp nginx-config /etc/nginx/sites-available/webapp

   # Create symbolic link
   ln -s /etc/nginx/sites-available/webapp /etc/nginx/sites-enabled/

   # Remove default site
   rm /etc/nginx/sites-enabled/default

   # Test configuration
   nginx -t

   # Restart nginx
   systemctl restart nginx
   ```

#### Access the Application:

```
http://172.104.178.72
```

**Expected Response:**

```json
{
  "message": "Hello from DevOps Training!",
  "hostname": "localhost",
  "version": "1.0"
}
```

#### Verification:

- Application accessible via HTTP
- Gunicorn service running with 3 workers
- Nginx reverse proxy functional
- Logs generated in `/opt/webapp/logs/`

---

### Task 1.4: System Monitoring

**Objective:** Implement automated system health monitoring

#### Monitoring Script:

**File:** `Part-1/Task-1.4/Config-Files/monitor.sh`

```bash
#!/bin/bash
LOG_FILE="/opt/webapp/logs/monitor.log"
echo "=== Monitoring Report: $(date) ===" >> $LOG_FILE
echo "Memory Usage:" >> $LOG_FILE
free -h >> $LOG_FILE
echo "Disk Usage /opt/webapp:" >> $LOG_FILE
du -sh /opt/webapp/ >> $LOG_FILE
echo "App Status:" >> $LOG_FILE
systemctl is-active webapp >> $LOG_FILE
echo "Nginx Status:" >> $LOG_FILE
systemctl is-active nginx >> $LOG_FILE
echo "---------------------------------" >> $LOG_FILE
```

#### Implementation:

```bash
# Make script executable
chmod +x /opt/webapp/monitor.sh

# Add to crontab (runs every 5 minutes)
crontab -e
```

**Cron Entry:**

```
*/5 * * * * /opt/webapp/monitor.sh
```

#### Monitored Metrics:

- **Memory Usage** - RAM utilization
- **Disk Usage** - Storage consumption for `/opt/webapp/`
- **Application Status** - Webapp service health
- **Nginx Status** - Web server availability

#### Log Location:

```
/opt/webapp/logs/monitor.log
```

#### Verification:

- Script executes successfully
- Logs updated every 5 minutes
- All system metrics captured
- Services status tracked

---

## 🐳 Part 2: Docker Containerization

### Task 2.1: Docker Installation

**Objective:** Install Docker and Docker Compose

**File:** `Part-2/Task-2.1/Config-Files/install_notes.txt`

```bash
# Update and install Docker
apt update
apt install -y docker.io
```

#### Complete Installation:

```bash
# Install Docker
apt update
apt install -y docker.io

# Start and enable Docker service
systemctl start docker
systemctl enable docker

# Install Docker Compose
apt install -y docker-compose

# Add user to docker group (optional)
usermod -aG docker webapp

# Verify installation
docker --version
docker-compose --version
```

#### Verification:

```bash
docker run hello-world
```

---

### Task 2.2: Dockerfile Creation

**Objective:** Containerize Flask application

**File:** `Part-2/Task-2.2/Config-Files/Dockerfile`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd -m appuser
USER appuser
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:5000/health || exit 1
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

#### Key Features:

- **Base Image:** `python:3.11-slim` (lightweight)
- **Security:** Non-root user (`appuser`)
- **Health Check:** Automated container health monitoring
- **Optimization:** No-cache pip installation for smaller image size
- **Production Ready:** Uses Gunicorn WSGI server

#### Build Image:

```bash
cd /opt/webapp
docker build -t webapp:v1 .
```

#### Verification:

```bash
docker images | grep webapp
```

---

### Task 2.3: Container Testing

**Objective:** Test containerized application

#### Run Container:

```bash
docker run -d \
  --name webapp-test \
  -p 5000:5000 \
  webapp:v1
```

#### Test Endpoints:

```bash
# Test home endpoint
curl http://localhost:5000

# Test health endpoint
curl http://localhost:5000/health
```

#### Container Management:

```bash
# View running containers
docker ps

# Check logs
docker logs webapp-test

# Stop container
docker stop webapp-test

# Remove container
docker rm webapp-test
```

---

### Task 2.4: Docker Compose Multi-Container Setup

**Objective:** Deploy application with Redis cache using Docker Compose

#### Application with Redis Integration:

**File:** `Part-2/Task-2.4/Config-Files/app.py`

```python
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
```

#### Docker Compose Configuration:

**File:** `Part-2/Task-2.4/Config-Files/docker-compose.yaml`

```yaml
version: "3.8"
services:
  webapp:
    build: .
    ports:
      - "5000:5000"
    environment:
      - REDIS_HOST=redis
    depends_on:
      - redis
    restart: always
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    networks:
      - app-network

networks:
  app-network:

volumes:
  redis-data:
```

#### Updated Dependencies:

**File:** `Part-2/Task-2.4/Config-Files/requirements.txt`

```
Flask==3.1.0
gunicorn==23.0.0
redis
```

#### Deploy Multi-Container Application:

```bash
cd /opt/webapp
docker-compose up -d --build
```

#### Verification:

```bash
# Check running containers
docker-compose ps

# View logs
docker-compose logs -f

# Test application
curl http://localhost:5000
```

**Expected Response:**

```json
{
  "message": "Hello from DevOps Training!",
  "hostname": "abc123def456",
  "version": "2.0",
  "visits": 1,
  "timestamp": "2025-11-21T10:30:45.123456"
}
```

#### Troubleshooting:

If you encounter `ContainerConfig` error:

```bash
# Stop and remove containers
docker-compose down -v --remove-orphans

# Remove corrupted containers
docker container prune -f

# Rebuild from scratch
docker-compose up -d --build
```

---

## ☸️ Part 3: Kubernetes Orchestration

### Task 3.1: Minikube Setup

**Objective:** Install and configure local Kubernetes cluster

#### Installation:

```bash
# Install required dependencies
apt install -y conntrack socat

# Download Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install minikube-linux-amd64 /usr/local/bin/minikube

# Start Minikube
minikube start --driver=docker --force

# Verify installation
kubectl version --client
kubectl cluster-info
```

#### Verification:

```bash
kubectl get nodes
```

---

### Task 3.2: Kubernetes Deployment

**Objective:** Deploy multi-tier application on Kubernetes

#### Architecture:

- **Frontend:** Flask webapp (2 replicas)
- **Backend:** Redis cache (1 replica)
- **Networking:** ClusterIP services for internal communication

#### Redis Deployment:

**File:** `Part-3/Task-3.2/Config-Files/redis-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
        - name: redis
          image: redis:7-alpine
          ports:
            - containerPort: 6379
          volumeMounts:
            - name: redis-data
              mountPath: /data
      volumes:
        - name: redis-data
          emptyDir: {}
```

**File:** `Part-3/Task-3.2/Config-Files/redis-service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: redis-service
spec:
  type: ClusterIP
  selector:
    app: redis
  ports:
    - port: 6379
      targetPort: 6379
```

#### Webapp Deployment:

**File:** `Part-3/Task-3.2/Config-Files/webapp-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
        - name: webapp
          image: webapp:v1
          imagePullPolicy: Never # Important: use local image
          ports:
            - containerPort: 5000
          env:
            - name: REDIS_HOST
              value: "redis-service"
          resources:
            requests:
              memory: "128Mi"
              cpu: "100m"
            limits:
              memory: "256Mi"
              cpu: "250m"
          livenessProbe:
            httpGet:
              path: /health
              port: 5000
          readinessProbe:
            httpGet:
              path: /health
              port: 5000
```

**File:** `Part-3/Task-3.2/Config-Files/webapp-service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: webapp-service
spec:
  type: ClusterIP
  selector:
    app: webapp
  ports:
    - port: 5000
      targetPort: 5000
```

#### Deployment Steps:

```bash
# Load Docker image into Minikube
minikube image load webapp:v1

# Deploy Redis
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml

# Deploy Webapp
kubectl apply -f webapp-deployment.yaml
kubectl apply -f webapp-service.yaml
```

#### Verification:

```bash
# Check deployments
kubectl get deployments

# Check pods
kubectl get pods

# Check services
kubectl get services

# Describe resources
kubectl describe deployment webapp
kubectl describe pod <pod-name>
```

---

### Task 3.3: Service Verification

**Objective:** Verify Kubernetes deployment and accessibility

#### Port Forwarding:

```bash
# Forward webapp service to local port
kubectl port-forward service/webapp-service 8080:5000
```

#### Test Application:

```bash
# Test from another terminal
curl http://localhost:8080
curl http://localhost:8080/health
```

#### Pod Logs:

```bash
# View logs from specific pod
kubectl logs <pod-name>

# Follow logs
kubectl logs -f <pod-name>

# View logs from all pods
kubectl logs -l app=webapp
```

#### Scaling:

```bash
# Scale webapp deployment
kubectl scale deployment webapp --replicas=3

# Verify scaling
kubectl get pods
```

#### Cleanup:

```bash
# Delete resources
kubectl delete -f webapp-service.yaml
kubectl delete -f webapp-deployment.yaml
kubectl delete -f redis-service.yaml
kubectl delete -f redis-deployment.yaml

# Stop Minikube
minikube stop
```

---

## 🔄 Part 4: CI/CD Pipeline

### Task 4.1: CI/CD Implementation

**Objective:** Automate build, test, and deployment pipeline

_(Configuration files and details to be added in Task-4.1/Config-Files/)_

#### Typical CI/CD Workflow:

1. **Source Control** - Git repository (GitHub)
2. **Build Stage** - Docker image creation
3. **Test Stage** - Automated testing
4. **Deploy Stage** - Push to registry and deploy
5. **Monitoring** - Health checks and alerts

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. Docker Compose ContainerConfig Error

**Error:** `KeyError: 'ContainerConfig'`

**Solution:**

```bash
docker-compose down -v --remove-orphans
docker container prune -f
docker-compose up -d --build
```

#### 2. Nginx 502 Bad Gateway

**Possible Causes:**

- Gunicorn service not running
- Port mismatch
- Firewall blocking connections

**Solution:**

```bash
systemctl status webapp
systemctl restart webapp
systemctl restart nginx
```

#### 3. Minikube Start Issues

**Solution:**

```bash
minikube delete
minikube start --driver=docker --force
```

#### 4. Kubernetes Pod ImagePullBackOff

**Solution:**

```bash
# Load image into Minikube
minikube image load webapp:v1

# Update deployment
kubectl rollout restart deployment webapp
```

---

## ✅ Best Practices

### Security

- ✅ Use non-root users in containers
- ✅ Implement firewall rules
- ✅ Regular security updates
- ✅ Environment variable management
- ✅ Secret management (not hardcoded)

### Performance

- ✅ Multi-worker Gunicorn configuration
- ✅ Nginx reverse proxy for load balancing
- ✅ Resource limits in Kubernetes
- ✅ Redis caching for performance

### Reliability

- ✅ Health checks and probes
- ✅ Automated monitoring scripts
- ✅ Service restart policies
- ✅ Logging and error tracking

### DevOps

- ✅ Infrastructure as Code
- ✅ Version control for configurations
- ✅ Container orchestration
- ✅ Automated deployments

---

## 📚 References

### Official Documentation

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
- [Redis Documentation](https://redis.io/documentation)

### Tools & Technologies

- **Operating System:** Ubuntu 20.04+
- **Web Framework:** Flask 3.1.x
- **WSGI Server:** Gunicorn 23.x
- **Reverse Proxy:** Nginx
- **Containerization:** Docker 20.x+
- **Orchestration:** Kubernetes via Minikube
- **Caching:** Redis 7.x
- **Programming Language:** Python 3.11

---

## 🎓 Skills Demonstrated

- ✅ Linux system administration and user management
- ✅ Web server configuration and reverse proxy setup
- ✅ Python application deployment with production-grade servers
- ✅ System monitoring and automation with bash scripting
- ✅ Docker containerization and multi-stage builds
- ✅ Docker Compose for multi-container applications
- ✅ Kubernetes orchestration and service management
- ✅ Infrastructure as Code practices
- ✅ Security best practices and hardening
- ✅ Troubleshooting and debugging
- ✅ Documentation and knowledge transfer

---

## 📧 Contact

**GitHub:** [@Shachiru](https://github.com/Shachiru)  
**Repository:** [devops-assessment](https://github.com/Shachiru/devops-assessment)

---

## 📝 License

This project is created for educational and assessment purposes.

---

**Last Updated:** November 21, 2025  
**Version:** 1.0
