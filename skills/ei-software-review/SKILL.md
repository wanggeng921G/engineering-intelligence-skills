---
name: ei-software-review
description: Review application, API, service, web, and data changes for correctness, security, compatibility, and tests.
---
# Software review

Map user-visible behavior and relevant callers before editing. Check input validation, authorization, data handling, failure paths, concurrency, migration/rollback, accessibility where relevant, dependency/API versions, and realistic load. Prioritize defects with a concrete failure path.

Use existing tests and deployment conventions. Verify changed behavior with a focused test or run and report what actually ran. Avoid adding a dependency or architecture layer for a small fix. If AI output is part of the product, also use `ei-ai-system-review`.
