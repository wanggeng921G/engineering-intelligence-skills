---
name: ei-system-architecture-review
description: Review cross-component architecture, interfaces, failure propagation, resource budgets, and trade-offs.
---
# System architecture review

Start with required capabilities, quality attributes, context, ownership boundaries, and existing architecture. Trace major data/control flows and recovery. Check interface contracts, versioning, single points of failure, capacity/timing budgets, observability, security boundaries, and rollback.

Compare credible options under the same constraints. Expose the strongest counterargument and decision-changing unknown. Avoid a diagram or layer solely for style. For lasting decisions use `ei-evidence-map` and record the decision and rationale. Add domain reviews only where details affect the choice.
