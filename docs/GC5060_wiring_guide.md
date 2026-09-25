# GC5060 Industrial Generator System: Electrical Wiring & Installation Manual

**Document ID:** DOC-GC5060-EWI-V1  
**Engineering Reference:** Jira Task `SAM1-11` / Escalation `SAM1-23`  
**Target Case Resolution:** Salesforce Case `#00001002` (United Oil & Gas Corp.)  
**Classification:** Technical Field Engineering & Tier-1 Support Documentation  

---

## 1. System Overview & Electrical Specifications

The **GC5060** is a commercial-grade standby/prime power generation unit designed for high-availability industrial facilities. Proper installation requires adherence to local electrical codes (NEC NFPA 70, NFPA 110 Level 1/2).

### Primary Electrical Ratings
* **Rated Output:** 500 kVA / 400 kW (Prime), 550 kVA / 440 kW (Standby)
* **Nominal Output Voltage:** 480Y/277V AC, 3-Phase, 4-Wire w/ Ground (Configurable to 208Y/120V)
* **Frequency:** 60 Hz ± 0.25% steady state
* **Rated Current:** 601 A per phase at 480V
* **Circuit Breaker:** 3-Pole 800A frame (adjustable trip unit set to 650A)
* **Control System Voltage:** 24V DC negative ground

---

## 2. Safety Precautions & LOTO Procedures

> ⚠️ **DANGER: HIGH VOLTAGE ARC FLASH HAZARD**  
> De-energize all utility feed lines and ensure generator engine starting circuits (24V DC battery bank) are isolated before opening electrical termination enclosures.

1. **Lockout/Tagout (LOTO):** Disconnect and lock out both normal utility service entrance and emergency feed disconnects.
2. **Isolate DC Starter Circuits:** Disconnect negative (-) battery terminal lead on the 24V engine starter bank.
3. **PPE Requirements:** NFPA 70E Category 4 PPE required during live verification phases.

---

## 3. Power Termination & Conductor Sizing

Connect supply cables to the main load terminal lugs located inside the lower right terminal cabinet.

### Conductor Terminal Mapping

| Terminal | Designation | Cable Specification | Torque Spec |
| :--- | :--- | :--- | :--- |
| **L1** | Phase A (Black) | 2x 350 kcmil Class B Cu per phase | 375 in-lbs (42.4 N·m) |
| **L2** | Phase B (Red) | 2x 350 kcmil Class B Cu per phase | 375 in-lbs (42.4 N·m) |
| **L3** | Phase C (Blue) | 2x 350 kcmil Class B Cu per phase | 375 in-lbs (42.4 N·m) |
| **N** | Neutral (White) | 2x 350 kcmil Class B Cu (Full Rated) | 375 in-lbs (42.4 N·m) |
| **G** | Earth Ground (Green) | 1x 2/0 AWG Bare/Insulated Copper | 275 in-lbs (31.1 N·m) |

*Note: Solid copper or concentric stranded class B conductors must be used. Ensure torque wrench calibration prior to final fastening.*

---

## 4. Control Wiring & ATS Telemetry Interface

Control signal terminations are made at **Terminal Block TB1** on the engine management controller.

```
+-------------------------------------------------------------+
|                 TB1 Control Terminal Block                  |
|  [1]   [2]   [3]   [4]   [5]   [6]   [7]   [8]   [9]  [10]  |
|  <-- Remote Start -->   <-- ATS Aux -->   <-- E-Stop Loop -->|
+-------------------------------------------------------------+
```

### Terminal Block TB1 Pinout Details
* **Pins 1 & 2 (Remote Engine Start/Stop):** Dry contact input from Automatic Transfer Switch (ATS). Contact closure initiates cranking cycle; open contacts trigger 5-minute engine cooldown and stop.
* **Pins 3 & 4 (ATS Utility Sense Telemetry):** 24V DC auxiliary feedback signal indicating utility power availability.
* **Pins 5 & 6 (Generator Available / Breaker Interlock):** Dry contact output indicating generator is up to voltage (90%+) and frequency (58.5Hz+), ready to accept load.
* **Pins 7 & 8 (External Emergency Stop Loop):** Normally-closed (NC) series loop. Breaking loop immediately opens load breaker and triggers fuel solenoid cutoff.
* **Pins 9 & 10 (RS-485 Modbus RTU / SCADA):** Pin 9: Data+ (A), Pin 10: Data- (B) for building management system telemetry.

---

## 5. Pre-Commissioning & Verification Checklist

Perform all checks prior to initiating automatic start sequence:

- [ ] **Megohmmeter Insulation Test:** 1000V DC Megger test across phases L1-L2, L2-L3, L3-L1 and Phase-to-Ground (> 100 MΩ required).
- [ ] **Phase Rotation Verification:** Confirm clockwise A-B-C rotation matching building utility service.
- [ ] **Neutral-to-Ground Bonding:** Verify bonding jumper configuration matches site scheme (Separately Derived vs. Non-Separately Derived System).
- [ ] **Torque Markings:** Apply inspection torque paint/seal across all power lug fasteners.
- [ ] **DC Control Voltage:** Verify 27.2V - 28.4V float charge across battery bank.

---

## 6. Troubleshooting Common Installation Faults

| Symptom | Probable Cause | Corrective Action |
| :--- | :--- | :--- |
| **Engine cranks but does not start on ATS call** | TB1 Pins 1 & 2 open circuit or high resistance | Measure contact resistance at ATS dry contacts (< 2Ω required). |
| **Reverse phase sequence warning on panel** | Swapped phase terminations (L1/L2/L3) | De-energize system; swap L1 and L3 at generator breaker lugs. |
| **High Neutral-to-Ground voltage (> 5V)** | Dual bonding conflict or loose neutral | Audit ATS neutral switching configuration; re-torque neutral bus. |
| **E-Stop Fault illuminated on startup** | Open circuit on TB1 Pins 7 & 8 | Verify NC circuit on all remote E-Stop pushbuttons. |

---
*Authored by Enterprise Systems Engineering | Maintained under Jira SAM1-11*