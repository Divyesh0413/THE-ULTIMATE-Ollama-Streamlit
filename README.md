# 🤖 THE ULTIMATE — Ollama + Streamlit AI Chatbot

**THE ULTIMATE** is a simple AI chatbot built using **Python, Streamlit, and Ollama**.

It allows users to enter a question and receive an AI-generated response using the locally running **Qwen 2.5 0.5B** model.

## ✨ Features

* 🤖 Simple AI chatbot interface
* 💬 User question input
* 🚀 One-click AI response
* ⚡ Fast and lightweight
* 🖥️ Runs locally using Ollama
* 🎨 Clean Streamlit interface

## 🛠️ Technologies Used

* Python
* Streamlit
* Ollama
* Qwen 2.5 0.5B


## 📸 Project Screenshot

![THE ULTIMATE Screenshot](Screenshots/first%20impression.png)

## ⚙️ Installation

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and running, then download the required model:

```bash
ollama pull qwen2.5:0.5b
```

## ▶️ Run the Project

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔄 How It Works

```text
User enters a question
        ↓
Streamlit receives the question
        ↓
Ollama sends the question to Qwen 2.5 0.5B
        ↓
AI generates a response
        ↓
Streamlit displays the response
```

## 📁 Project Structure

```text
THE-ULTIMATE-Ollama-Streamlit/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .gitattributes
│
└── screenshots/
    └── app.png
```

## 🚀 Future Improvements

* 🌐 Deploy the application online
* 💬 Chat history
* 🧠 Conversation memory
* 🤖 Multiple Ollama model selection
* ⚡ Streaming responses
* 🗑️ Clear chat button
* 🎨 Improved user interface

## 👨‍💻 Author

**Divyesh Tiwari**

B.Tech — Artificial Intelligence & Data Science
