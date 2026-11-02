# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Microvascular Capillary Refill Time Perfusion Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentMicrovascularCapillaryRefillTimePerfusion

mcp = FastMCP("PersonalAgentMicrovascularCapillaryRefillTimePerfusion")
client = PersonalAgentMicrovascularCapillaryRefillTimePerfusion()

@mcp.tool()
def evaluate_capillary_refill_time(
    measured_crt_seconds: float = 1.8,
    ambient_temperature_celsius: float = 21.0,
    skin_site: str = "fingertip_index"
) -> str:
    """Calculates temperature-normalized Capillary Refill Time (CRT) and perfusion tier."""
    import json
    return json.dumps(client.evaluate_capillary_refill_time(
        measured_crt_seconds, ambient_temperature_celsius, skin_site
    ), indent=2)

@mcp.tool()
def calculate_peripheral_shock_index(
    systolic_bp: float = 120.0,
    heart_rate_bpm: float = 72.0,
    normalized_crt_seconds: float = 1.8
) -> str:
    """Calculates Shock Index (HR / SBP) and Combined Microvascular Shock Score (CMSS)."""
    import json
    return json.dumps(client.calculate_peripheral_shock_index(
        systolic_bp, heart_rate_bpm, normalized_crt_seconds
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
