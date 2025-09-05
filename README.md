# LLM Knowledge Extractor

A prototype application that extracts structured insights from unstructured text using Large Language Models (LLMs) and natural language processing.

## 🚀 Features

- **Text Analysis**: Accepts any block of unstructured text input
- **LLM Integration**: Uses OpenAI GPT-3.5-turbo for intelligent analysis
- **Structured Output**: Generates summary and metadata including:
  - 1-2 sentence summary
  - Title extraction
  - 3 key topics/themes
  - Sentiment analysis (positive/neutral/negative)
  - Top 3 most frequent nouns as keywords
- **Dual Interface**: Both REST API and web UI
- **Fallback Mode**: Works without OpenAI API key using mock responses
- **Docker Support**: Fully containerized with Docker Compose
- **Cross-Platform**: Works on Windows, Linux, and Mac

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or higher (for local development)
- Docker and Docker Compose (for containerized deployment)
- OpenAI API key (optional - app works in demo mode without it)

### Option 1: Docker Deployment (Recommended)

1. **Clone or download the project**
   ```bash
   cd "LLM Knowledge Extractor"
   ```

2. **Set up OpenAI API key (optional)**
   ```bash
   # Windows PowerShell
   $env:OPENAI_API_KEY="your-api-key-here"
   
   # Windows Command Prompt
   set OPENAI_API_KEY=your-api-key-here
   
   # Linux/Mac
   export OPENAI_API_KEY="your-api-key-here"
   ```

3. **Build and run with Docker Compose**
   ```bash
   # Using helper script (PowerShell)
   .\docker-scripts.ps1 compose
   
   # Or manually
   docker-compose up -d
   ```

4. **Access the application**
   - Web UI: http://localhost:8000
   - API docs: http://localhost:8000/docs

### Option 2: Local Development

1. **Clone or download the project**
   ```bash
   cd "LLM Knowledge Extractor"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key (optional)**
   ```bash
   # Windows PowerShell
   $env:OPENAI_API_KEY="your-api-key-here"
   
   # Windows Command Prompt
   set OPENAI_API_KEY=your-api-key-here
   
   # Linux/Mac
   export OPENAI_API_KEY="your-api-key-here"
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Access the application**
   - Web UI: http://localhost:8000
   - API docs: http://localhost:8000/docs

## 🐳 Docker Commands

### Quick Start
```bash
# Build and run with Docker Compose (recommended)
docker-compose up -d

# Or use the helper script
.\docker-scripts.ps1 compose  # Windows PowerShell
./docker-scripts.sh compose   # Linux/Mac
```

### Manual Docker Commands
```bash
# Build the image
docker build -t llm-knowledge-extractor .

# Run the container
docker run -d -p 8000:8000 -e OPENAI_API_KEY="your-key" llm-knowledge-extractor

# View logs
docker logs -f llm-knowledge-extractor

# Stop the container
docker stop llm-knowledge-extractor
```

### Docker Helper Scripts
The project includes helper scripts for common Docker operations:

**Windows PowerShell:**
```powershell
.\docker-scripts.ps1 build      # Build image
.\docker-scripts.ps1 run        # Run container
.\docker-scripts.ps1 compose    # Run with docker-compose
.\docker-scripts.ps1 logs       # Show logs
.\docker-scripts.ps1 cleanup    # Stop and remove containers
```

**Linux/Mac:**
```bash
./docker-scripts.sh build       # Build image
./docker-scripts.sh run         # Run container
./docker-scripts.sh compose     # Run with docker-compose
./docker-scripts.sh logs        # Show logs
./docker-scripts.sh cleanup     # Stop and remove containers
```

### Docker Features
- **Security**: Non-root user execution, minimal base image
- **Performance**: Multi-layer caching, NLTK data pre-downloaded
- **Development**: Volume mounting for live code changes
- **Health Checks**: Built-in health monitoring

### Docker Troubleshooting
```bash
# Clean build (no cache)
docker build --no-cache -t llm-knowledge-extractor .

# Check container logs
docker logs llm-extractor

# Access container shell
docker exec -it llm-extractor /bin/bash

# Port conflicts - use different port
docker run -p 8001:8000 llm-knowledge-extractor
```

## 📡 API Usage

### POST /analyze
Analyze text and return structured data.

**Request:**
```json
{
  "text": "Your text content here..."
}
```

**Response:**
```json
{
  "summary": "1-2 sentence summary of the text",
  "metadata": {
    "title": "Extracted or generated title",
    "topics": ["topic1", "topic2", "topic3"],
    "sentiment": "positive|neutral|negative",
    "keywords": ["keyword1", "keyword2", "keyword3"]
  }
}
```

**Example with curl:**
```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "Artificial intelligence is transforming industries worldwide..."}'
```

## 🏗️ Architecture & Design

### Technology Stack
- **Backend**: FastAPI (Python) - Modern, fast, with automatic API docs
- **LLM**: OpenAI GPT-3.5-turbo - Cost-effective and reliable
- **NLP**: NLTK - Lightweight keyword extraction
- **Frontend**: HTML/CSS/JavaScript - Clean, responsive design
- **Templates**: Jinja2 - Server-side rendering
- **Containerization**: Docker with multi-stage builds

### Key Design Decisions

1. **Hybrid Analysis Approach**: Combined LLM analysis with traditional NLP for keywords to balance cost and accuracy
2. **Graceful Degradation**: App works in demo mode without API keys, making it immediately runnable
3. **Dual Interface**: Both API and web UI to demonstrate different use cases
4. **Docker-First**: Fully containerized for consistent deployment across environments
5. **Error Handling**: Comprehensive error handling with fallback responses
6. **Responsive Design**: Modern, mobile-friendly web interface

### Project Structure
```
LLM Knowledge Extractor/
├── main.py                 # Main FastAPI application
├── start.py               # Startup script with dependency checks
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker container configuration
├── docker-compose.yml     # Docker Compose configuration
├── docker-scripts.ps1     # Docker helper scripts (Windows)
├── docker-scripts.sh      # Docker helper scripts (Linux/Mac)
├── test_example.py        # API testing script
├── test_simple.py         # Simple functionality tests
└── templates/
    └── index.html         # Web UI template
```

## ⚡ Trade-offs Made

### What Was Prioritized
- ✅ Core functionality working end-to-end
- ✅ Clean, professional code structure
- ✅ Comprehensive documentation
- ✅ Error handling and graceful degradation
- ✅ Modern, responsive UI
- ✅ Docker containerization

### What Was Deferred (Due to time constraints)
- ❌ Database storage (SQLite/PostgreSQL)
- ❌ Search/filter endpoints
- ❌ Unit tests
- ❌ Advanced error handling
- ❌ Caching layer
- ❌ Authentication

### Technical Trade-offs
1. **Mock LLM Responses**: When API key is missing, provides demo functionality
2. **Simple NLP**: Used basic noun extraction instead of more sophisticated keyword algorithms
3. **Limited Text Length**: Truncates very long texts to stay within API limits
4. **No Caching**: Each request hits the LLM API (could be optimized with Redis/memory cache)

## 🔮 Future Enhancements

If given more time, I would add:
- **Database Integration**: SQLite/PostgreSQL for storing analysis results
- **Search/Filter API**: Query stored analyses by sentiment, topics, or keywords
- **Batch Processing**: Analyze multiple texts at once
- **Advanced NLP**: Named entity recognition, topic modeling
- **Caching Layer**: Redis for frequently analyzed content
- **Authentication**: User accounts and API keys
- **Comprehensive Testing**: Unit and integration tests
- **Rate Limiting**: API usage controls
- **Export Features**: Download results as JSON/CSV
- **Monitoring**: Application performance monitoring
- **Scaling**: Kubernetes deployment for production

## 📝 License

This is a take-home assignment prototype. Feel free to use and modify as needed.

---