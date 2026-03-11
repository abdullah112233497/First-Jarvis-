# First-Jarvis

A **basic voice-activated assistant** built in Python using **speech recognition**, **text-to-speech**, and **web automation**. This project demonstrates a simple version of a virtual assistant (like Jarvis) that can open websites and respond to voice commands.

> ⚠️ Note: This is a **beginner project**. It can be extended with more functionality like opening apps, telling time, or running Python scripts.

---

## Features

* **Voice activation:** Responds when you say “hello”
* **Website automation:** Open websites like Google and Facebook via voice commands
* **Text-to-speech feedback:** Jarvis speaks back confirmation
* **Simple Python modules:** Uses `speech_recognition`, `pyttsx3`, and `webbrowser`

---

## Tech Stack / Modules

* **Python 3.x**
* **speech_recognition** – Recognize voice commands
* **pyttsx3** – Text-to-speech engine
* **webbrowser** – Open websites automatically
* **time** – Pause execution between tasks

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/First-Jarvis.git
cd First-Jarvis
```

2. Install dependencies:

```bash
pip install SpeechRecognition pyttsx3
# If on Mac and you face pyobjc errors, run:
pip install pyobjc>=9.0.1
```

---

## How to Use

1. Run the Python script:

```bash
python first_jarvis.py
```

2. Speak “hello” to activate Jarvis.

3. After activation, you can say commands like:

   * `"google"` → Opens Google in your browser
   * `"facebook"` → Opens Facebook in your browser
   * `"exit"` → Exit the assistant

4. Jarvis will respond via voice using text-to-speech.

---

## Example Usage

```
User: hello
Jarvis: I am Activated...
User: google
Jarvis: Google open ho gya
User: facebook
Jarvis: Facebook open ho gya
User: exit
Jarvis exits
```

---

## Notes / Tips

* Make sure your **microphone is working** and allowed for Python
* Internet connection is required for `speech_recognition` to work
* You can extend this assistant by adding more commands, e.g., opening apps, telling time, or searching on YouTube

---

## Future Improvements

* Integrate **AI for smarter commands**
* Add **more website shortcuts**
* Include **system commands** (shutdown, open apps)
* Implement a **GUI interface**


