import os

# --- Configuration ---
SUMMARIES_DIR = 'summaries'
SYNTHESIS_FILE = 'synthesis_for_workshop.md'

# --- Key Themes and Concepts (to guide synthesis) ---
FOCUS_AREAS = {
    'Demystifying the agentic journey': {
        'keywords': ['agentic journey', 'first steps', 'tangible value', 'enterprise buy-in', 'getting started'],
        'summary': 'This section should focus on the initial steps and challenges of adopting agentic AI. It should provide a clear path for enterprises to start their journey, from understanding the basic concepts to achieving initial buy-in from stakeholders. Key topics include defining the agentic journey, identifying the first tangible use cases, and building a foundation for future growth.'
    },
    'Strategizing for measurable wins': {
        'keywords': ['practical', 'low-risk', 'proof-of-concept', 'poc', 'quantifiable outcomes', 'measurable wins', 'roi'],
        'summary': 'This section should provide a practical guide to planning and executing a successful agentic AI proof-of-concept. It should emphasize a low-risk, value-driven approach that focuses on clear, measurable outcomes. Key topics include selecting the right use case for a PoC, defining success metrics, and building a business case for further investment.'
    },
    'Laying the groundwork for future autonomy': {
        'keywords': ['strategic building blocks', 'autonomous enterprise platform', 'future autonomy', 'scaling', 'architecture'],
        'summary': 'This section should focus on the long-term vision of building an autonomous enterprise platform. It should discuss the strategic building blocks that need to be in place to support future autonomy, including a robust toolkit, a flexible workflow engine, and a scalable architecture. Key topics include the evolution from simple agents to a multi-agent system, the importance of a common platform, and the role of data in driving autonomous decisions.'
    },
    'AI/Agent Primitives': {
        'keywords': ['primitive', 'toolkit', 'workflows', 'deterministic', 'non-deterministic', 'building blocks'],
        'summary': 'This section should provide a detailed explanation of AI/agent primitives and their role in building agentic systems. It should differentiate between deterministic and non-deterministic workflows and explain how a rich toolkit of primitives can enable the creation of complex and sophisticated agents. Key topics include the definition of agent primitives, examples of common primitives, and the relationship between primitives, workflows, and the overall agent architecture.'
    },
}

# --- Main Execution ---
def main():
    """Orchestrates the final synthesis and reporting of research findings."""

    print(f"Starting final synthesis of summaries in '{SUMMARIES_DIR}'...")

    # --- Read all summaries into memory ---
    summaries = {}
    for file_name in os.listdir(SUMMARIES_DIR):
        if file_name.endswith('.txt'):
            with open(os.path.join(SUMMARIES_DIR, file_name), 'r', encoding='utf-8') as f:
                summaries[file_name] = f.read()

    # --- Generate the final synthesis ---
    with open(SYNTHESIS_FILE, 'w', encoding='utf-8') as report:
        report.write("# Synthesis for Workshop\n\n")
        report.write("This document provides a synthesized overview of the research findings, tailored for the 'Practical lessons from building an agentic-first developer platform' workshop.\n\n")

        for area, data in FOCUS_AREAS.items():
            report.write(f"## {area}\n\n")
            report.write(f"**Core Idea:** {data['summary']}\n\n")

            # --- Synthesize insights from all articles for this focus area ---
            for file_name, text in summaries.items():
                # A more sophisticated approach would use NLP for summarization and topic modeling.
                # For now, we'll extract keywords and present them.
                words = text.lower().split()
                keywords_in_article = [word.strip('.,!?:;()[]{}') for word in words if word in data['keywords']]
                
                if keywords_in_article:
                    article_title = os.path.splitext(file_name)[0].replace('_', ' ').title()
                    report.write(f"### Insights from: {article_title}\n")
                    report.write(f"- **Relevant Keywords:** {', '.join(set(keywords_in_article))}\n")
                    # In a real scenario, this is where you'd add a synthesized summary of the article's contribution to the focus area.
                    report.write("- **Key Takeaway:** (Placeholder for synthesized takeaway)\n\n")

            report.write("\n---\n\n")

    print(f"\nFinal synthesis complete. Report generated at '{SYNTHESIS_FILE}'")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
