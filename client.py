# -*- coding: utf-8 -*-
"""Personal Agent Microvascular Capillary Refill Time Perfusion Skill.

Zero-dependency Capillary Refill Time (CRT) thermal normalization modeler,
peripheral vasomotor tone indexer, and microvascular shock index calculator.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentMicrovascularCapillaryRefillTimePerfusion:
    """Quantitative peripheral microcirculation and cutaneous perfusion engine based on
    the ANDROMEDA-SHOCK trial criteria and Anderson et al. ambient temperature normalization equations."""

    def evaluate_capillary_refill_time(
        self,
        measured_crt_seconds: float = 1.8,
        ambient_temperature_celsius: float = 21.0,
        skin_site: str = "fingertip_index"
    ) -> Dict[str, Any]:
        """Calculates temperature-normalized Capillary Refill Time (CRT in seconds)
        and evaluates peripheral microvascular vasoconstriction severity."""
        raw_crt = max(0.2, min(12.0, float(measured_crt_seconds)))
        t_amb = max(5.0, min(40.0, float(ambient_temperature_celsius)))

        # Anderson et al. thermal normalization equation:
        # CRT increases by ~0.06 seconds per 1 C drop below 20 C
        # CRT_norm = raw_crt - 0.06 * (20.0 - t_amb)
        thermal_offset = round(0.06 * (20.0 - t_amb), 2)
        crt_norm = round(max(0.2, raw_crt - thermal_offset), 2)

        # ANDROMEDA-SHOCK Trial Clinical Benchmarks:
        # Normal healthy perfusion: <= 2.0 seconds
        # Mild delay / vasoconstriction: 2.1 - 3.0 seconds
        # Moderate hypoperfusion: 3.1 - 4.5 seconds
        # Critical microcirculatory shutdown: > 4.5 seconds
        if crt_norm <= 2.0:
            perfusion_tier = "Prompt / Optimal Cutaneous Microvascular Perfusion"
            microcirc_status = "Robust capillary capillary bed filling; low sympathetic vasoconstrictive tone"
        elif crt_norm <= 3.0:
            perfusion_tier = "Borderline / Mild Peripheral Vasoconstriction"
            microcirc_status = "Sub-clinical sympathetic alpha-1 adrenergic tone or local thermal cooling"
        elif crt_norm <= 4.5:
            perfusion_tier = "Delayed Capillary Refill / Systemic Vasoconstrictive Clamping"
            microcirc_status = "Elevated peripheral vascular resistance; hypovolemia or elevated neuro-adrenergic drive"
        else:
            perfusion_tier = "Severe Microcirculatory Stagnation / Critical Hypoperfusion"
            microcirc_status = "Severe capillary shutdown; acute tissue hypoperfusion warning"

        return {
            "measured_raw_crt_seconds": raw_crt,
            "ambient_temperature_celsius": t_amb,
            "thermal_adjustment_offset_seconds": thermal_offset,
            "normalized_capillary_refill_time_seconds": crt_norm,
            "anatomical_site": skin_site,
            "microvascular_perfusion_tier": perfusion_tier,
            "microcirculation_status": microcirc_status,
            "prolonged_crt_flag": crt_norm > 2.5
        }

    def calculate_peripheral_shock_index(
        self,
        systolic_bp: float = 120.0,
        heart_rate_bpm: float = 72.0,
        normalized_crt_seconds: float = 1.8
    ) -> Dict[str, Any]:
        """Calculates classic Shock Index (HR / SBP) and Combined Microvascular Shock Score (CMSS)."""
        sbp = max(50.0, float(systolic_bp))
        hr = max(30.0, float(heart_rate_bpm))
        crt = max(0.2, float(normalized_crt_seconds))

        # Classical Shock Index: SI = HR / SBP
        # Normal: 0.50 - 0.70; Elevated: >= 0.90 (indicates hypovolemia / shock)
        si = round(hr / sbp, 2)

        # Combined Microvascular Shock Score (CMSS: 0 - 100)
        # Combines macro-hemodynamics (SI) and micro-perfusion (CRT)
        si_component = max(0.0, (si - 0.50) * 80.0)
        crt_component = max(0.0, (crt - 1.5) * 20.0)
        cmss = min(100.0, round(si_component + crt_component, 1))

        if cmss < 20.0:
            hemodynamic_tier = "Optimal Hemodynamic & Microcirculatory Stability"
        elif cmss < 45.0:
            hemodynamic_tier = "Mild Compensated Autonomic Strain"
        elif cmss < 70.0:
            hemodynamic_tier = "Moderate Hemodynamic Instability / Early Hypoperfusion"
        else:
            hemodynamic_tier = "Severe Decompensated Shock & Microvascular Collapse"

        return {
            "systolic_bp_mmHg": sbp,
            "heart_rate_bpm": hr,
            "shock_index_si": si,
            "shock_index_elevated": si >= 0.90,
            "combined_microvascular_shock_score_cmss": cmss,
            "hemodynamic_stability_tier": hemodynamic_tier,
            "hemodynamic_resuscitation_guidance": (
                "Ensure oral electrolyte rehydration (500-750 mL hypotonic solution) and warm extremities."
                if cmss >= 35.0 else
                "Hemodynamic volume and microvascular tone are optimal."
            )
        }
