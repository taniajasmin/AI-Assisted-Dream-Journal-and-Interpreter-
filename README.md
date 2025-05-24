# AI-Assisted Dream Journal and Interpreter 🌙✨

## Overview 📝
This application allows users to record their dreams and receive AI-generated interpretations based on common dream symbolism. It’s designed for entertainment and personal reflection, helping users explore their subconscious thoughts through a creative lens. 💭🌌

The AI analyzes dream descriptions, emotions, and key symbols to offer speculative insights, with a clear disclaimer that these are not psychological diagnoses.

## Features 🌟
  **Dream Logging:** Record detailed dream descriptions, emotions felt, and key symbols or themes. 📖
  **AI Interpretation:** Receive creative insights using Google’s Gemini API, with a focus on reflection and entertainment. 🤖💡
  **Recurring Theme Tracking:** Input symbols or themes to track patterns over time (basic tagging). 🔍
  **Dream History:** View past dream entries and interpretations in reverse chronological order. 🕒
  **Local Storage:** All entries are stored locally in a JSON file for privacy. 🔒

## Technologies Used 💻
  **Flask:** Python web framework for the backend. 🐍
  **Google Gemini API:** Large Language Model API for generating dream interpretations. 🌠
  **HTML/CSS:** Frontend interface. 🌐
  **JSON:** Local data storage format. 📊
  
## Installation 🛠️
1. Set up a virtual environment (recommended) 🕹️
   ```BASH
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install dependencies 📦
   ```BASH
   pip install -r requirements.txt

3. Create a .env file in the project root with your Gemini API key 🔑
   ```BASH
   GEMINI_API_KEY=your_gemini_api_key_here
Get your API key from Google AI Studio

## Usage 🚀
1. Start the application ▶️
  ```BASH
python app.py
```
2. Open your browser and navigate to http://127.0.0.1:5000/ 🌍
3. Begin logging dreams by describing your dream, noting emotions and symbols, and clicking submit. ✍️
4. View history by clicking the "View Dream History" link. 📜

## Project Structure 🗂️
```

dream_journal_interpreter/
│
├── app.py                # Main Flask application
├── templates/            # HTML templates
│   ├── index.html        # Main dream logging page
│   └── history.html      # Page to view past dreams
├── static/               # Static files
│   └── style.css         # CSS styling
├── data/                 # Data storage
│   └── dreams.json       # JSON file storing dream entries
├── .env                  # Environment variables (not in version control)
└── requirements.txt      # Project dependencies
```

## Configuration ⚙️
You can customize the AI interpretation by modifying the prompt in app.py:
``` Python
prompt = f"""
You are a dream interpreter providing reflective and creative insights. 
Analyze the user's dream description and offer a speculative interpretation based on common dream symbolism.
Keep the response short (3-4 sentences), emphasize that this is for entertainment and reflection, and avoid definitive psychological diagnoses.
Dream description: {dream_text}
Emotions felt during dream: {emotions if emotions else 'Not specified'}
Key symbols or themes: {symbols if symbols else 'Not specified'}
"""
```
Adjust this prompt to change the tone, depth, or style of dream interpretations. 🎨

## Privacy and Security 🔐
- All dream entries are stored locally on your machine in the data/dreams.json file. 💾
- No data is sent to external servers except for the dream content sent to Google's Gemini API for interpretation. 🌐
- Your Gemini API key is stored in the .env file, which should not be committed to version control. 🚫


## Future Enhancements 🚀
- Advanced theme/pattern analysis with visualizations (e.g., frequency of symbols like "water" or "flying"). 📈
- **Dream categorization by type (e.g., lucid, nightmare). 🌀**
- Export functionality for dream logs (PDF, text). 📤
- Password protection for privacy. 🔒
- Integration with sleep tracking data if available. 😴

## Disclaimer ⚠️
This application is for entertainment and personal reflection purposes only. Dream interpretations are speculative and based on common symbolism; they are not professional psychological analyses. For serious mental health concerns or sleep disorders, please consult a qualified professional.

## Acknowledgements 🙏
- Google Gemini API for powering the AI interpretations. 🤖
- Flask for the web framework. 🐍
