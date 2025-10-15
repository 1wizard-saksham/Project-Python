# 🧠 Voice-Controlled Desktop Assistant (with OpenAI, News, and Weather Integration)

### 🎙 Overview  
This Python project is a **voice-activated desktop assistant** that listens to your speech and performs smart actions — such as opening websites, playing music, fetching news, reporting weather, or chatting using **OpenAI’s GPT model**.  

It combines **speech recognition**, **API integrations**, and **OpenAI’s conversational power** to act as an all-in-one personal AI helper.

---

## 🚀 Features  

- 🎤 **Voice Commands** — Speak naturally, and the assistant will recognize your request using Google’s speech-to-text.  
- 💬 **Conversational Chatbot** — Uses **GPT-4o-mini** to respond intelligently to anything you say.  
- 🌦 **Weather Reports** — Fetches real-time weather data for any city via the **Open-Meteo API** and has GPT summarize it nicely.  
- 📰 **News Headlines** — Displays the latest trending news using the **NewsAPI** (currently Bitcoin-related by default, but easily customizable).  
- 🎵 **Music Playback** — Opens a local MP3 file or your preferred media when you say “Open music.”  
- 🌐 **Website Access** — Instantly opens sites like YouTube, Google, or Wikipedia by voice.  
- 🕒 **Time Updates** — Speaks the current time when you ask for it.  

---

## ⚙️ Technologies Used  

| Category | Technology |
|-----------|-------------|
| Voice Recognition | `speech_recognition` |
| Text-to-Speech | macOS `say` command |
| Language Model | `openai` (GPT-4o-mini) |
| News Feed | `newsapi-python` |
| Weather | `open-meteo` API |
| Misc | `requests`, `datetime`, `os`, `webbrowser` |

---

## 🧩 How It Works  

1. The assistant listens through your microphone using **SpeechRecognition**.  
2. Recognized text is matched against known commands (like “open YouTube” or “weather in Delhi”).  
3. Depending on the command:  
   - It may open a website  
   - Play music  
   - Fetch the weather or news  
   - Or chat with you through **OpenAI’s API**  
4. Voice feedback is given via macOS’s `say` function.  

---

## 🔑 Setup Instructions  

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/voice-desktop-assistant.git
   cd voice-desktop-assistant
