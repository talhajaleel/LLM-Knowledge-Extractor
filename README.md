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

## 🎨 Design Choices & Architecture

### Technology Stack
- **FastAPI**: Chosen for its excellent performance, automatic API documentation, and modern Python async support
- **OpenAI GPT-3.5-turbo**: Cost-effective LLM with good performance for text analysis tasks
- **NLTK**: Lightweight NLP library for keyword extraction without requiring LLM calls
- **Jinja2**: Simple templating for the web UI
- **Pydantic**: Type safety and data validation

### Architecture Decisions

1. **Hybrid Approach**: Combined LLM analysis with traditional NLP for keywords to balance cost and accuracy
2. **Graceful Degradation**: App works in demo mode without API keys, making it immediately runnable
3. **Dual Interface**: Both API and web UI to demonstrate different use cases
4. **Error Handling**: Comprehensive error handling with fallback responses
5. **Responsive Design**: Modern, mobile-friendly web interface

### Code Structure
- **Single-file application**: Kept simple for rapid prototyping
- **Async/await**: Used throughout for better performance with I/O operations
- **Separation of concerns**: Clear separation between NLP, LLM, and web logic
- **Type hints**: Full type annotations for better code maintainability

## ⚡ Trade-offs Made

### Time Constraints (2-hour limit)
1. **No Database**: Skipped persistent storage to focus on core functionality
2. **No Tests**: Prioritized working code over test coverage
3. **No Docker**: Simplified deployment without containerization
4. **Basic Error Handling**: Implemented essential error handling but not exhaustive
5. **Single File**: Kept everything in main.py for simplicity

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
- **Docker Support**: Containerized deployment
- **Comprehensive Testing**: Unit and integration tests
- **Rate Limiting**: API usage controls
- **Export Features**: Download results as JSON/CSV

## 📝 License

This is a take-home assignment prototype. Feel free to use and modify as needed.

---

**Built with ❤️ for the Jouster take-home assignment**
