#  English to Spanish Translator using FastAPI & Groq (LLaMA3)

This project is a simple API-based English-to-Spanish translator built using:

-  **Groq API** with the **LLaMA3-8B-8192** model
-  **FastAPI** for creating a lightweight and blazing-fast REST API
-  **Pydantic** for request validation

---

## Features

- Translate English text to Spanish via an API
- Uses Groq’s powerful LLaMA3 model for high-quality translations
- Exposes a clean REST endpoint via FastAPI
- Modular and easily extensible

---
### 1. Clone the Repository

```bash
git clone https://github.com/jeevvanth/Prompt_Engineering_using_llama.git
cd Prompt_Engineering_using_llama
```

### 2. Set Up a Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### Set Your Groq API Key
Create a .env file in your root directory:
```bash
GROQ_API_KEY=your_groq_api_key_here
```



