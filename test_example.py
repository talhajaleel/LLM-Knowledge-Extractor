#!/usr/bin/env python3
"""
Example script to test the LLM Knowledge Extractor API
Run this after starting the main application with: python main.py
"""

import requests
import json

def test_api():
    """Test the /analyze endpoint with sample text."""
    
    # Sample text for testing
    sample_text = """
    Artificial intelligence is revolutionizing the way we work and live. 
    From healthcare to finance, AI technologies are being deployed to solve complex problems 
    and improve efficiency. Machine learning algorithms can now process vast amounts of data 
    to identify patterns and make predictions with remarkable accuracy. 
    
    However, the rapid advancement of AI also raises important questions about ethics, 
    privacy, and the future of employment. As we embrace these technologies, we must 
    ensure they are developed and deployed responsibly, with proper safeguards to protect 
    individual rights and promote societal benefit.
    
    The future of AI looks promising, with emerging applications in areas like autonomous 
    vehicles, personalized medicine, and climate change mitigation. Companies and governments 
    worldwide are investing heavily in AI research and development, recognizing its potential 
    to drive innovation and economic growth.
    """
    
    # API endpoint
    url = "http://localhost:8000/analyze"
    
    # Request payload
    payload = {
        "text": sample_text
    }
    
    try:
        print("🚀 Testing LLM Knowledge Extractor API...")
        print("=" * 50)
        
        # Make the API request
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            
            print("✅ Analysis completed successfully!")
            print("\n📝 Summary:")
            print(result["summary"])
            
            print("\n📊 Metadata:")
            metadata = result["metadata"]
            
            if metadata.get("title"):
                print(f"📌 Title: {metadata['title']}")
            
            print(f"😊 Sentiment: {metadata['sentiment']}")
            
            print(f"🏷️  Topics: {', '.join(metadata['topics'])}")
            
            print(f"🔑 Keywords: {', '.join(metadata['keywords'])}")
            
            print("\n" + "=" * 50)
            print("🎉 Test completed successfully!")
            
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the server is running!")
        print("   Start the server with: python main.py")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_api()
