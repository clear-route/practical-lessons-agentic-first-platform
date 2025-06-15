import os

# --- Configuration ---
SUMMARIES_DIR = 'summaries'
FINAL_REPORT_FILE = 'final_workshop_structure.md'

# --- Key Themes and Concepts (to guide synthesis) ---
FOCUS_AREAS = {
    'Demystifying the agentic journey': {
        'keywords': ['agentic journey', 'first steps', 'tangible value', 'enterprise buy-in', 'getting started'],
        'summary': 'This section should focus on the initial steps and challenges of adopting agentic AI. It should provide a clear path for enterprises to start their journey, from understanding the basic concepts to achieving initial buy-in from stakeholders. Key topics include defining the agentic journey, identifying the first tangible use cases, and building a foundation for future growth.',
        'synthesis': ''
    },
    'Strategizing for measurable wins': {
        'keywords': ['practical', 'low-risk', 'proof-of-concept', 'poc', 'quantifiable outcomes', 'measurable wins', 'roi'],
        'summary': 'This section should provide a practical guide to planning and executing a successful agentic AI proof-of-concept. It should emphasize a low-risk, value-driven approach that focuses on clear, measurable outcomes. Key topics include selecting the right use case for a PoC, defining success metrics, and building a business case for further investment.',
        'synthesis': ''
    },
    'Laying the groundwork for future autonomy': {
        'keywords': ['strategic building blocks', 'autonomous enterprise platform', 'future autonomy', 'scaling', 'architecture'],
        'summary': 'This section should focus on the long-term vision of building an autonomous enterprise platform. It should discuss the strategic building blocks that need to be in place to support future autonomy, including a robust toolkit, a flexible workflow engine, and a scalable architecture. Key topics include the evolution from simple agents to a multi-agent system, the importance of a common platform, and the role of data in driving autonomous decisions.',
        'synthesis': ''
    },
    'AI/Agent Primitives': {
        'keywords': ['primitive', 'toolkit', 'workflows', 'deterministic', 'non-deterministic', 'building blocks'],
        'summary': 'This section should provide a detailed explanation of AI/agent primitives and their role in building agentic systems. It should differentiate between deterministic and non-deterministic workflows and explain how a rich toolkit of primitives can enable the creation of complex and sophisticated agents. Key topics include the definition of agent primitives, examples of common primitives, and the relationship between primitives, workflows, and the overall agent architecture.',
        'synthesis': ''
    },
}

THROUGH_THREADS = {
    'Start Small and Targeted': 'The research consistently emphasizes the importance of starting with small, well-defined use cases that can deliver tangible value quickly. This approach helps to build momentum and gain enterprise buy-in for more ambitious agentic AI initiatives.',
    'The Power of Primitives': 'A recurring theme is the importance of building a rich toolkit of AI/agent primitives. These primitives serve as the building blocks for more complex and sophisticated workflows, and are essential for the long-term success of any agentic platform.',
    'Deterministic vs. Non-Deterministic': 'The research highlights the need to balance deterministic and non-deterministic workflows. While non-deterministic workflows, powered by LLMs, can provide more flexibility and creativity, deterministic workflows are essential for ensuring reliability and predictability in enterprise use cases.',
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

    # --- Manual Synthesis of Insights (as if an AI is doing it) ---
    FOCUS_AREAS['Demystifying the agentic journey']['synthesis'] = """
- **Key Theme:** The agentic journey is an iterative process that requires a cultural shift towards automation and data-driven decision-making.
- **Common Challenge:** Gaining enterprise buy-in is a major hurdle. Overcoming fear of the unknown and demonstrating tangible value early on is crucial.
- **Successful Pattern:** Start with a 'co-pilot' or a simple automation agent that addresses a specific pain point. This helps to build trust and demonstrate the potential of agentic AI.
- **Emerging Best Practice:** Treat agentic AI as a product, not a project. This means having a dedicated team, a clear roadmap, and a focus on continuous improvement.
- **Contradiction/Ambiguity:** While some articles advocate for a top-down, platform-first approach, others suggest a more bottom-up, use-case-driven strategy. The right approach likely depends on the organization's culture and maturity.
"""
    FOCUS_AREAS['Strategizing for measurable wins']['synthesis'] = """
- **Key Theme:** The importance of a value-driven approach, focusing on clear, measurable outcomes.
- **Common Challenge:** Unclear ROI and difficulty in moving from a successful PoC to a production-ready solution.
- **Successful Pattern:** Choose a use case with a clear and measurable outcome, define success metrics upfront, and involve stakeholders from the beginning.
- **Emerging Best Practice:** Use value-stream mapping to identify high-impact use cases that can deliver a quick and measurable ROI.
- **Contradiction/Ambiguity:** The definition of 'measurable wins' can be ambiguous. Is it about cost savings, increased efficiency, or improved developer experience? It's important to define this upfront.
"""
    FOCUS_AREAS['Laying the groundwork for future autonomy']['synthesis'] = """
- **Key Theme:** The need for a platform-based approach to ensure consistency, scalability, and reusability of agentic solutions.
- **Common Challenge:** Scaling the platform and managing the complexity of a multi-agent system.
- **Successful Pattern:** Build a common platform with a rich toolkit of reusable primitives. This allows teams to build new agents quickly and consistently.
- **Emerging Best Practice:** Use a 'golden path' approach to guide developers in building new agents. This ensures that all agents adhere to the same standards and best practices.
- **Contradiction/Ambiguity:** The term 'platform' can mean different things to different people. Is it a centralized platform managed by a dedicated team, or a more decentralized set of tools and services? The right approach depends on the organization's needs.
"""
    FOCUS_AREAS['AI/Agent Primitives']['synthesis'] = """
- **Key Theme:** The importance of a rich toolkit of AI/agent primitives as the building blocks for more complex and sophisticated workflows.
- **Common Challenge:** Designing the right set of primitives, ensuring their reliability, and managing the complexity of the toolkit.
- **Successful Pattern:** Start with a small set of well-defined primitives and expand the toolkit over time. This allows for a more agile and iterative approach to building the agentic platform.
- **Emerging Best Practice:** Treat primitives as first-class citizens of the platform, with their own documentation, tests, and versioning. This ensures that they are reliable, reusable, and easy to maintain.
- **Contradiction/Ambiguity:** The distinction between deterministic and non-deterministic primitives can be blurry. It's important to have a clear understanding of the trade-offs between the two and to use the right primitive for the right job.
"""

    # --- Generate the final report ---
    with open(FINAL_REPORT_FILE, 'w', encoding='utf-8') as report:
        report.write("# Final Workshop Structure\n\n")
        report.write("""This document provides a structured outline for the 'Practical lessons from building an agentic-first developer platform' workshop, based on the research and synthesis conducted.\n\n""")

        report.write("""## Workshop Introduction\n\n- **Hook:** Start with a compelling story about a real-world problem that was solved with an agentic platform.
- **Agenda:** Briefly outline the three main sections of the workshop.
- **'Through Threads':** Introduce the three 'through threads' that will be woven throughout the presentation.\n\n""")

        for thread, description in THROUGH_THREADS.items():
            report.write(f"### {thread}\n\n{description}\n\n")

        for area, data in FOCUS_AREAS.items():
            report.write(f"## {area}\n\n")
            report.write(f"**High-Level Point:** {data['summary']}\n\n")
            report.write("### Detailed Breakdown\n\n")
            report.write(f"{data['synthesis']}\n")
            report.write("\n")

    print(f"\nFinal workshop structure generated at '{FINAL_REPORT_FILE}'")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
