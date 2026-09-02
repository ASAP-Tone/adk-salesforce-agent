# GC5060 Electrical Wiring & Installation Manual

**Document Reference:** UM-GC5060-REV4  
**Date:** September 2, 2026  
**Engineering Escalation:** SAM1-11  
**Classification:** Technical Release  

This comprehensive, code-compliant manual provides detailed instructions for the safe, reliable, and compliant electrical wiring and configuration of the GC5060 Heavy-Duty Industrial Generator System. This document serves as the standard operational reference to resolve technical integration inquiries for key clients, including United Oil & Gas Corp.

---

## 1. Safety & Compliance Standards

Before beginning installation, ensure strict adherence to all safety protocols and regulatory standards:
*   **De-energization:** Verify that all upstream utility and auxiliary power sources are completely disconnected and locked out/tagged out (LOTO) in accordance with OSHA and standard industrial safety guidelines.
*   **Personnel Requirements:** Wiring must be performed exclusively by a licensed industrial electrician or certified field engineer.
*   **Standards Compliance:** This installation must comply with all local, state, and national electrical codes, including the National Electrical Code (NEC/NFPA 70) and IEC 60364.
*   **PPE Requirements:** Appropriate Personal Protective Equipment (PPE) including Arc Flash protection, high-voltage gloves (Class 00 or higher), and dielectric safety footwear is mandatory.

---

## 2. Electrical Specifications

Ensure the site electrical supply matches the GC5060's operational parameters:

| Parameter | Specification | Value |
| :--- | :--- | :--- |
| **Prime Power Rating** | kVA / kW | 500 kVA / 400 kW |
| **Standard Output Voltage** | Volts (AC) | 277 / 480V AC (3-Phase Delta) |
| **System Frequency** | Hertz (Hz) | 60 Hz (Standard US Configuration) |
| **Rated Current Output** | Amperes (A) | 601 Amps @ 480V |
| **Excitation System** | Type | Permanent Magnet Generator (PMG) |
| **Power Factor** | cos φ | 0.8 (Lagging) |

---

## 3. Detailed Wiring Diagram & Terminal Connections

The GC5060 requires a 3-Phase, 4-Wire Star/Wye configuration at the main terminal block (TB-A) inside the generator control bay.

```
       [ Upstream Utility / ATS Panel ]
             |     |     |     |
             |     |     |     |
        L1---|-----|-----|-----|  (480V Phase A - Black)
             L2---|-----|-----|  (480V Phase B - Red)
                  L3---|-----|  (480V Phase C - Blue)
                       N-----|  (Neutral - White)
                             G  (Ground / PE - Green/Yellow)
             |     |     |     |
             v     v     v     v
        [ TB-1  TB-2  TB-3  TB-N  TB-G ]
        ============== TB-A ============
           GC5060 MAIN TERMINAL BLOCK
```

### Connection Protocols:
1.  **Phase Conductors (L1, L2, L3):** Connect the main phase feeders to terminals **TB-1 (Phase A)**, **TB-2 (Phase B)**, and **TB-3 (Phase C)**. Use double-bolt compression lugs torqued to 45 N·m (33 lb-ft).
    *   *Color Code:* Black (L1), Red (L2), Blue (L3) for US 480V installations.
2.  **Neutral Conductor (N):** Connect the system neutral to terminal **TB-N**. Ensure the neutral-to-ground bonding strap is installed ONLY if the GC5060 is configured as a *Separately Derived System* (SDS).
3.  **Protective Earth / Ground (G/PE):** Connect a minimum 2/0 AWG copper grounding electrode conductor directly to terminal **TB-G**. Solidly bond this to the main site grounding grid.

---

## 4. Control Wiring & Auxiliary Configurations

To enable remote monitoring, automated start/stop cycles, and safety interlocks, integrate the auxiliary terminal strip (TB-AUX):

*   **Remote Start (Terminals 3 & 4):** Connect potential-free dry contacts from the Automatic Transfer Switch (ATS) to terminals 3 and 4. A contact closure initiates the start cycle.
*   **Modbus RS485 Comm (Terminals 11 & 12):** Connect shielded twisted-pair (STP) cable to terminals 11 (A-) and 12 (B+) for telemetry integration with SCADA or Building Management Systems.
*   **Emergency Stop (Terminals 1 & 2):** Connect external, normally-closed (NC) emergency stop buttons in series across terminals 1 and 2. Opening this circuit triggers an immediate hardware shutdown.

---

## 5. Post-Installation Commissioning & Testing

Before energizing the load, perform the following verification procedures:

1.  **Insulation Resistance Test:** Measure insulation resistance between phases and from phases to ground using a 1000V Megger. Readings must exceed **100 MΩ** before startup.
2.  **Phase Rotation Verification:** Use a phase rotation meter to verify that phase sequence is **A-B-C (Right-Hand Rotation)**. Incorrect rotation will damage downstream motors.
3.  **No-Load Voltage Check:** Start the engine and run the generator with output breaker open. Verify terminal voltage reads **480V AC (Phase-to-Phase) ± 1.5%** and **277V AC (Phase-to-Neutral) ± 1.5%** across all phases.
4.  **CSAT & SLA Assurance:** Prompt resolution of customer inquiries regarding these setup protocols is crucial to maintaining CSAT targets (>4.70/5.00) and preventing stalled GTM pipeline. Reference escalations should always be logged against the active tracking ticket.
