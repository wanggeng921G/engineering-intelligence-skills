---
name: ei-embedded-review
description: Review MCU firmware, drivers, RTOS, interrupts, DMA, boot, and update behavior with hardware-specific evidence.
---
# Embedded review

Identify exact MCU/SoC, silicon and board revisions, toolchain, SDK/HAL/RTOS versions, clock, memory, peripherals, and timing constraints. Read applicable reference manual, datasheet, errata, and repository configuration before asserting peripheral behavior.

Review shared-resource ownership, ISR/task boundaries, DMA/cache where applicable, bounds/timeouts, reset/watchdog paths, persistent formats, update recovery, and fault-safe outputs. Verify with build/static analysis and target measurements for hardware behavior; host tests alone do not establish target behavior. For STM32 C use existing MISRA-oriented project skills if available; do not claim compliance or add medical process rules without explicit scope.
