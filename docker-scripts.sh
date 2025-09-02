#!/bin/bash

# Docker helper scripts for LLM Knowledge Extractor

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Build the Docker image
build() {
    print_status "Building LLM Knowledge Extractor Docker image..."
    docker build -t llm-knowledge-extractor .
    print_success "Docker image built successfully!"
}

# Run the container
run() {
    print_status "Starting LLM Knowledge Extractor container..."
    
    # Check if OpenAI API key is set
    if [ -z "$OPENAI_API_KEY" ]; then
        print_warning "OPENAI_API_KEY not set. App will run in demo mode."
    fi
    
    docker run -d \
        --name llm-extractor \
        -p 8000:8000 \
        --env-file .env \
        -e OPENAI_API_KEY="$OPENAI_API_KEY" \
        llm-knowledge-extractor
    
    print_success "Container started! Access the app at http://localhost:8000"
    print_status "To view logs: docker logs -f llm-extractor"
    print_status "To stop: docker stop llm-extractor"
}

# Run with docker-compose
compose_up() {
    print_status "Starting services with docker-compose..."
    docker-compose up -d
    print_success "Services started! Access the app at http://localhost:8000"
    print_status "To view logs: docker-compose logs -f"
    print_status "To stop: docker-compose down"
}

# Stop and remove containers
cleanup() {
    print_status "Stopping and removing containers..."
    docker-compose down 2>/dev/null || true
    docker stop llm-extractor 2>/dev/null || true
    docker rm llm-extractor 2>/dev/null || true
    print_success "Cleanup completed!"
}

# Show logs
logs() {
    if docker ps -q -f name=llm-extractor > /dev/null 2>&1; then
        docker logs -f llm-extractor
    elif docker-compose ps -q > /dev/null 2>&1; then
        docker-compose logs -f
    else
        print_error "No running containers found!"
    fi
}

# Show help
help() {
    echo "LLM Knowledge Extractor - Docker Helper Scripts"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  build       Build the Docker image"
    echo "  run         Run the container (standalone)"
    echo "  compose     Run with docker-compose"
    echo "  logs        Show container logs"
    echo "  cleanup     Stop and remove all containers"
    echo "  help        Show this help message"
    echo ""
    echo "Environment Variables:"
    echo "  OPENAI_API_KEY    Your OpenAI API key (optional)"
    echo ""
    echo "Examples:"
    echo "  $0 build"
    echo "  OPENAI_API_KEY=your-key-here $0 run"
    echo "  $0 compose"
    echo "  $0 logs"
}

# Main script logic
case "${1:-help}" in
    build)
        build
        ;;
    run)
        run
        ;;
    compose)
        compose_up
        ;;
    logs)
        logs
        ;;
    cleanup)
        cleanup
        ;;
    help|--help|-h)
        help
        ;;
    *)
        print_error "Unknown command: $1"
        help
        exit 1
        ;;
esac
