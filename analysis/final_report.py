import os
import re

# --- Configuration ---
SUMMARIES_DIR = 'summaries'
REPORT_FILE = 'final_workshop_report.md'
FOCUS_AREAS = {
    'Demystifying the agentic journey': ['agentic', 'journey', 'first steps', 'tangible value', 'enterprise buy-in'],
    'Strategizing for measurable wins': ['practical', 'low-risk', 'proof-of-concept', 'poc', 'quantifiable outcomes', 'measurable wins'],
    'Laying the groundwork for future autonomy': ['strategic building blocks', 'autonomous enterprise platform', 'future autonomy', 'scaling'],
    'AI/Agent Primitives': ['primitive', 'toolkit', 'workflows', 'deterministic', 'non-deterministic'],
}

def generate_report():
    report_content = '# Final Workshop Report\n\nThis report provides a synthesized and structured overview of the research findings, tailored for the \'Practical lessons from building an agentic-first developer platform\' workshop.\n\n'

    for area, keywords in FOCUS_AREAS.items():
        report_content += f'## {area}\n\n'
        for file_name in os.listdir(SUMMARIES_DIR):
            if file_name.endswith('.txt'):
                with open(os.path.join(SUMMARIES_DIR, file_name), 'r', encoding='utf-8') as f:
                    text = f.read()
                sentences = re.split('[.!?]', text)
                relevant_sentences = []
                for sentence in sentences:
                    if any(keyword in sentence.lower() for keyword in keywords):
                        relevant_sentences.append(sentence.strip())
                if relevant_sentences:
                    report_content += f'### From: {file_name.replace(".txt", "").replace("_", " ").title()}\n'
                    report_content += f'**Source:** `{file_name.replace(".txt", ".html")}`\n'
                    report_content += '> ' + ' '.join(relevant_sentences[:3]) + '\n\n'
        report_content += '\n---\n\n'

    report_content += '## Suggested Diagrams and Visual Aids\n\n'
    report_content += '- **The Agentic Journey:** A flowchart illustrating the transition from manual processes to a fully agentic platform, highlighting key milestones and decision points.\n'
    report_content += '- **The Agentic-First Platform:** A high-level architecture diagram showing the core components of an agentic-first platform, including the agent toolkit, workflow engine, and user interface.\n'
    report_content += '- **Deterministic vs. Non-Deterministic Workflows:** A side-by-side comparison of the two workflow types, with examples of each.\n'
    report_content += '- **The \'Golden Path\' for Agentic Workflows:** A visual representation of a \'golden path\' for a specific use case, such as a CI/CD pipeline or an incident response process.\n'

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print('Final report generated successfully.')

if __name__ == '__main__':
    # Change the working directory to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    generate_report()
