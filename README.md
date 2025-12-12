# EchoMind – Personality-Aware Companion AI with Adaptive Memory

EchoMind is a modular companion AI system that extracts meaningful user memory from conversations and adapts its response tone using a personality engine.

This project was built as part of the **GuppShupp – Founding AI Engineer Assignment**.

---

## 🚀 Features

### 🧠 Memory Extraction Module
Given a set of user chat messages, the system automatically identifies and extracts:
- **User Preferences** (likes, dislikes, communication style)
- **User Emotional Patterns** (stress, anxiety, motivation)
- **Facts Worth Remembering** (education, goals, personal context)

The output is returned in a structured **JSON format** suitable for long-term memory storage in companion AI systems.

---

### 🎭 Personality Engine
The personality engine dynamically transforms a base AI response into different tones:
- **Calm Mentor**
- **Witty Friend**
- **Therapist-Style**

This enables emotionally aware and context-sensitive AI interactions.

---

### 🔁 Before / After Personality Comparison
The same base reply produces different responses depending on the selected personality, clearly demonstrating tone transformation.

---

## 🧩 System Architecture
User / Reviewer
|
v
FastAPI Backend
├── Memory Extraction Module
├── Personality Engine
└── REST APIs
