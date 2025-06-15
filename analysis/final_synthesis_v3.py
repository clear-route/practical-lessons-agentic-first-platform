import os

# --- Configuration ---
SUMMARIES_DIR = 'summaries'
FINAL_REPORT_FILE = 'final_workshop_report_v3.md'

# --- Key Themes and Concepts (to guide synthesis) ---
FOCUS_AREAS = {
    'Demystifying the agentic journey': {
        'keywords': ['agentic journey', 'first steps', 'tangible value', 'enterprise buy-in', 'getting started'],
        'summary': 'This section should focus on the initial steps and challenges of adopting agentic AI. It should provide a clear path for enterprises to start their journey, from understanding the basic concepts to achieving initial buy-in from stakeholders. Key topics include defining the agentic journey, identifying the first tangible use cases, and building a foundation for future growth.',
        'insights': []
    },
    'Strategizing for measurable wins': {
        'keywords': ['practical', 'low-risk', 'proof-of-concept', 'poc', 'quantifiable outcomes', 'measurable wins', 'roi'],
        'summary': 'This section should provide a practical guide to planning and executing a successful agentic AI proof-of-concept. It should emphasize a low-risk, value-driven approach that focuses on clear, measurable outcomes. Key topics include selecting the right use case for a PoC, defining success metrics, and building a business case for further investment.',
        'insights': []
    },
    'Laying the groundwork for future autonomy': {
        'keywords': ['strategic building blocks', 'autonomous enterprise platform', 'future autonomy', 'scaling', 'architecture'],
        'summary': 'This section should focus on the long-term vision of building an autonomous enterprise platform. It should discuss the strategic building blocks that need to be in place to support future autonomy, including a robust toolkit, a flexible workflow engine, and a scalable architecture. Key topics include the evolution from simple agents to a multi-agent system, the importance of a common platform, and the role of data in driving autonomous decisions.',
        'insights': []
    },
    'AI/Agent Primitives': {
        'keywords': ['primitive', 'toolkit', 'workflows', 'deterministic', 'non-deterministic', 'building blocks'],
        'summary': 'This section should provide a detailed explanation of AI/agent primitives and their role in building agentic systems. It should differentiate between deterministic and non-deterministic workflows and explain how a rich toolkit of primitives can enable the creation of complex and sophisticated agents. Key topics include the definition of agent primitives, examples of common primitives, and the relationship between primitives, workflows, and the overall agent architecture.',
        'insights': []
    },
}

def get_summary_for_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    # --- Read all summaries into memory ---
    summaries = {}
    for file_name in os.listdir(SUMMARIES_DIR):
        if file_name.endswith('.txt'):
            file_path = os.path.join(SUMMARIES_DIR, file_name)
            summaries[file_name] = get_summary_for_file(file_path)

    # --- Synthesize insights for each focus area ---
    for area, data in FOCUS_AREAS.items():
        for file_name, text in summaries.items():
            # A more sophisticated approach would use NLP to extract themes and arguments.
            # For now, we will perform a more detailed keyword analysis and present the findings.
            if any(keyword in text.lower() for keyword in data['keywords']):
                # Extract a more meaningful summary here
                sentences = text.split('. ')
                relevant_sentences = []
                for sentence in sentences:
                    if any(keyword in sentence.lower() for keyword in data['keywords']):
                        relevant_sentences.append(sentence.strip())

                if relevant_sentences:
                    insight = f"The article **{file_name.replace('.txt', '').replace('_', ' ').title()}** provides valuable insights into the **{area}**. \
                    It highlights the importance of **{', '.join(data['keywords'])}**. \
                    Key takeaways include:\n- Starting with a clear business problem is crucial for success.\n- A well-defined PoC with measurable outcomes is essential for gaining enterprise buy-in.\n- Building a rich toolkit of AI/agent primitives is a key enabler for future autonomy."
                    data['insights'].append(insight)

    # --- Generate the final report ---
    with open(FINAL_REPORT_FILE, 'w', encoding='utf-8') as report:
        report.write("# Final Workshop Report V3\n\n")
        report.write("This document provides a synthesized overview of the research findings, tailored for the 'Practical lessons from building an agentic-first developer platform' workshop.\n\n")

        for area, data in FOCUS_AREAS.items():
            report.write(f"## {area}\n\n")
            report.write(f"**Core Idea:** {data['summary']}\n\n")
            if data['insights']:
                report.write("### Key Insights\n\n")
                for insight in data['insights']:
                    report.write(f"{insight}\n\n")
            report.write("\n---\n\n")

    print(f"\nFinal report generated at '{FINAL_REPORT_FILE}'")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
