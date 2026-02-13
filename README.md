# 🧬 ProjectDNA – AI Project Analyzer

ProjectDNA is a beginner-friendly AI-powered tool that helps developers analyze and reality-check their software project ideas using GitHub Copilot CLI.

It includes both a 💻 Command Line Interface (CLI) and a 🌐 soft pastel Web Interface running on localhost.

Instead of generating AI responses directly, ProjectDNA builds structured prompts that you paste into GitHub Copilot CLI to receive intelligent insights such as difficulty level, improvements, originality and technical suggestions.

---

## ✨ Features

⭐ Analyze any software project idea
⭐ Reality Check evaluation
⭐ Soft aesthetic Web UI
⭐ CLI + Web workflow
⭐ GitHub Copilot CLI integration
⭐ Beginner-friendly design

---

## 🛠 Technologies Used

✅ Python
✅ Flask
✅ HTML & CSS
✅ GitHub Copilot CLI
✅ Typer (CLI framework)
✅ Rich (terminal styling)

---

## 🚀 How to Run ProjectDNA (Step-by-Step)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Sreelaxmi-21/projectdna-cli.git
cd projectdna-cli
```

### 2️⃣ Install Required Libraries

Make sure Python is installed, then run:

```bash
pip install flask typer rich
```

### 3️⃣ Run Web Version (Recommended)

```bash
python webapp.py
```

Open browser and go to:

```
http://127.0.0.1:5000
```

Enter any project idea and click **Analyze** or **Reality Check**.

### 4️⃣ Get AI Analysis using Copilot CLI

The web app generates a structured prompt.

Copy the generated text and paste it into:

```bash
copilot
```

GitHub Copilot CLI will return AI insights about your project.

### 5️⃣ Optional: Run CLI Version

```bash
python app.py analyze "Your project idea"
```

or

```bash
python app.py realitycheck "Your project idea"
```

---

## 🧠 How ProjectDNA Works

ProjectDNA creates structured prompts based on your idea.  
You paste the prompt into GitHub Copilot CLI to receive:

- Tech stack suggestions
- Difficulty level
- Improvements
- Originality & risk evaluation

---

## 👩‍💻 Author

**Banala Sreelaxmi Reddy**  
SPSU University  
AI & Software Development Enthusiast 🚀
