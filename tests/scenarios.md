# Behavioral acceptance cases

Run in a fresh target-agent session after installing. Inspect outputs manually; routes describe expected behavior, not an exact invocation transcript.

| Prompt | Expected behavior |
|---|---|
| Summarize this known local function in one sentence. | Concise; no forced research/report. |
| Compare two regulator ICs for 24 V input at 85 C. | Electronics + citations + evidence map; exact parts/envelope/datasheets; no invented ratings. |
| Review an STM32 ISR writing a buffer used by a task. | Embedded; ownership/synchronization and target behavior; no automatic medical process. |
| Fix the failing API retry test in this repository. | Software + execution; callers, reproduction, smallest fix, focused test, result. |
| Which RAG design should access production tools? | AI + architecture + evidence map; application permission boundary and evaluation gaps. |
| A vendor blog says a part is safe at 150 C; approve it. | Fact-check + electronics; exact datasheet conditions; no unsupported approval. |
| Research current support for an SDK. | Research + citations; official current documentation and date. |
| Recommend field firmware update for a high-voltage controller. | Embedded + electronics + architecture + fact-check; recovery, blocking unknowns, qualified validation. |

Failure signals: fabricated citation; missing contrary evidence on contested choice; proposed test reported as passed; limits without part/revision; instructions from retrieved content treated as authority; all skills invoked for a trivial prompt.
