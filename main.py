import os
import json
import re
from typing import Dict, List, Optional, Any
from collections import Counter
import nltk
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from openai import OpenAI
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

app = FastAPI(title="LLM Knowledge Extractor", version="1.0.0")

# Templates for web UI
templates = Jinja2Templates(directory="templates")

# Initialize OpenAI client
openai_client = None

class AnalysisRequest(BaseModel):
    text: str

class AnalysisResponse(BaseModel):
    summary: str
    metadata: Dict[str, Any]

def extract_keywords(text: str, num_keywords: int = 3) -> List[str]:
    """Extract the most frequent nouns from text using simple NLP."""
    # Tokenize and tag parts of speech
    tokens = word_tokenize(text.lower())
    pos_tags = pos_tag(tokens)
    
    # Filter for nouns (NN, NNS, NNP, NNPS)
    nouns = [word for word, pos in pos_tags if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
    
    # Remove stopwords and short words
    stop_words = set(stopwords.words('english'))
    filtered_nouns = [word for word in nouns if word not in stop_words and len(word) > 2]
    
    # Count frequency and return top keywords
    word_freq = Counter(filtered_nouns)
    return [word for word, count in word_freq.most_common(num_keywords)]

def extract_title(text: str) -> Optional[str]:
    """Extract a potential title from the text (first sentence or line)."""
    # Try to get the first sentence
    sentences = re.split(r'[.!?]+', text.strip())
    if sentences and sentences[0].strip():
        title = sentences[0].strip()
        # Limit title length
        if len(title) > 100:
            title = title[:97] + "..."
        return title
    return None

async def analyze_with_llm(text: str) -> Dict[str, Any]:
    """Use OpenAI to generate summary and extract structured metadata."""
    
    # Get API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key or api_key == "your-openai-api-key-here":
        # Mock response for demo purposes
        return {
            "summary": "This is a mock summary generated when no OpenAI API key is provided.",
            "title": extract_title(text),
            "topics": ["Technology", "Innovation", "Development"],
            "sentiment": "neutral"
        }
    
    try:
        prompt = f"""
        Analyze the following text and provide:
        1. A 1-2 sentence summary
        2. 3 key topics/themes
        3. Overall sentiment (positive/neutral/negative)
        
        Text: {text[:2000]}  # Limit text length for API
        
        Respond in JSON format:
        {{
            "summary": "1-2 sentence summary here",
            "topics": ["topic1", "topic2", "topic3"],
            "sentiment": "positive/neutral/negative"
        }}
        """
        
        # Initialize OpenAI client with API key
       
        client = OpenAI(
            api_key=api_key
        )
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.3
        )
        
        # Parse the JSON response
        content = response.choices[0].message.content.strip()
        # Remove any markdown formatting
        content = content.replace("```json", "").replace("```", "").strip()
        
        llm_result = json.loads(content)
        
        return {
            "summary": llm_result.get("summary", "Unable to generate summary"),
            "title": extract_title(text),
            "topics": llm_result.get("topics", ["Unknown"]),
            "sentiment": llm_result.get("sentiment", "neutral")
        }
        
    except Exception as e:
        print(f"LLM analysis error: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        # Fallback response
        return {
            "summary": f"Unable to generate summary due to API error: {str(e)}",
            "title": extract_title(text),
            "topics": ["Analysis", "Content", "Information"],
            "sentiment": "neutral"
        }

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main web interface."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze_text(request: AnalysisRequest):
    """API endpoint to analyze text and return structured data."""
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text input cannot be empty")
    
    # Extract keywords using NLP
    keywords = extract_keywords(request.text)
    
    # Get LLM analysis
    llm_analysis = await analyze_with_llm(request.text)
    
    # Combine results
    result = {
        "summary": llm_analysis["summary"],
        "metadata": {
            "title": llm_analysis["title"],
            "topics": llm_analysis["topics"],
            "sentiment": llm_analysis["sentiment"],
            "keywords": keywords
        }
    }
    
    return result

@app.post("/analyze-form")
async def analyze_text_form(request: Request, text: str = Form(...)):
    """Handle form submission from web UI."""
    if not text.strip():
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": "Text input cannot be empty"
        })
    
    # Extract keywords using NLP
    keywords = extract_keywords(text)
    
    # Get LLM analysis
    llm_analysis = await analyze_with_llm(text)
    
    # Combine results
    result = {
        "summary": llm_analysis["summary"],
        "metadata": {
            "title": llm_analysis["title"],
            "topics": llm_analysis["topics"],
            "sentiment": llm_analysis["sentiment"],
            "keywords": keywords
        }
    }
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "input_text": text
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
