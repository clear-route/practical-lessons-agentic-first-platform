import os

# --- Configuration ---
SUMMARIES_DIR = 'analysis/summaries'
REPORT_FILE = 'analysis/workshop_research_report.md'

# --- Main Execution ---
def main():
    """Orchestrates the synthesis and reporting of the research findings."""

    print(f"Starting synthesis of summaries in '{SUMMARIES_DIR}'...")

    # Find all text files in the summaries directory
    try:
        summary_files = [f for f in os.listdir(SUMMARIES_DIR) if f.endswith('.txt')]
    except FileNotFoundError:
        print(f"Error: Summaries directory '{SUMMARIES_DIR}' not found.")
        return

    if not summary_files:
        print(f"No summary files found in '{SUMMARIES_DIR}'.")
        return

    # Process each summary file and generate a report
    with open(REPORT_FILE, 'w', encoding='utf-8') as report:
        report.write("# Workshop Research Report\n\n")
        report.write("This report summarizes the key findings from the research conducted for the 'Practical lessons from building an agentic-first developer platform' workshop.\n\n")

        for file_name in summary_files:
            input_path = os.path.join(SUMMARIES_DIR, file_name)
            article_title = os.path.splitext(file_name)[0].replace('_', ' ').title()

            print(f"  - Synthesizing '{file_name}'...")

            try:
                with open(input_path, 'r', encoding='utf-8') as f:
                    summary_text = f.read()

                # --- Basic Analysis (Keyword Extraction) ---
                # A more sophisticated approach would use NLP libraries like NLTK or spaCy
                words = summary_text.lower().split()
                keywords = [
                    word.strip('.,!?:;()[]{}') for word in words 
                    if len(word) > 4 and word.isalpha()
                ]
                keyword_counts = {kw: keywords.count(kw) for kw in set(keywords)}
                top_keywords = sorted(keyword_counts.items(), key=lambda item: item[1], reverse=True)[:5]

                # --- Reporting ---
                report.write(f"## {article_title}\n\n")
                report.write("### Key Information\n\n")
                report.write(f"- **Source:** `{file_name.replace('.txt', '.html')}`\n")
                report.write(f"- **Top Keywords:** {', '.join([kw for kw, count in top_keywords])}\n\n")
                report.write("### Summary\n\n")
                report.write(f"```text\n{summary_text[:1000]}...\n```\n\n")

                print(f"    - Successfully synthesized and added to report.")

            except Exception as e:
                print(f"    - Error processing '{file_name}': {e}")

    print(f"\nSynthesis complete. Report generated at '{REPORT_FILE}'")

if __name__ == "__main__":
    main()
