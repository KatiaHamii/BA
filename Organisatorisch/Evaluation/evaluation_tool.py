import PyPDF2
import os
import re

def compare_text_with_words(text, words):
    found_words = {}
    for word in words:
        #pattern = rf"\b{re.escape(word)}\w*\b"
        #matches = re.findall(pattern, text, re.IGNORECASE)
        #count = len(matches)
        count = text.count(word)
        if count > 0:
            found_words[word] = count
    return found_words

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text.lower()

def read_words_from_txt(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return [word.lower() for word in words]


def main():
    # Read the words from the TXT file
    words = read_words_from_txt('Konzepte.txt')

    # Extract text from the PDF file
    pdf_text = extract_text_from_pdf(
        'NaturkatastrophenWirbelstürme,Beben,Vulkanausbrüche.pdf')

    # Compare the text with the words and count occurrences
    found_words = compare_text_with_words(pdf_text, words)

    sorted_words = sorted(found_words.items(), key=lambda x: x[1], reverse=True)

    # Print the found words and their occurrences
    if sorted_words:
        print("The following words were found in the PDF (sorted by frequency):")
        for word, count in sorted_words:
            print(f"{word}: {count} occurrences")
    else:
        print("No words were found in the PDF.")

    print("Found in Document:", len(sorted_words))

    with open('results_Wirbelstürme,Beben,Vulkanausbrüche_evaluation.txt', 'w') as file:
        file.write("Word\tOccurrences\n")
        for word, count in sorted_words:
            file.write(f"{word}\t{count}\n")
        print(f"Results written results_Wirbelstürme,Beben,Vulkanausbrüche.txt")


cwd = os.getcwd()
print("Current working directory:", cwd)


if __name__ == '__main__':
    main()
