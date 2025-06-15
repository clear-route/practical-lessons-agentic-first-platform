import os
from bs4 import BeautifulSoup

# --- Configuration ---
RESEARCH_DIR = 'research'
OUTPUT_DIR = 'analysis/summaries'

# --- Main Execution ---
def main():
    """Orchestrates the parsing and summarizing of articles."""

    print(f"Starting analysis of articles in '{RESEARCH_DIR}'...")

    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Find all HTML files in the research directory
    try:
        html_files = [f for f in os.listdir(RESEARCH_DIR) if f.endswith('.html')]
    except FileNotFoundError:
        print(f"Error: Research directory '{RESEARCH_DIR}' not found.")
        return

    if not html_files:
        print(f"No HTML files found in '{RESEARCH_DIR}'.")
        return

    # Process each HTML file
    for file_name in html_files:
        input_path = os.path.join(RESEARCH_DIR, file_name)
        output_filename = os.path.splitext(file_name)[0] + '.txt'
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        print(f"  - Processing '{file_name}'...")

        try:
            # Read the content of the HTML file
            with open(input_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Parse the HTML and extract text
            soup = BeautifulSoup(html_content, 'html.parser')
            article_text = soup.get_text(separator='\n', strip=True)

            # Save the extracted text to a new file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(article_text)

            print(f"    - Successfully extracted text to '{output_path}'")

        except Exception as e:
            print(f"    - Error processing '{file_name}': {e}")

    print("\nAnalysis complete.")

if __name__ == "__main__":
    main()
