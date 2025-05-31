# Module A: Review Cadence Guidelines

This document provides guidelines for scheduling periodic reviews related to Module A's content (aspirations, vision, mission, values).

## Scheduling Reviews
When asked to schedule a review, generate an iCal (`.ics`) event snippet.

## iCal Event Structure
- **SUMMARY**: The summary should clearly indicate the purpose of the review, e.g., "Module A Aspiration Review" or "Module A Mission & Values Review".
- **RRULE**: Use an appropriate recurrence rule (e.g., `FREQ=YEARLY` for annual reviews, `FREQ=QUARTERLY` for quarterly reviews).

### Example: Annual Aspiration Review
```
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:20250101T090000
RRULE:FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0;BYSECOND=0
SUMMARY:Module A Annual Aspiration Review
END:VEVENT
END:VCALENDAR
```

### Example: Quarterly Mission & Values Review
```
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:20250331T100000
RRULE:FREQ=QUARTERLY;BYMONTH=3,6,9,12;BYMONTHDAY=31;BYHOUR=10;BYMINUTE=0;BYSECOND=0
SUMMARY:Module A Quarterly Mission & Values Review
END:VEVENT
END:VCALENDAR