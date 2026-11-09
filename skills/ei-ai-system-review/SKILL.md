---
name: ei-ai-system-review
description: Review LLM agents, RAG, prompts, tools, and evaluations for evidence quality, security boundaries, and measured performance.
---
# AI system review

Define task, users, ground truth or rubric, cost/latency limits, and failure severity. Trace retrieval freshness and provenance; inspect prompt injection surfaces, tool permissions, data leakage, and untrusted output handling. Keep execution authority in application controls.

Use representative ordinary, adversarial, and abstention cases. Report dataset, model/version/config, metric definition, observed results, and limits. A demo is not evidence of reliability at scale. For production integration also use `ei-software-review`; for multi-component choices use `ei-system-architecture-review`.
