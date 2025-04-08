---

# 🗣️ Igbo Chatbot for Office Stationery Sales (Local Project)

This project is a **local educational chatbot** that speaks in **Igbo language** to help customers inquire about **office stationery** products like pens, paper, notebooks, etc. It uses `Ollama` and `Qwen 2.5` as the language model backend and features a simple **Python + Streamlit** frontend.

---

## 📋 Project Breakdown

### ✅ Project Goal

To create a local, educational **Igbo-language chatbot** for **customer support** in office supply sales using:

- Python (core logic)
- Streamlit (for user interface)
- Ollama + Qwen2.5 (for the LLM backend)
- Open-source tools only

---

## 🧱 Tasks Breakdown

### 1. 📁 Project Setup

- Create a project folder `igbo-chatbot/`
- Set up a virtual environment:  
  ```bash
  python3 -m venv .myvenv
  source .myvenv/bin/activate
  ```
- Install dependencies:  
  ```bash
  pip install streamlit requests ollama
  ```

---

### 2. 🧠 Dataset Generation

- Auto-generate **50–100 Igbo Q&A pairs** for stationery sales using a Python script.
- Store it in: `data/igbo_faq.json`

Script:
```bash
python scripts/generate_dataset.py
```

---

### 3. 🔌 Set Up Ollama with Qwen 2.5

- Ensure you have [Ollama](https://ollama.com/) installed.
- Pull and run Qwen 2.5:
  ```bash
  ollama pull qwen:2.5
  ollama run qwen:2.5
  ```

---

### 4. 🧠 Local API Backend (Optional)

Create a simple Python API using **FastAPI or Flask** (optional) to:

- Load the dataset
- Interface with Ollama
- Process user input and return chatbot responses

---

### 5. 🎨 Streamlit Frontend

Create a `main.py` for a **simple chatbot UI**:

- Textbox for user questions
- Display previous chat history
- Show model-generated answers

Run the app:
```bash
streamlit run main.py
```

---

### 6. 🧪 Testing

Create **unit tests** using `pytest` or `unittest`:

- Test dataset integrity (valid Q&A format)
- Validate chatbot response structure
- Ensure Ollama API call works
- UI loads successfully

---

### 7. 🧠 Future Upgrades (Optional)

- Add voice-to-text or text-to-speech in Igbo
- Support multiple product categories
- Add chatbot memory (context tracking)
- Train with more advanced fine-tuned models

---

## 📁 Recommended Folder Structure

```
igbo-chatbot/
├── data/
│   └── igbo_faq.json
├── scripts/
│   └── generate_dataset.py
├── app/
│   └── main.py               # Streamlit UI
│   └── chatbot.py            # Core chatbot logic
├── tests/
│   └── test_chatbot.py
├── README.md
├── requirements.txt
└── .myvenv/
```

---

## 🔧 Requirements

```txt
streamlit
requests
ollama
```

---

## 💬 Local Usage

1. Start Ollama:
   ```bash
   ollama run qwen:2.5
   ```

2. Run the chatbot UI:
   ```bash
   streamlit run app/main.py
   ```

---

## 🙌 Credits

This project was built with ❤️ for educational use, promoting **Indigenous Language AI** development using free and open-source tools.


👩‍💻 **Author:** Engr. Amarachi Omereife  
📧 **Email:** [amarachiomereife@gmail.com](mailto:amarachiomereife@gmail.com)  
📱 **Phone Number:** +2348068590823 *(WhatsApp/Telegram)*

---
