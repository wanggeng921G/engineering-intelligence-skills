---
name: ei-electronics-review
description: Review circuits, power stages, components, sensors, PCB, and EMC choices against exact documentation and operating margins.
---
# Electronics review

Establish schematic/board revision, supply ranges, loads, temperature, tolerances, transients, and operating modes. Check pin functions and ratings against exact manufacturer part/revision; keep absolute limits separate from operating limits. Recalculate consequential power, thermal, timing, noise, and tolerance budgets with units and worst-case assumptions.

Inspect startup/shutdown, fault/open/short cases, protection, return paths, layout-sensitive loops, test points, and measurement method. Label simulations and bench measurements accurately. For hazardous energy require a safe test plan and qualified review before energizing. Route firmware-controlled behavior through `ei-embedded-review` when it changes electrical risk.
