import re

def clean_text(text):
    # Lowercase and remove special characters
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def get_sentences(text):
    # Split based on '.', '?', '!' marks
    return [sentence.strip() for sentence in re.split(r'[.!?]', text) if sentence.strip()]

def get_words(text):
    return set(clean_text(text).split())

def check_plagiarism(file1, file2):
    # Read files
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        text1 = f1.read()
        text2 = f2.read()

    # Compare sentences
    sentences1 = set(get_sentences(text1))
    sentences2 = set(get_sentences(text2))
    common_sentences = sentences1.intersection(sentences2)

    # Compare words
    words1 = get_words(text1)
    words2 = get_words(text2)
    common_words = words1.intersection(words2)

    # Sentence-level plagiarism
    sentence_score = (len(common_sentences) / max(len(sentences1), 1)) * 100

    # Word-level plagiarism
    word_score = (len(common_words) / max(len(words1), 1)) * 100

    print("🧾 Plagiarism Report:")
    print(f"🔸 Sentence Similarity: {sentence_score:.2f}%")
    print(f"🔸 Word Similarity: {word_score:.2f}%")
    print(f"🔍 Common Sentences Found: {len(common_sentences)}")

    if common_sentences:
        print("\n👀 Sample Common Sentences:")
        for sent in list(common_sentences)[:3]:
            print("•", sent)

if __name__ == "__main__":
    file1 = "file1.txt"
    file2 = "file2.txt"
    check_plagiarism(file1, file2)
