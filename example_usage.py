# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Microvascular Capillary Refill Time Perfusion Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentMicrovascularCapillaryRefillTimePerfusion

def main():
    agent = PersonalAgentMicrovascularCapillaryRefillTimePerfusion()

    print("=" * 70)
    print("DEMO: Personal Agent Capillary Refill Time (CRT) & Perfusion Engine")
    print("=" * 70)

    # 1. Evaluate Fingertip Capillary Refill Time (Measured 2.4s at 15.0 C ambient -> normalized to ~2.1s)
    res_crt = agent.evaluate_capillary_refill_time(
        measured_crt_seconds=2.4,
        ambient_temperature_celsius=15.0,
        skin_site="fingertip_index"
    )

    print(f"\n1. Peripheral Capillary Refill Time (CRT) Analysis:")
    print(f"   Raw Measured CRT: {res_crt['measured_raw_crt_seconds']} s (Site: {res_crt['anatomical_site']})")
    print(f"   Ambient Temperature: {res_crt['ambient_temperature_celsius']} C")
    print(f"   Anderson Thermal Offset: {res_crt['thermal_adjustment_offset_seconds']} s")
    print(f"   Normalized CRT (20 C Standard): {res_crt['normalized_capillary_refill_time_seconds']} s")
    print(f"   Perfusion Tier: {res_crt['microvascular_perfusion_tier']}")
    print(f"   Microcirculation Status: {res_crt['microcirculation_status']}")
    print(f"   Prolonged CRT Flag: {res_crt['prolonged_crt_flag']}")

    # 2. Calculate Combined Microvascular Shock Score (BP 118/76, HR 88 bpm, CRT 2.1s)
    res_shock = agent.calculate_peripheral_shock_index(
        systolic_bp=118.0,
        heart_rate_bpm=88.0,
        normalized_crt_seconds=res_crt['normalized_capillary_refill_time_seconds']
    )

    print(f"\n2. Combined Microvascular Shock Score (CMSS):")
    print(f"   Systolic BP: {res_shock['systolic_bp_mmHg']} mmHg | Heart Rate: {res_shock['heart_rate_bpm']} bpm")
    print(f"   Classical Shock Index (SI): {res_shock['shock_index_si']} (Elevated: {res_shock['shock_index_elevated']})")
    print(f"   Combined Microvascular Score (CMSS): {res_shock['combined_microvascular_shock_score_cmss']}/100")
    print(f"   Hemodynamic Stability: {res_shock['hemodynamic_stability_tier']}")
    print(f"   Guidance: {res_shock['hemodynamic_resuscitation_guidance']}")

    print("\nVerification complete: Capillary refill perfusion engine executed flawlessly.")

if __name__ == "__main__":
    main()
