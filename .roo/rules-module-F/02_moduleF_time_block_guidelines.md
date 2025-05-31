# Module F: Time Block Guidelines

This document provides guidelines for scheduling time blocks within Module F's `Time_Architecture_Calendar.ics`.

## Scheduling Time Blocks
When asked to schedule a new time block, generate an iCal (`.ics`) event snippet.

## iCal Event Structure
- **SUMMARY**: The summary should clearly indicate the activity, e.g., "Time Block: Writing Session" or "Time Block: Deep Work".
- **DTSTART**: The start date and time of the time block (YYYYMMDDTHHMMSS).
- **DTEND**: The end date and time of the time block (YYYYMMDDTHHMMSS).
- **RRULE**: An optional recurrence rule for recurring blocks (e.g., `FREQ=DAILY`, `FREQ=WEEKLY`).

### Example: Daily Writing Session (Monday-Friday)
```
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:20250602T090000
DTEND:20250602T110000
RRULE:FREQ=DAILY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=9;BYMINUTE=0;BYSECOND=0
SUMMARY:Time Block: Writing Session
END:VEVENT
END:VCALENDAR
```

### Example: Weekly Planning Session
```
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:20250601T140000
DTEND:20250601T150000
RRULE:FREQ=WEEKLY;BYDAY=SU;BYHOUR=14;BYMINUTE=0;BYSECOND=0
SUMMARY:Time Block: Weekly Planning
END:VEVENT
END:VCALENDAR