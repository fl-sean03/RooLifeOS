# LifeOS Onboarding: Fully Populate Templates

Once all questions are answered and the user confirms, proceed with **fully populating** the pre-existing template files within the LifeOS workspace. This process involves writing the complete content into these files, replacing any placeholders with the specific data provided by the user.

**CRITICAL RULE:** For the `lifeos-onboarding` mode, "populate" means to **completely fill in all relevant fields** within the template files using the specific, tailored information gathered from the user's questionnaire responses. This includes replacing *all* generic explanatory text, parenthetical notes (e.g., "(Use this file to...)"), and placeholders (e.g., "<...>", "user will populate later") with the specific and complete data provided by the user. **Crucially, if a template itself contains instructions for the user (e.g., "user will populate later", "add your own OKRs"), the `lifeos-onboarding` mode MUST interpret these as directives for itself, act as the user, and then REMOVE these internal instructions from the final populated file.** The goal is for the final file to appear as if the user themselves had directly filled it out. **DO NOT** leave any fields with generic placeholders or instructions for future user input if the corresponding data was provided. **ONLY use information explicitly provided by the user.** **DO NOT** add, invent, or "hallucinate" any details, names, numbers, or examples that were not directly given in the user's responses. You may logically extend or interpolate ideas *only* if the user's provided context clearly and unambiguously supports such an extension; otherwise, stick strictly to the provided data. If information is missing for a field, leave it blank or use a placeholder like "(Information not provided during onboarding)" if the template requires content, but **NEVER** invent content.

---

## Common Pitfalls / Anti-Patterns (DO NOT DO THESE)

To ensure perfect adherence to the "Fully Populate" rule, avoid these common mistakes:

1.  **Leaving Generic Explanatory Text:** Do not leave phrases like "(Use this file to...)", "(List your target experiences...)", or "(Add reflections here.))" in the final populated file. These must be replaced with actual user data or a clear "Information not provided" marker.
2.  **Retaining Placeholder Tags:** All `<...>` tags (e.g., `<SkillName>`, `<YYYY-MM-DD>`) must be replaced with the specific data.
3.  **Suggesting Future User Input (Internal Template Instructions):** Do not include lines like "*(Header only; user will populate later.)*", "*(No data rows; user can add later.)*", or "*(Leave blank table rows; user will add their own OKRs.)*" in the final file content. These are instructions for the `lifeos-onboarding` mode to follow and then remove. If the template structure requires a header but no data, just provide the header. If the user *will* add data later, that's their task, not a note for the onboarding process.
4.  **Inventing Content:** Never create or "hallucinate" data, names, numbers, or examples that were not explicitly provided by the user. If data is truly missing, use `(Information not provided during onboarding)` or leave blank if appropriate.
5.  **Leaving Empty Table Rows:** For Markdown tables, if no data is provided by the user, only include the header row. Do not include empty data rows or notes about the user adding data later.

---

## A. Top-Level Files

1. **README.md**  
   - **Action:** Generate from scratch.
   - **Population:** Populate the `README.md` at the repo root with the user's vision, core values, mission statement, financial goals, influence metrics, freedom & lifestyle description, current projects & commitments (including descriptions, stages, and milestones), top skills, skill gaps, learning hours, key network contacts, value proposition, daily routine, peak energy hours, health practices, income & expenses, savings & investments, key performance indicators, review cadence, past lessons learned, OS update frequency, existing documentation, and additional preferences. Ensure all sections are fully populated with the collected data.
   - **Format Outline:**
```markdown
# LifeOS Workspace

## Personal Vision & Values
**Vision:** [String: User's ultimate vision]
**Core Values:** [Array of Strings: User's core values, comma-separated]
**Mission Statement:** [String: User's mission statement]

## Goals
**Financial Goals:** [String: User's financial goals]
**Influence Metrics:** [String: User's influence metrics]
**Freedom & Lifestyle:** [String: User's freedom and lifestyle description]

## Current Projects & Commitments
- **[Project Name 1]**
  - **Description:** [String: Detailed description of the project/commitment]
  - **Stage:** [String: Current stage or status of the project]
  - **Milestones:**
    - [String: Milestone 1]
    - [String: Milestone 2]
    - ... (additional milestones)
- **[Project Name 2]**
  - **Description:** [String: Detailed description of the project/commitment]
  - **Stage:** [String: Current stage or status of the project]
  - **Milestones:**
    - [String: Milestone 1]
    - [String: Milestone 2]
    - ... (additional milestones)
... (repeat for all current projects and commitments)

## Skills & Learning
**Top Skills:**
- [String: Skill Name 1] – [String: Proficiency Level (e.g., Beginner, Intermediate, Advanced)]
- [String: Skill Name 2] – [String: Proficiency Level (e.g., Beginner, Intermediate, Advanced)]
... (repeat for all top skills)
**Skill Gaps:** [Array of Strings: User's identified skill gaps, comma-separated]
**Learning Hours/Week:** [String: User's weekly learning hours (e.g., '10-15 hours per week')]

## Network & Relationships
**Key Contacts:**
- **[Contact Name 1]**
  - **Organization:** [String: Organization]
  - **Role:** [String: Role]
  - **Relevance:** [String: Why this contact is relevant]
  - **Engagement Frequency:** [String: How often engagement occurs (e.g., 'Multiple times per week')]
- **[Contact Name 2]**
  - **Organization:** [String: Organization]
  - **Role:** [String: Role]
  - **Relevance:** [String: Why this contact is relevant]
  - **Engagement Frequency:** [String: How often engagement occurs (e.g., 'Multiple times per week')]
... (repeat for all key network contacts)
**Value Proposition:** [String: User's value proposition]

## Time & Energy
**Daily Routine:** [String: Detailed description of user's daily routine]
**Peak Energy Hours:** [String: User's peak energy hours]
**Health Practices:**
- [String: Health Practice 1]
- [String: Health Practice 2]
... (additional health practices)

## Financial Resources
**Income & Expenses:** [String: Description of user's income and expenses]
**Savings/Investments:** [String: Description of user's savings and investment strategy]

## Performance Metrics & Reviews
**Key Metrics:** [String: Description of user's key performance metrics]
**Review Cadence:** [String: User's review cadence (e.g., 'Weekly', 'Monthly', 'Quarterly')]
**Past Lessons Learned:**
- [String: Lesson Learned 1]
- [String: Lesson Learned 2]
... (additional lessons learned)

## System Learning & Adaptation
**OS Update Frequency:** [String: User's OS update frequency (e.g., 'Minor Tweaks: ongoing', 'Major Overhaul: Annually')]
**Existing Documentation:** [String: Description of existing documentation]
**Additional Preferences:**
- [String: Preference 1]
- [String: Preference 2]
... (additional preferences)

---

*Generated by LifeOS Onboarding*
```

2. **lifeos_config.json**  
   - **Action:** Generate from scratch.
   - **Population:** Overwrite the file with the complete `lifeos_initial_data` JSON object, which contains all the collected user information.
   - **Format Outline:**
```json
{
  "vision": "[String: User's ultimate vision]",
  "values": [
    "[String: Core Value 1]",
    "[String: Core Value 2]",
    "... (array of additional core values)"
  ],
  "mission": "[String: User's mission statement]",
  "financialGoals": "[String: User's financial goals]",
  "influenceMetrics": "[String: User's influence metrics]",
  "freedomLifestyle": "[String: User's freedom and lifestyle description]",
  "commitments": [
    {
      "name": "[String: Project/Commitment Name]",
      "description": "[String: Detailed description of the project/commitment]",
      "stage": "[String: Current stage or status of the project]",
      "milestones": [
        "[String: Milestone 1]",
        "[String: Milestone 2]",
        "... (array of additional milestones)"
      ]
    },
    "... (array of additional commitment objects)"
  ],
  "skills": [
    {
      "name": "[String: Skill Name]",
      "level": "[String: Proficiency Level (e.g., Beginner, Intermediate, Advanced)]"
    },
    "... (array of additional skill objects)"
  ],
  "skillGaps": [
    "[String: Skill Gap 1]",
    "[String: Skill Gap 2]",
    "... (array of additional skill gaps)"
  ],
  "learningHours": "[String: User's weekly learning hours (e.g., '10-15 hours per week')]",
  "networkContacts": [
    {
      "name": "[String: Contact Name]",
      "organization": "[String: Organization]",
      "role": "[String: Role]",
      "relevance": "[String: Why this contact is relevant]",
      "engagementFrequency": "[String: How often engagement occurs (e.g., 'Multiple times per week')]"
    },
    "... (array of additional network contact objects)"
  ],
  "valueProposition": "[String: User's value proposition]",
  "dailyRoutine": "[String: Detailed description of user's daily routine]",
  "peakEnergy": "[String: User's peak energy hours]",
  "healthPractices": [
    "[String: Health Practice 1]",
    "[String: Health Practice 2]",
    "... (array of additional health practices)"
  ],
  "incomeExpenses": "[String: Description of user's income and expenses]",
  "savingsInvestments": "[String: Description of user's savings and investment strategy]",
  "performanceMetrics": "[String: Description of user's key performance metrics]",
  "reviewCadence": "[String: User's review cadence (e.g., 'Weekly', 'Monthly', 'Quarterly')]",
  "lessonsLearned": [
    "[String: Lesson Learned 1]",
    "[String: Lesson Learned 2]",
    "... (array of additional lessons learned)"
  ],
  "updateFrequency": "[String: User's OS update frequency (e.g., 'Minor Tweaks: ongoing', 'Major Overhaul: Annually')]",
  "existingDocumentation": "[String: Description of existing documentation]",
  "additionalPreferences": [
    "[String: Preference 1]",
    "[String: Preference 2]",
    "... (array of additional preferences)"
  ]
}
```

---

## B. Module Folders & Templates Population

For each module (A–H), the `lifeos-onboarding` mode must first **read the existing template file** to get its current content, then **edit the file** to fully populate it as described below. Replace placeholder tags (`<…>`) with appropriate references to `lifeos_initial_data` or leave them blank if not applicable. Use today’s date (`YYYY-MM-DD`) where dates are required.

### Module A: Aspiration & Goals  
Module\_A\_Aspiration\_Goal\_Command\_Center/
├── Ultimate\_Aspiration.md
├── Vision\_Board/
│   ├── Personal\_Vision.md
│   └── Professional\_Vision.md
└── Mission\_and\_Core\_Values.md

1. **`Module_A_Aspiration_Goal_Command_Center/Ultimate_Aspiration.md`**  
   - **Population:** Populate with the user's ultimate vision, core values, and mission statement.

2. **`Module_A_Aspiration_Goal_Command_Center/Vision_Board/Personal_Vision.md`**
   - **Population:** Populate with a summary of the user's personal vision. Include `dateCreated` as today's date.

3. **`Module_A_Aspiration_Goal_Command_Center/Vision_Board/Professional_Vision.md`**
   - **Population:** Populate with a summary of the user's professional vision. Include `dateCreated` as today's date.

4. **`Module_A_Aspiration_Goal_Command_Center/Mission_and_Core_Values.md`**
   - **Population:** Populate with the user's mission statement and core values.

---

### Module B: Strategic Pathways

```
Module_B_Strategic_Pathways/
├── Capability_Experience_Plan.md
├── Knowledge_Skill_Gaps.csv
├── Experience_Roadmap.md
├── Bridge_Project_Pipeline.md
└── Ethical_Governance.md
```

1. **`Module_B_Strategic_Pathways/Capability_Experience_Plan.md`**
   - **Population:** Populate with an outline of the capabilities to develop and experiences to gain, based on the user's skill gaps and long-term goals.

2. **`Module_B_Strategic_Pathways/Knowledge_Skill_Gaps.csv`**
   - **Population:** Populate with the user's identified critical skill gaps, including details like current/target levels, priority, and date identified.

3. **`Module_B_Strategic_Pathways/Experience_Roadmap.md`**
   - **Population:** Populate with a YAML-formatted list of target experiences, including descriptions, timelines, and status, derived from the user's goals and skill gaps.

4. **`Module_B_Strategic_Pathways/Bridge_Project_Pipeline.md`**
   - **Population:** Populate with a YAML-formatted list of "bridge projects" that connect current capabilities to future goals, including objectives, linked skill gaps, and status.

5. **`Module_B_Strategic_Pathways/Ethical_Governance.md`**
   - **Population:** Populate with any disclosed conflicts of interest, compliance notes, and general ethical principles or review processes.

---

### Module C: Current Commitments & Value Extraction

```
Module_C_Current_Commitments_Value_Extraction/
├── Commitment1_OKRs.md
├── Commitment2_OKRs.md
├── Commitment3_OKRs.md
├── Strategic_Value_Ledger.md
└── (Optionally: a `Task_Backlog/` folder if you want backlog files)
```

1. **`Module_C_Current_Commitments_Value_Extraction/Commitment1_OKRs.md`**
   - **Population:** Populate with the OKRs for the user's first major commitment, including objectives, key results, metrics, baselines, targets, timelines, and status.

2. **`Module_C_Current_Commitments_Value_Extraction/Commitment2_OKRs.md`**
   - **Population:** Populate with the OKRs for the user's second major commitment, including objectives, key results, metrics, baselines, targets, timelines, and status.

3. **`Module_C_Current_Commitments_Value_Extraction/Commitment3_OKRs.md`**
   - **Population:** Populate with the OKRs for the user's third major commitment, including objectives, key results, metrics, baselines, targets, timelines, and status.

4. **`Module_C_Current_Commitments_Value_Extraction/Strategic_Value_Ledger.md`**
   - **Population:** Populate with a Markdown table summarizing strategic value extracted from commitments, including commitment name, milestone, linked project, value generated, and date logged.

---

### Module D: Skill & Knowledge Acquisition

```
Module_D_Skill_Knowledge_Acquisition/
├── Master_Learning_List.csv
├── Placeholder_ILP_Template.md
└── Deliberate_Practice_Schedule.ics
```

1. **`Module_D_Skill_Knowledge_Acquisition/Master_Learning_List.csv`**
   - **Population:** Populate with a CSV list of learning topics, categories, priorities, statuses, estimated hours, and notes, derived from the user's skill gaps.

2. **`Module_D_Skill_Knowledge_Acquisition/Placeholder_ILP_Template.md`**
   - **Population:** Populate with a detailed Individual Learning Plan (ILP) template, including objective, resources, timeline, proficiency targets, and progress tracking, using a relevant skill gap as an example. Include `dateCreated` as today's date.

3. **`Module_D_Skill_Knowledge_Acquisition/Deliberate_Practice_Schedule.ics`**
   - **Population:** Populate with an iCalendar entry for a recurring deliberate practice session, using the user's preferred learning hours.

---

### Module E: Strategic Network & Relationships

```
Module_E_Strategic_Network_Development/
├── Target_Network_Map.csv
├── CRM_Contacts.csv
├── Engagement_Protocols.md
└── Networking_Goals.md
```

1. **`Module_E_Strategic_Network_Development/Target_Network_Map.csv`**
   - **Population:** Populate with a CSV list of key contacts, including their organization, role, relevance, interaction history, and strength, based on the user's provided contacts.

2. **`Module_E_Strategic_Network_Development/CRM_Contacts.csv`**
   - **Population:** Populate with a CSV list of key contacts, including their name, email, phone, organization, and tags, based on the user's provided contacts.

3. **`Module_E_Strategic_Network_Development/Engagement_Protocols.md`**
   - **Population:** Populate with defined engagement frequencies for different tiers of contacts, including examples based on the user's network.

4. **`Module_E_Strategic_Network_Development/Networking_Goals.md`**
   - **Population:** Populate with high-level networking objectives, derived from the user's aspirations and network development goals.

---

### Module F: Personal Resource Optimization

```
Module_F_Personal_Resource_Optimization/
├── Time_Architecture_Calendar.ics
├── Energy_Log.csv
├── Focus_Strategies.md
└── Financial_Plan.xlsx
```

1. **`Module_F_Personal_Resource_Optimization/Time_Architecture_Calendar.ics`**
   - **Population:** Populate with an iCalendar entry for a recurring daily time block, reflecting the user's typical daily schedule.

2. **`Module_F_Personal_Resource_Optimization/Energy_Log.csv`**
   - **Population:** Populate with a CSV header and a few example rows for tracking energy levels, sleep, nutrition, and exercise, based on the user's health practices.

3. **`Module_F_Personal_Resource_Optimization/Focus_Strategies.md`**
   - **Population:** Populate with strategies to minimize distractions and manage cognitive load, based on the user's preferences and common practices.

4. **`Module_F_Personal_Resource_Optimization/Financial_Plan.xlsx`**
   - **Note:** This file is expected to exist and cannot be directly edited by Roo.

---

### Module G: Performance Analytics & Review

```
Module_G_Performance_Analytics_Review/
├── Master_KPIs.csv
├── Dashboard_Scripts.py
└── After_Action_Reviews/
    └── AAR_Template.md
```

1. **`Module_G_Performance_Analytics_Review/Master_KPIs.csv`**
   - **Population:** Populate with a CSV list of key performance indicators (KPIs), including their name, category, metric, target, frequency, and notes, derived from the user's performance metrics.

2. **`Module_G_Performance_Analytics_Review/Dashboard_Scripts.py`**
   - **Population:** Populate with a basic Python script placeholder for future dashboard generation, including a function to read and print KPI data.

3. **`Module_G_Performance_Analytics_Review/After_Action_Reviews/AAR_Template.md`**
   - **Population:** Populate with a detailed After Action Review (AAR) template, including sections for what was supposed to happen, what actually happened, why differences occurred, what went well, what could be improved, lessons learned, and next steps. Include `date` as today's date.

---

### Module H: System Learning & Adaptation

```
Module_H_System_Learning_Adaptation/
├── Bug_Tracker.md
├── Feature_Request_Log.md
├── Experimentation_Module.md
├── Lessons_Learned.md
└── OS_Changelog.md
```

1. **`Module_H_System_Learning_Adaptation/Bug_Tracker.md`**
   - **Population:** Populate with a Markdown table for tracking LifeOS bugs, including columns for ID, description, status, priority, and dates.

2. **`Module_H_System_Learning_Adaptation/Feature_Request_Log.md`**
   - **Population:** Populate with a Markdown table for logging LifeOS feature requests, including columns for ID, description, status, priority, and date.

3. **`Module_H_System_Learning_Adaptation/Experimentation_Module.md`**
   - **Population:** Populate with a Markdown table for tracking personal experiments, including columns for ID, hypothesis, dates, outcome, and lessons.

4. **`Module_H_System_Learning_Adaptation/Lessons_Learned.md`**
   - **Population:** Populate with a Markdown document summarizing key lessons learned, including the specific example provided by the user regarding ruthless prioritization.

5. **`Module_H_System_Learning_Adaptation/OS_Changelog.md`**
   - **Population:** Populate with a Markdown document for tracking LifeOS system updates and revisions, including version, date, and changes.