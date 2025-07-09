import re

# 📂 Load and read the resume file
def read_resume(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# 🧍 Extract name (simple pattern: line starting with Name:)
def extract_name(text):
    match = re.search(r'Name:\s*(.*)', text)
    return match.group(1).strip() if match else "Not found"

# 📧 Extract email address using standard regex
def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Not found"

# 📞 Extract phone number (Indian format or international format)
def extract_phone(text):
    match = re.search(r'(\+91[\-\s]?\d{10}|\d{10})', text)
    return match.group(0) if match else "Not found"

# 🧠 Extract skills from a fixed keyword set
def extract_skills(text, known_skills):
    found_skills = []
    for skill in known_skills:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
            found_skills.append(skill)
    return list(set(found_skills))

# 📚 Extract key section headers like Education, Experience
def extract_sections(text):
    sections = re.findall(r'^(Education|Experience|Certifications|Skills|Projects|Objective):', text, re.MULTILINE)
    return sections

# 🧾 Generate final report
def scan_resume(file_path):
    text = read_resume(file_path)

    known_skills = [
        "Python", "Machine Learning", "Data Science", "NLP", "Deep Learning",
        "Flask", "Django", "C++", "Java", "Data Structures", "SQL"
    ]

    report = {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills Found": extract_skills(text, known_skills),
        "Detected Sections": extract_sections(text)
    }

    # 📤 Print the results
    print("\n🧾 Resume Scan Report:")
    for k, v in report.items():
        print(f"🔹 {k}: {v}")

if __name__ == "__main__":
    scan_resume("resume.txt")
