import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# --- Download NLTK data (if not already downloaded) ---
try:
    stopwords.words('english')
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('tokenizers/punkt_tab')
except (LookupError, OSError):
    print("Downloading NLTK data...")
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('punkt_tab')

# --- Configuration ---
SUMMARIES_DIR = 'analysis/summaries'
REPORT_FILE = 'analysis/enhanced_workshop_report.md'
FOCUS_AREAS = {
    'Demystifying the agentic journey': ['agentic', 'journey', 'first steps', 'tangible value', 'enterprise buy-in'],
    'Strategizing for measurable wins': ['practical', 'low-risk', 'proof-of-concept', 'poc', 'quantifiable outcomes', 'measurable wins'],
    'Laying the groundwork for future autonomy': ['strategic building blocks', 'autonomous enterprise platform', 'future autonomy', 'scaling'],
    'AI/Agent Primitives': ['primitive', 'toolkit', 'workflows', 'deterministic', 'non-deterministic'],
}

# --- Helper Functions ---
def get_top_sentences(text, keywords, num_sentences=5):
    """Extracts the most relevant sentences based on keyword matching."""
    sentences = sent_tokenize(text)
    sentence_scores = {sentence: 0 for sentence in sentences}

    for sentence in sentences:
        for keyword in keywords:
            if re.search(r'\b' + keyword + r'\b', sentence, re.IGNORECASE):
                sentence_scores[sentence] += 1
    
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(top_sentences)

# --- Main Execution ---
def main():
    """Orchestrates the enhanced synthesis and reporting of research findings."""

    print(f"Starting enhanced synthesis of summaries in '{SUMMARIES_DIR}'...")

    try:
        summary_files = [f for f in os.listdir(SUMMARIES_DIR) if f.endswith('.txt')]
    except FileNotFoundError:
        print(f"Error: Summaries directory '{SUMMARIES_DIR}' not found.")
        return

    if not summary_files:
        print(f"No summary files found in '{SUMMARIES_DIR}'.")
        return

    with open(REPORT_FILE, 'w', encoding='utf-8') as report:
        report.write("# Enhanced Workshop Research Report\n\n")
        report.write("This report provides a detailed analysis of the research findings, structured around the key focus areas of the workshop.\n\n")

        for area, keywords in FOCUS_AREAS.items():
            report.write(f"## {area}\n\n")
            
            for file_name in summary_files:
                input_path = os.path.join(SUMMARIES_DIR, file_name)
                
                with open(input_path, 'r', encoding='utf-8') as f:
                    full_text = f.read()

                # Extract relevant sentences for the focus area
                relevant_summary = get_top_sentences(full_text, keywords)

                if relevant_summary:
                    article_title = os.path.splitext(file_name)[0].replace('_', ' ').title()
                    report.write(f"### From: {article_title}\n")
                    report.write(f"**Source:** `{file_name.replace('.txt', '.html')}`\n")
                    report.write(f"> {relevant_summary}\n\n")

            report.write("\n---\n\n")

    print(f"\nEnhanced synthesis complete. Report generated at '{REPORT_FILE}'")

if __name__ == "__main__":
    main()
