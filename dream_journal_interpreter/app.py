import os
import json
from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

# Retrieve Gemini API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Set up the Gemini model (e.g., gemini-1.5-flash)
model = genai.GenerativeModel('gemini-1.5-flash')

# Path to store dream entries locally (JSON for simplicity)
DATA_FILE = os.path.join('data', 'dreams.json')
if not os.path.exists('data'):
    os.makedirs('data')
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Function to load dream entries with error handling
def load_entries():
    try:
        with open(DATA_FILE, 'r') as f:
            content = f.read().strip()
            if not content:  # If file is empty, return empty list
                return []
            return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        # If file is corrupted or missing, initialize it with empty list
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
        return []

# Function to save dream entries
def save_entry(entry):
    entries = load_entries()
    entries.append(entry)
    with open(DATA_FILE, 'w') as f:
        json.dump(entries, f, indent=2)

# Route for the main dream journal page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dream_text = request.form.get('dream_text')
        emotions = request.form.get('emotions')
        symbols = request.form.get('symbols')
        if dream_text:
            # Generate a prompt for Gemini to interpret the dream
            prompt = f"""
            You are a dream interpreter providing reflective and creative insights. 
            Analyze the user's dream description and offer a speculative interpretation based on common dream symbolism.
            Keep the response short (3-4 sentences), emphasize and provide psychological diagnoses.
            Dream description: {dream_text}
            Emotions felt during dream: {emotions if emotions else 'Not specified'}
            Key symbols or themes: {symbols if symbols else 'Not specified'}
            """
            try:
                # Call Gemini API to generate response
                response = model.generate_content(prompt)
                ai_interpretation = response.text
            except Exception as e:
                ai_interpretation = "I'm sorry, I couldn't interpret your dream right now. Please try again."
                print(f"Gemini API Error: {e}")

            # Save entry with timestamp
            entry_data = {
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'dream_text': dream_text,
                'emotions': emotions if emotions else 'Not specified',
                'symbols': symbols if symbols else 'Not specified',
                'ai_interpretation': ai_interpretation
            }
            save_entry(entry_data)
            return redirect(url_for('index'))
    return render_template('index.html', entries=load_entries())

# Route to view history of dream entries
@app.route('/history')
def history():
    entries = load_entries()
    return render_template('history.html', entries=entries[::-1])  # Reverse to show newest first

if __name__ == '__main__':
    app.run(debug=True)