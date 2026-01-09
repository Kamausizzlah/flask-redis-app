# Flask Redis Hit Counter

A modern Flask web application that uses Redis to track page views. This project demonstrates containerized application development with Docker, automated testing, and a complete CI/CD pipeline using GitHub Actions.

## Overview

This is a DevOps project that showcases:

- **Multi-container application** with Flask and Redis
- **Automated testing** with unit tests
- **CI/CD pipeline** using GitHub Actions
- **Docker containerization** for consistent deployments
- **Docker Hub integration** for image registry

## Features

✅ Simple hit counter that tracks page views  
✅ Redis backend for persistent data storage  
✅ Docker and Docker Compose support  
✅ Automated unit tests  
✅ GitHub Actions CI/CD pipeline  
✅ Automatic Docker image builds and pushes to Docker Hub

## Project Structure

├── src/
│ ├── app.py # Flask application
│ ├── requirements.txt # Python dependencies
│ └── tests/
│ └── test_app.py # Unit tests
├── .github/
│ └── workflows/
│ └── main.yml # GitHub Actions CI/CD workflow
├── Dockerfile # Docker image configuration
├── docker-compose.yml # Local development setup
├── docker-compose.prod.yml # Production setup
├── .gitignore # Git ignore rules
└── README.md # This file

## Quick Start

### Prerequisites

- Docker & Docker Compose (recommended)
- Python 3.9+ (for local development)
- Redis (for local development without Docker)
- Git

### Running with Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/Kamausizzlah/flask-redis-app.git
cd flask-redis-app

# Start the application
docker-compose up

# Visit http://localhost:5000 in your browser
```
