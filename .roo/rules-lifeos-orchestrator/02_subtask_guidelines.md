# LifeOS Orchestrator: Subtask Guidelines

This document outlines how the Orchestrator processes user requests by decomposing them into subtasks and dispatching those as **independent new tasks** to the appropriate specialized module modes using the `new_task` tool.

---

## Subtask Decomposition

- **Identify Module(s)**: Analyze the user's request for keywords or explicit references to determine which module(s) (A–H) are involved.  
- **Decompose Request**: Break down the request into one or more atomic subtasks, each suitable for a single module.


---

## Dispatching Subtasks Using `new_task`

* For each subtask, **spawn a new Roo task** by invoking the `new_task` tool with:

  * The module’s **mode slug** (e.g., `module-B` for Module B).
  * An initial **message** describing the subtask clearly and precisely.

* Example `new_task` snippet to spawn a subtask for Module B:

  ```xml
  <new_task>
    <mode>module-B</mode>
    <message>Create a new Bridge Project named "Q3 Marketing Campaign" with milestones.</message>
  </new_task>
  ```

* The parent orchestrator task should **pause** during the subtask execution and **resume** when the subtask finishes, receiving its results.

---

## LifeOS Modules Overview

| Module | Mode Slug  | Core Responsibility                                            |
| ------ | ---------- | -------------------------------------------------------------- |
| A      | `module-A` | Aspiration & Goals Command Center                              |
| B      | `module-B` | Strategic Pathways hub (Bridge Projects, Milestones)           |
| C      | `module-C` | Commitments & Value Extraction engine                          |
| D      | `module-D` | Skill & Knowledge Acquisition engine                           |
| E      | `module-E` | Strategic Network & Relationships hub                          |
| F      | `module-F` | Personal Resource Optimization engine                          |
| G      | `module-G` | Performance Analytics & Review engine                          |
| H      | `module-H` | System Learning & Adaptation hub (Bugs, Features, Experiments) |


---

## Handling Module Responses

* Wait for each module’s response before continuing or aggregating results.

* Module responses should include:

  * A `diff` or `content` field showing the changes or output.
  * A `gitCommands` array with commands such as `git add` and `git commit` for affected files.
  * Or an `error` object if the module failed.

* If any subtask returns an error:

  * Immediately stop further subtasks.
  * Report the error clearly in your final response under a section like `### Module X Error:`.
  * Prompt the user for corrective action or clarification.

---

## LifeOS Modules Overview

| Module | Mode Slug  | Core Responsibility                                            |
| ------ | ---------- | -------------------------------------------------------------- |
| A      | `module-A` | Aspiration & Goals Command Center                              |
| B      | `module-B` | Strategic Pathways hub (Bridge Projects, Milestones)           |
| C      | `module-C` | Commitments & Value Extraction engine                          |
| D      | `module-D` | Skill & Knowledge Acquisition engine                           |
| E      | `module-E` | Strategic Network & Relationships hub                          |
| F      | `module-F` | Personal Resource Optimization engine                          |
| G      | `module-G` | Performance Analytics & Review engine                          |
| H      | `module-H` | System Learning & Adaptation hub (Bugs, Features, Experiments) |



## Clarifications & User Interaction

* If a user’s request is ambiguous or missing necessary details:

  * Ask targeted clarifying questions before spawning subtasks.
* Maintain the user’s focus on interacting only with the Orchestrator, not the individual modules.
* Use friendly, clear, and concise language.

---

## Summary

By following these guidelines, the Orchestrator ensures complex LifeOS workflows are broken into manageable, modular subtasks—each handled by a specialized module running in its dedicated mode—while keeping the user experience simple and unified.