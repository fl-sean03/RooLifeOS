# Module D: Deliberate Practice Schedule Guidelines

This document provides guidelines for scheduling "Deliberate Practice" sessions within Module D.

## Scheduling Practice Sessions
When asked to schedule a deliberate practice session, generate an iCal (`.ics`) event snippet.

## iCal Event Structure
- **SUMMARY**: The summary should clearly indicate the skill being practiced, e.g., "Deliberate Practice – <SkillName>".
- **DTSTART**: The start date and time of the practice session (YYYYMMDDTHHMMSS).
- **RRULE**: An appropriate recurrence rule (e.g., `FREQ=WEEKLY` for weekly sessions, `FREQ=DAILY` for daily sessions, with `COUNT` for a specific number of occurrences).

### Example: Weekly Deliberate Practice for "Data Visualization"
```
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:20250605T070000
RRULE:FREQ=WEEKLY;COUNT=8;BYDAY=MO;BYHOUR=7;BYMINUTE=0;BYSECOND=0
SUMMARY:Deliberate Practice – Data Visualization
END:VEVENT
END:VCALENDAR
```

### Example: Daily Deliberate Practice for "Public Speaking" (for 30 days)
```
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:20250601T180000
RRULE:FREQ=DAILY;COUNT=30;BYHOUR=18;BYMINUTE=0;BYSECOND=0
SUMMARY:Deliberate Practice – Public Speaking
END:VEVENT
END:VCALENDAR