# Module H: OS Changelog Guidelines

This document provides guidelines for maintaining `OS_Changelog.md` within Module H.

## Changelog Structure
The `OS_Changelog.md` file should start with an initial version heading and bullet points, and then be updated incrementally.

```markdown
# OS Changelog

## v1.0 – YYYY-MM-DD
- Initial scaffolding of Modules A–H via LifeOS Onboarding.
```

## Updating the Changelog
For each subsequent update to the LifeOS system, increment the version number (`v<major>.<minor>`) and add new bullet points describing the changes.

### Example Update
```markdown
## v1.1 – 2025-06-01
- Added new feature: Automated KPI dashboard generation in Module G.
- Fixed bug: YAML parsing error in Module B's Bridge Project Pipeline.
- Improved onboarding flow with clearer instructions.
```

## Best Practices
- **Date**: Always include the date of the update (YYYY-MM-DD).
- **Conciseness**: Keep bullet points concise and to the point.
- **Categorization**: Optionally, categorize changes (e.g., "Features", "Bug Fixes", "Improvements").
- **Chronological Order**: Newest versions should appear at the top of the changelog.