# Module B: Bridge Project Pipeline YAML Schema

This document defines the YAML schema for `Bridge_Project_Pipeline.md`.

## YAML Structure
The `Bridge_Project_Pipeline.md` file should contain a YAML list of bridge projects, each following this schema:

```yaml
- id: BP-###
  name: "<Project Name>"
  objective: "<Brief objective>"
  linked_gap: SKG-###
  status: <Proposed|In Progress|Completed>
  owner: "<UserName>"
```

## Field Definitions
- `id`: A unique identifier for the bridge project (e.g., `BP-001`).
- `name`: The name of the project.
- `objective`: A brief description of the project's objective.
- `linked_gap`: The `Gap_ID` from `Knowledge_Skill_Gaps.csv` that this project helps address. This field is crucial for linking projects to skill development.
- `status`: The current status of the project. Allowed values are `Proposed`, `In Progress`, or `Completed`.
- `owner`: The person responsible for the project.

## Example Entry
```yaml
- id: BP-001
  name: "Develop a Machine Learning Model"
  objective: "Build a predictive model for customer churn using Python and scikit-learn."
  linked_gap: SKG-005
  status: In Progress
  owner: "Sean Florez"