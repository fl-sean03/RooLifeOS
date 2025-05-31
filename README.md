# RooLifeOS

This repository implements **LifeOS**, a generic personal “operating system” framework designed to help users manage their aspirations, goals, commitments, skills, network, resources, and overall system adaptation. LifeOS is organized into eight core modules (A–H) and two special modes: `lifeos-onboarding` and `lifeos-orchestrator`.

## How to Use RooLifeOS

Getting started with RooLifeOS is straightforward:

1.  **Clone the Repository:** Begin by cloning this repository into your local environment. All necessary configurations for Roo (the `.roo` and `.roomodes` directories) are already set up within the project.

    ```bash
    git clone https://github.com/fl-sean03/RooLifeOS.git
    cd RooLifeOS
    ```

2.  **Initial Setup with Onboarding:** Once cloned, switch to the `lifeos-onboarding` mode. This guided assistant will walk you through a questionnaire to gather your personal vision, values, goals, and other foundational information. Upon completion, it will automatically populate all the scaffolded documents across the various modules (A-H) with your provided details.

3.  **Day-to-Day Operations with Orchestrator:** After the onboarding process is complete, switch to the `lifeos-orchestrator` mode. This mode acts as your central command center for all daily interactions with LifeOS. You can issue natural-language commands, and the Orchestrator will intelligently delegate tasks to the appropriate modules, manage updates, and provide you with clear feedback and necessary `git` commands to persist your changes.

## Core Modules Overview


LifeOS is composed of the following modules:

- **Module A: Aspiration & Goal Command Center**
  - Captures and reviews your ultimate vision, mission, and core values.
  - Manages files like `Ultimate_Aspiration.md`, `Vision_Board/*.md`, and `Mission_and_Core_Values.md`.

- **Module B: Strategic Pathways**
  - Maps skill gaps, defines experiences, and tracks “bridge projects.”
  - Manages files like `Capability_Experience_Plan.md`, `Knowledge_Skill_Gaps.csv`, `Experience_Roadmap.md`, `Bridge_Project_Pipeline.md`, and `Ethical_Governance.md`.

- **Module C: Current Commitments & Value Extraction**
  - Manages ongoing commitments (OKRs), tracks strategic value outputs, and links to bridge projects.
  - Manages files like `Commitment_OKRs.md` and `Strategic_Value_Ledger.md`.

- **Module D: Skill & Knowledge Acquisition Engine**
  - Maintains a master learning list, scaffolds Individual Learning Plans (ILPs), and schedules deliberate practice.
  - Manages files like `Master_Learning_List.csv` and `ILP_<SkillName>.md`.

- **Module E: Strategic Network & Relationships**
  - Builds a network map, manages CRM contacts, defines engagement protocols, and sets networking goals.
  - Manages files like `Target_Network_Map.csv`, `CRM_Contacts.csv`, and `Engagement_Protocols.md`.

- **Module F: Personal Resource Optimization Engine**
  - Optimizes time (calendar), energy (sleep/food/exercise), focus (cognitive load), and financial resources (budgeting).
  - Manages files like `Energy_Log.csv`, `Time_Architecture_Calendar.ics`, `Focus_Strategies.md`, and `Financial_Plan.xlsx`.

- **Module G: Performance Analytics & Review**
  - Stores Master KPIs, generates dashboards, runs After Action Reviews (AARs), and schedules periodic reviews.
  - Manages files like `Master_KPIs.csv`, `Dashboard_Scripts.py`, and `AAR_Templates/`.

- **Module H: System Learning & Adaptation**
  - Tracks system bugs, feature requests, experiments, lessons learned, and maintains an OS changelog.
  - Manages files like `Bug_Tracker.md`, `Feature_Request_Log.md`, `Experimentation_Module.md`, `Lessons_Learned.md`, and `OS_Changelog.md`.

## Special Modes

- **✨ LifeOS Onboarding (`lifeos-onboarding`)**
  - A guided setup assistant that asks a series of structured questions to gather user data (vision, values, commitments, goals, skills, network, resources, preferences).
  - Iteratively populates pre-existing scaffolded files within each module (A–H) with the collected data, and creates a top-level `README.md` and `lifeos_config.json`.

- **🚀 LifeOS Orchestrator (`lifeos-orchestrator`)**
  - The single front-end Roo mode for all day-to-day LifeOS operations.
  - Identifies which module(s) a user's natural-language request relates to, decomposes the request into subtasks, and dispatches them to the corresponding `module-X` mode.
  - Aggregates outputs from modules and provides clear instructions, diffs, and `git` commands for persisting changes.

## Interaction with the Workspace

To interact with this workspace, use the appropriate mode: `lifeos-onboarding`, `lifeos-orchestrator`, or `module-A` through `module-H`. Each module’s folder and file structure is defined under `Module_*/`.