#!/usr/bin/env python3
"""
Simple test script that doesn't require external dependencies
This tests the core functionality of the LLM Knowledge Extractor
"""

import sys
import os

# Add the current directory to the path so we can import from main
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_keyword_extraction():
    """Test the keyword extraction functionality."""
    print("🧪 Testing keyword extraction...")
    
    try:
        from main import extract_keywords
        
        sample_text = """
        Artificial intelligence is revolutionizing technology and business. 
        Machine learning algorithms are becoming more sophisticated every day.
        Companies are investing heavily in AI research and development.
        """
        
        keywords = extract_keywords(sample_text)
        print(f"✅ Keywords extracted: {keywords}")
        return True
        
    except Exception as e:
        print(f"❌ Keyword extraction failed: {e}")
        return False

def test_title_extraction():
    """Test the title extraction functionality."""
    print("🧪 Testing title extraction...")
    
    try:
        from main import extract_title
        
        sample_text = "This is a sample article about technology. It discusses various topics."
        title = extract_title(sample_text)
        print(f"✅ Title extracted: {title}")
        return True
        
    except Exception as e:
        print(f"❌ Title extraction failed: {e}")
        return False

def test_imports():
    """Test that all required modules can be imported."""
    print("🧪 Testing imports...")
    
    required_modules = [
        'fastapi',
        'uvicorn',
        'openai', 
        'nltk',
        'pydantic',
        'multipart',  # python-multipart imports as 'multipart'
        'jinja2',
        'dotenv'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n⚠️  Missing modules: {', '.join(failed_imports)}")
        print("Install with: pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Run all tests."""
    print("🧠 LLM Knowledge Extractor - Simple Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_keyword_extraction,
        test_title_extraction
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application should work correctly.")
        print("\n🚀 To start the server:")
        print("   python main.py")
        print("\n📱 Then visit: http://localhost:8000")
    else:
        print("⚠️  Some tests failed. Please install missing dependencies.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
