# Module E: CSV Schema Guidelines

This document defines the schema for CSV files within Module E, specifically for `Target_Network_Map.csv` and `CRM_Contacts.csv`.

## 1. `Target_Network_Map.csv` Header
The `Target_Network_Map.csv` file must use the following header row:

```csv
Contact_ID,Name,Organization,Role,Arena_Relevance,Interaction_History,Notes,Follow_Up_Date,Strength
```

### Example Data Row
When adding a new row, ensure it follows this format:

```csv
CN-001,Jane Doe,Acme Corp,VP of Marketing,General,"Met at conference, 2025-02","High priority",2025-06-15,Tier 1
```

### Field Definitions
- `Contact_ID`: Unique identifier for the contact (e.g., CN-001).
- `Name`: Full name of the contact.
- `Organization`: The organization the contact belongs to.
- `Role`: The contact's role or title.
- `Arena_Relevance`: How relevant the contact is to your professional arena (e.g., General, Industry Leader, Mentor).
- `Interaction_History`: A brief log of past interactions.
- `Notes`: Any additional notes or reminders.
- `Follow_Up_Date`: The date for the next planned follow-up (YYYY-MM-DD).
- `Strength`: The strength of the relationship (e.g., Tier 1, Tier 2, Tier 3).

## 2. `CRM_Contacts.csv` Header
The `CRM_Contacts.csv` file must use the following header row:

```csv
Contact_ID,Name,Email,Phone,Organization,Tags
```

### Example Data Row
```csv
CN-002,John Smith,john.smith@example.com,555-123-4567,Example Corp,"Colleague, Project X"
```

### Field Definitions
- `Contact_ID`: Unique identifier for the contact (e.g., CN-002).
- `Name`: Full name of the contact.
- `Email`: Contact's email address.
- `Phone`: Contact's phone number.
- `Organization`: The organization the contact belongs to.
- `Tags`: Comma-separated tags for categorization (e.g., "Client", "Mentor", "Friend").