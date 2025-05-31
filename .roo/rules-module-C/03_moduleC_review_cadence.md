# Module C: Review Cadence Guidelines

This document provides guidelines for scheduling periodic reviews related to Module C's content (commitments, OKRs, strategic value ledger).

## Scheduling Reviews
When asked to schedule a review, generate an iCal (`.ics`) event snippet.

## iCal Event Structure
- **SUMMARY**: The summary should clearly indicate the purpose of the review, e.g., "Module C OKR Review" or "Module C Value Ledger Review".
- **RRULE**: Use an appropriate recurrence rule (e.g., `FREQ=MONTHLY` for monthly check-ins, `FREQ=QUARTERLY` for quarterly reviews).

### Example: Monthly OKR Review
```
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:20250701T080000
RRULE:FREQ=MONTHLY;BYDAY=MO;BYSETPOS=1;BYHOUR=8;BYMINUTE=0;BYSECOND=0
SUMMARY:Module C OKR Review
END:VEVENT
END:VCALENDAR
```

### Example: Quarterly Value Ledger Review
```
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:20250930T140000
RRULE:FREQ=QUARTERLY;BYMONTH=3,6,9,12;BYMONTHDAY=30;BYHOUR=14;BYMINUTE=0;BYSECOND=0
SUMMARY:Module C Quarterly Value Ledger Review
END:VEVENT
END:VCALENDAR