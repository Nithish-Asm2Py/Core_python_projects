# 🧾 Python Plagiarism Checker

This project is a simple **text similarity checker** using Python — built as part of my learning journey toward becoming an **AI Engineer**.  
It compares two text files and calculates how similar they are at both the sentence and word level.

---

## 🎯 Why This Project?

As I build up from core Python to more advanced topics like NLP and ML, this project helps me practice:

- Text cleaning & preprocessing
- File I/O in Python
- Regex (`re` module)
- Basic natural language handling (without libraries)

---

## 🚀 Features

- ✅ Compare any two `.txt` files
- 🔍 Detect common sentences and words
- 📊 Show word & sentence similarity percentage
- 👀 Displays up to 3 matched sentences

---

## 🛠️ Tech Stack

- **Python 3**
- Built-in `re` (Regex) module
- No external libraries or frameworks

---

## 📂 How It Works

1. Reads the content of `file1.txt` and `file2.txt`
2. Cleans text: lowercases and removes special characters
3. Splits content into sentences and words
4. Compares both sets to find intersections
5. Prints a clear similarity report

---

## 📦 Usage

### 🔹 1. Clone the Repository

git clone https://github.com/yourusername/plagiarism-checker.git
cd plagiarism-checker

### 🔹 2. Add Your Text Files
Ensure the following files are present:

file1.txt
file2.txt
These should contain the text content you want to compare.

### 🔹 3. Run the Script

python3 plagiarism_checker.py

### sample output:
🧾 Plagiarism Report:
🔸 Sentence Similarity: 83.33%
🔸 Word Similarity: 91.25%
🔍 Common Sentences Found: 5

👀 Sample Common Sentences:
• machine learning is a subfield of ai
• python is widely used in ai projects
• text processing is key in nlp

🧾 Plagiarism Report:
🔸 Sentence Similarity: 83.33%
🔸 Word Similarity: 91.25%
🔍 Common Sentences Found: 5

👀 Sample Common Sentences:
• machine learning is a subfield of ai
• python is widely used in ai projects
• text processing is key in nlp

# 🔮 Future Improvements
Once I move further in my AI roadmap, I plan to:

Add NLP tokenization (using nltk or spaCy)

Use cosine similarity or TF-IDF

Accept .docx or .pdf files

Create a web version with Flask

Auto-generate detailed PDF reports


# 🪪 License
MIT License — use freely and improve it!

🙋‍♂️ Author
Nithish Kumar
Documenting my journey to AI Engineering through hands-on Python projects.