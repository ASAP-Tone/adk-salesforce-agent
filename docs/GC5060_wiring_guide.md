# GC5060 Electrical Wiring Installation Guide

This official technical guide provides comprehensive, code-compliant electrical wiring installation instructions for the **GC5060 Heavy-Duty Industrial Generator System**. It addresses the specific electrical design inquiries raised by United Oil & Gas Corp. under customer support case **#00001002** and is tracked under Engineering Escalation Jira Ticket **SAM1-11**.

---

## 1. Safety Specifications & Pre-requisites
- **DANGER:** HIGH VOLTAGE. Ensure all main distribution breakers, isolators, and transfer switches are fully locked out and tagged out (LOTO) prior to initiating any wiring operations.
- All wiring must conform strictly to the National Electrical Code (NEC / NFPA 70), local municipal codes, and IEC 60364 industrial standards.
- Grounding and bonding must be executed prior to any phase terminal terminations.

## 2. Technical Specifications
- **Voltage Output:** 3-Phase 480V AC (Delta) / 277V AC (Wye) Configurable
- **Rated Power:** 500 kW / 625 kVA
- **Full Load Current:** 752 Amps (at 480V 3-Phase)
- **Frequency:** 60 Hz
- **Insulation Class:** Class H

---

## 3. Wiring Terminal Connection Layout
The terminal box is located on the rear-left quadrant of the generator housing. Connection terminals are rated for copper conductors only.

| Terminal Label | Description | Wire Color Code (NEC) | Recommended Torque (Nm) | Conductor Size |
| :--- | :--- | :--- | :--- | :--- |
| **L1 (A)** | Phase A Hot Line | Black | 42 Nm | 3x 250 kcmil THHN |
| **L2 (B)** | Phase B Hot Line | Red | 42 Nm | 3x 250 kcmil THHN |
| **L3 (C)** | Phase C Hot Line | Blue | 42 Nm | 3x 250 kcmil THHN |
| **N** | Neutral Line | White | 35 Nm | 2x 250 kcmil THHN |
| **PE / G** | Protective Earth / Ground | Green / Bare | 35 Nm | 1x 2/0 AWG |

---

## 4. Grounding and Bonding Guidelines
- Neutral grounding must be solidly bonded to the generator frame and connected to the facility main grounding electrode system at the Automatic Transfer Switch (ATS) or service entrance.
- Ensure the grounding electrode conductor is sized according to NEC Table 250.66.

---

## 5. Control and Excitation Interface Wiring
For automatic starting and monitoring, connect the control harness to the auxiliary block **Aux-T1**:
1. **Pins 1 & 2 (Remote Start):** Connect to the ATS dry contacts. Apply 18 AWG shielded twisted pair.
2. **Pins 5 & 6 (Common Alarm):** High-temperature/Low-oil pressure shutdown indicators.
3. **Pins 9 & 10 (Battery Charger Input):** 120V AC input for the integrated trickle charger.

---

## 6. Pre-Commissioning & Verification Protocol
Perform the following checks before energizing the system:
1. **Insulation Resistance Test (Megger):** Test phase-to-phase and phase-to-ground using a 1000V DC megohmmeter. Minimum acceptable reading is **100 Megaohms**.
2. **Phase Rotation Audit:** Verify clockwise (A-B-C) phase rotation to match the utility power grid.
3. **Torque Audit:** Re-verify terminal torque values against the specifications in Section 3.
4. **SLA Reference:** To maintain support CSAT levels within our SLA targets, these diagnostic steps should be fully logged.

---

**Authorized by:** Cloud Architecture and Engineering GTM Team  
**Jira Reference:** `SAM1-11`  
**Salesforce Case Reference:** `Case #00001002`  
**GCP Project Context:** `truiz-agy-demo`