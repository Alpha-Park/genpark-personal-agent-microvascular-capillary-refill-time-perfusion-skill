# Personal Agent Microvascular Capillary Refill Time Perfusion Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Capillary Refill Time (CRT) thermal normalization modeler, peripheral vasomotor tone indexer, and microvascular shock index calculator.

## Architecture

```mermaid
flowchart TD
    BlanchInput[Measured CRT Seconds & Ambient Temperature C] --> CRTEngine[Anderson Thermal Normalization Modeler]
    CRTEngine --> ThermalCorrection[Offset: +0.06s per C Below 20 C]
    ThermalCorrection --> NormalizedCRT[Normalized Capillary Refill Time Seconds]
    NormalizedCRT --> AndromedaShock[ANDROMEDA-SHOCK Perfusion Tiers: <= 2.0s Prompt vs > 3.0s Delayed]
    MacroHemodynamics[Systolic BP & Heart Rate bpm] --> ShockEngine[Combined Microvascular Shock Modeler]
    ShockEngine --> ShockIndex[Classical Shock Index: HR / SBP]
    ShockIndex & NormalizedCRT --> CMSSScore[Combined Microvascular Shock Score: CMSS]
```

## Quickstart

```python
from client import PersonalAgentMicrovascularCapillaryRefillTimePerfusion

agent = PersonalAgentMicrovascularCapillaryRefillTimePerfusion()
res = agent.evaluate_capillary_refill_time(measured_crt_seconds=2.2, ambient_temperature_celsius=16.0)
print(f"Normalized CRT: {res['normalized_capillary_refill_time_seconds']} s | Tier: {res['microvascular_perfusion_tier']}")
```
