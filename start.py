#!/usr/bin/env python3
"""
Startup script for LLM Knowledge Extractor
This script checks for dependencies and starts the application.
"""

import sys
import subprocess
import os

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = [
        'fastapi',
        'uvicorn', 
        'openai',
        'nltk',
        'pydantic',
        'python-multipart',
        'jinja2',
        'aiofiles',
        'requests',
        'dotenv'
    ]
    
    missing_packages = []
    
    # Special handling for packages with different import names
    import_mapping = {
        'python-multipart': 'multipart'
    }
    
    for package in required_packages:
        try:
            import_name = import_mapping.get(package, package.replace('-', '_'))
            __import__(import_name)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n💡 Install them with:")
        print("   pip install -r requirements.txt")
        return False
    
    return True

def check_openai_key():
    """Check if OpenAI API key is set."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️  OpenAI API key not found!")
        print("   The app will run in demo mode with mock responses.")
        print("   To use real LLM analysis, set your API key:")
        print("   Windows: $env:OPENAI_API_KEY='your-key-here'")
        print("   Linux/Mac: export OPENAI_API_KEY='your-key-here'")
        print()
    else:
        print("✅ OpenAI API key found - real LLM analysis enabled!")
    
    return True

def start_server():
    """Start the FastAPI server."""
    print("🚀 Starting LLM Knowledge Extractor...")
    print("📱 Web UI: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("🛑 Press Ctrl+C to stop")
    print("=" * 50)
    
    try:
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    print("🧠 LLM Knowledge Extractor - Startup Check")
    print("=" * 50)
    
    if not check_dependencies():
        sys.exit(1)
    
    check_openai_key()
    
    start_server()
