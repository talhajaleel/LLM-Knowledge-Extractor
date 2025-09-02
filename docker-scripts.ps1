# Docker helper scripts for LLM Knowledge Extractor (PowerShell)

param(
    [Parameter(Position=0)]
    [string]$Command = "help"
)

# Colors for output
$Red = "Red"
$Green = "Green"
$Yellow = "Yellow"
$Blue = "Blue"

# Function to print colored output
function Write-Status {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor $Blue
}

function Write-Success {
    param([string]$Message)
    Write-Host "[SUCCESS] $Message" -ForegroundColor $Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "[WARNING] $Message" -ForegroundColor $Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor $Red
}

# Build the Docker image
function Build-Image {
    Write-Status "Building LLM Knowledge Extractor Docker image..."
    docker build -t llm-knowledge-extractor .
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Docker image built successfully!"
    } else {
        Write-Error "Failed to build Docker image!"
        exit 1
    }
}

# Run the container
function Start-Container {
    Write-Status "Starting LLM Knowledge Extractor container..."
    
    # Check if OpenAI API key is set
    if (-not $env:OPENAI_API_KEY) {
        Write-Warning "OPENAI_API_KEY not set. App will run in demo mode."
    }
    
    docker run -d `
        --name llm-extractor `
        -p 8000:8000 `
        --env-file .env `
        -e OPENAI_API_KEY="$env:OPENAI_API_KEY" `
        llm-knowledge-extractor
    
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Container started! Access the app at http://localhost:8000"
        Write-Status "To view logs: docker logs -f llm-extractor"
        Write-Status "To stop: docker stop llm-extractor"
    } else {
        Write-Error "Failed to start container!"
        exit 1
    }
}

# Run with docker-compose
function Start-Compose {
    Write-Status "Starting services with docker-compose..."
    docker-compose up -d
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Services started! Access the app at http://localhost:8000"
        Write-Status "To view logs: docker-compose logs -f"
        Write-Status "To stop: docker-compose down"
    } else {
        Write-Error "Failed to start services with docker-compose!"
        exit 1
    }
}

# Stop and remove containers
function Stop-Containers {
    Write-Status "Stopping and removing containers..."
    docker-compose down 2>$null
    docker stop llm-extractor 2>$null
    docker rm llm-extractor 2>$null
    Write-Success "Cleanup completed!"
}

# Show logs
function Show-Logs {
    $containerRunning = docker ps -q -f name=llm-extractor 2>$null
    $composeRunning = docker-compose ps -q 2>$null
    
    if ($containerRunning) {
        docker logs -f llm-extractor
    } elseif ($composeRunning) {
        docker-compose logs -f
    } else {
        Write-Error "No running containers found!"
    }
}

# Show help
function Show-Help {
    Write-Host "LLM Knowledge Extractor - Docker Helper Scripts (PowerShell)" -ForegroundColor $Green
    Write-Host ""
    Write-Host "Usage: .\docker-scripts.ps1 [COMMAND]"
    Write-Host ""
    Write-Host "Commands:"
    Write-Host "  build       Build the Docker image"
    Write-Host "  run         Run the container (standalone)"
    Write-Host "  compose     Run with docker-compose"
    Write-Host "  logs        Show container logs"
    Write-Host "  cleanup     Stop and remove all containers"
    Write-Host "  help        Show this help message"
    Write-Host ""
    Write-Host "Environment Variables:"
    Write-Host "  OPENAI_API_KEY    Your OpenAI API key (optional)"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "  .\docker-scripts.ps1 build"
    Write-Host "  `$env:OPENAI_API_KEY='your-key-here'; .\docker-scripts.ps1 run"
    Write-Host "  .\docker-scripts.ps1 compose"
    Write-Host "  .\docker-scripts.ps1 logs"
}

# Main script logic
switch ($Command.ToLower()) {
    "build" {
        Build-Image
    }
    "run" {
        Start-Container
    }
    "compose" {
        Start-Compose
    }
    "logs" {
        Show-Logs
    }
    "cleanup" {
        Stop-Containers
    }
    "help" {
        Show-Help
    }
    default {
        Write-Error "Unknown command: $Command"
        Show-Help
        exit 1
    }
}
