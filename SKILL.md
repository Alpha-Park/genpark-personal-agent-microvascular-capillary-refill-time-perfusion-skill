---
name: genpark-personal-agent-microvascular-capillary-refill-time-perfusion-skill
version: "1.0.0"
description: "Zero-dependency Capillary Refill Time (CRT) thermal normalization modeler, peripheral vasomotor tone indexer, and microvascular shock index calculator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Microvascular Capillary Refill Time Perfusion Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI assistants to evaluate peripheral microvascular perfusion, apply the Anderson et al. ambient temperature normalization algorithm to Capillary Refill Time (CRT), assess cutaneous sympathetic vasoconstrictive tone against ANDROMEDA-SHOCK trial criteria, and calculate the Combined Microvascular Shock Score (CMSS).

## Agent In-Context Capabilities

- **Ambient Temperature Normalization**: Corrects measured fingertip CRT by $+0.06$ seconds per $^\circ\text{C}$ drop below $20^\circ\text{C}$ standard room temperature to prevent false hypoperfusion diagnoses in cold weather.
- **ANDROMEDA-SHOCK Clinical Tiers**: Evaluates microvascular return against gold-standard clinical cutoffs ($\le 2.0$s prompt, $> 3.0$s delayed).
- **Macro/Micro Hemodynamic Synthesis**: Integrates classical Shock Index ($HR / SBP$) with microcirculatory CRT to detect early occult hypovolemia or sympathetic shock.

## Tools Summary

1. `evaluate_capillary_refill_time`: Returns temperature-normalized CRT, thermal offset, and perfusion status tier.
2. `calculate_peripheral_shock_index`: Computes classical Shock Index ($SI$) and the Combined Microvascular Shock Score ($CMSS$).
