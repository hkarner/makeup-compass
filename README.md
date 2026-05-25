# 🧭 Makeup Compass

A free, privacy-first makeup profiling app. Answer 7 questions about your features and get a personalized guide covering brows, eyes, lips, base, undereye correction, and shopping strategy.

No specific products are recommended — descriptions focus on format, finish, and shade direction so the guide stays useful regardless of what's on shelves.

**Live app:** [makeup-compass.streamlit.app](https://makeup-compass.streamlit.app) *(update after deploy)*

---

## How it works

1. User answers 7 questions: skin depth, undertone, eye shape, contrast, lip type, coverage preference, dark circles
2. `logic.py` dispatches each answer to the appropriate rule module
3. Results are rendered as expandable sections in Streamlit
4. User can download their guide as a `.txt` file

**No data is collected or stored.** The app has no database; all logic is static.

---

## Local setup
pip install streamlit

streamlit run [app.py](http://app.py)

```

Or with conda:

```

conda create -n makeup python=3.11 -y

conda activate makeup

pip install streamlit

streamlit run [app.py](http://app.py)

```

---

## File structure

```

makeup_quiz/

├── [app.py](http://app.py)

├── [logic.py](http://logic.py)

├── rules/

│   ├── **init**.py

│   ├── [brows.py](http://brows.py)

│   ├── [eyes.py](http://eyes.py)

│   ├── [lips.py](http://lips.py)

│   ├── [base.py](http://base.py)

│   ├── [undereye.py](http://undereye.py)

│   └── [store.py](http://store.py)

├── requirements.txt

└── [README.md](http://README.md)

```

---

## Deploy (Streamlit Cloud)

1. Push to a public GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io), connect the repo, set main file to `app.py`
3. Deploy — live in ~2 minutes
```