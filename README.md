# 🧠 Reddit Persona Generator

This project analyzes Reddit user profiles and generates detailed personas using their posts and comments. It combines web scraping with Natural Language Processing (NLP) to understand interests, sentiments, and behavior.

---

## 🔍 Why It’s Valuable

- **Automation**: Scrapes Reddit using the Reddit API (`PRAW`)
- **AI/NLP**: Uses `spaCy`, `transformers`, and `TextBlob` to understand text
- **Insight Generation**: Outputs structured summaries, keywords, and sentiment scores
- **HealthTech Adaptability**: This tool can be adapted to analyze **health forums**, **patient reviews**, or **feedback from diagnostic platforms**, helping healthcare organizations:
  - Track patient satisfaction
  - Understand trending symptoms or lab test demand
  - Improve customer experience

---

## 🛠️ Tech Stack

- Python
- Reddit API (via `PRAW`)
- NLP Libraries: spaCy, transformers, TextBlob
- Data Processing: Pandas
- Visualization: Matplotlib, WordCloud
- Notebook interface: Jupyter

---

## 📂 Features

- Fetch Reddit posts/comments for any username
- Perform:
  - Sentiment analysis
  - Keyword extraction
  - Behavioral summary
- Generate persona report with visual charts

---

## ▶️ How to Run

```bash
git clone https://github.com/Shambhawikumari/reddit-persona-generator.git
cd reddit-persona-generator
pip install -r requirements.txt
