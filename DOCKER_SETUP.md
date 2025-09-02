# Docker Setup for LLM Knowledge Extractor

## 🐳 Docker Files Added

The following Docker-related files have been added to the project:

### Core Docker Files
- **`Dockerfile`** - Multi-stage Docker image configuration
- **`docker-compose.yml`** - Docker Compose configuration for easy deployment
- **`.dockerignore`** - Excludes unnecessary files from Docker build context

### Helper Scripts
- **`docker-scripts.sh`** - Bash script for Linux/Mac users
- **`docker-scripts.ps1`** - PowerShell script for Windows users

## 🚀 Quick Start

### Using Docker Compose (Recommended)
```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

### Using Helper Scripts

**Windows PowerShell:**
```powershell
.\docker-scripts.ps1 compose    # Start with docker-compose
.\docker-scripts.ps1 build      # Build image only
.\docker-scripts.ps1 run        # Run standalone container
.\docker-scripts.ps1 logs       # View logs
.\docker-scripts.ps1 cleanup    # Stop and remove containers
```

**Linux/Mac:**
```bash
./docker-scripts.sh compose     # Start with docker-compose
./docker-scripts.sh build       # Build image only
./docker-scripts.sh run         # Run standalone container
./docker-scripts.sh logs        # View logs
./docker-scripts.sh cleanup     # Stop and remove containers
```

## 🔧 Docker Features

### Security
- Non-root user execution
- Minimal base image (Python 3.11 slim)
- Health checks included

### Performance
- Multi-layer caching for faster rebuilds
- NLTK data downloaded during build
- Optimized layer structure

### Development
- Volume mounting for live code changes
- Environment variable support
- Easy port configuration

## 📋 Environment Variables

Set these environment variables before running:

```bash
# Required for real LLM analysis (optional for demo mode)
OPENAI_API_KEY=your-openai-api-key-here
```

## 🏗️ Docker Image Details

- **Base Image**: `python:3.11-slim`
- **Working Directory**: `/app`
- **Port**: `8000`
- **User**: `app` (non-root)
- **Health Check**: HTTP endpoint check every 30s

## 🔍 Troubleshooting

### Build Issues
```bash
# Clean build (no cache)
docker build --no-cache -t llm-knowledge-extractor .

# Check build context
docker build --progress=plain -t llm-knowledge-extractor .
```

### Runtime Issues
```bash
# Check container logs
docker logs llm-extractor

# Check container status
docker ps -a

# Access container shell
docker exec -it llm-extractor /bin/bash
```

### Port Conflicts
If port 8000 is already in use, modify the port mapping:
```bash
# In docker-compose.yml, change:
ports:
  - "8001:8000"  # Use port 8001 instead

# Or for standalone container:
docker run -p 8001:8000 llm-knowledge-extractor
```

## 📊 Production Considerations

For production deployment, consider:

1. **Environment Variables**: Use proper secret management
2. **Resource Limits**: Add memory and CPU limits
3. **Logging**: Configure proper log aggregation
4. **Monitoring**: Add application monitoring
5. **SSL/TLS**: Use reverse proxy with SSL termination
6. **Scaling**: Use Docker Swarm or Kubernetes for scaling

## 🎯 Benefits of Docker Setup

✅ **Consistency**: Same environment across development, staging, and production  
✅ **Isolation**: No conflicts with local Python installations  
✅ **Portability**: Easy deployment to any Docker-compatible platform  
✅ **Scalability**: Easy to scale horizontally with orchestration tools  
✅ **Security**: Non-root execution and minimal attack surface  
✅ **Maintenance**: Easy updates and rollbacks  

---

**The LLM Knowledge Extractor is now fully containerized and ready for deployment! 🚀**
