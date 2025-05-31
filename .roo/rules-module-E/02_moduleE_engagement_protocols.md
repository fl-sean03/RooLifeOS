# Module E: Engagement Protocols

This document defines guidelines for engaging with contacts in your network, categorized by tiers.

## Engagement Frequency Guidelines
Define how often to follow up with contacts at different levels. For example:

```markdown
- Tier 1 Contacts: Weekly check-ins (e.g., Mondays at 10 AM).
- Tier 2 Contacts: Monthly check-ins (e.g., first Friday at 11 AM).
- Tier 3 Contacts: Quarterly (15th day at 3 PM).
- Tier 4 Contacts: Semi-annually (June 1, December 1 at 4 PM).
```

## Scheduling Follow-ups
When asked to schedule a networking follow-up, generate an iCal (`.ics`) event snippet.

### iCal Event Structure
- **SUMMARY**: The summary should clearly indicate the contact and purpose, e.g., "Module E Follow-Up: <ContactName>".
- **DTSTART**: The start date and time of the follow-up (YYYYMMDDTHHMMSS).
- **RRULE**: An appropriate recurrence rule (e.g., `FREQ=MONTHLY`, `FREQ=QUARTERLY`).

### Example: Monthly Follow-Up with Jane Doe
```
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:20250704T110000
RRULE:FREQ=MONTHLY;BYDAY=FR;BYSETPOS=1;BYHOUR=11;BYMINUTE=0;BYSECOND=0
SUMMARY:Module E Follow-Up: Jane Doe
END:VEVENT
END:VCALENDAR