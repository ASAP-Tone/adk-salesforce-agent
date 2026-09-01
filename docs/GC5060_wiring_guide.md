# GC5060 Generator System - Technical Electrical Wiring Installation Guide

**Document ID:** GD-GC5060-E01  
**Date:** September 1, 2026  
**Version:** 2.0  
**Reference:** Jira Escalation Ticket **SAM1-11**  

---

## 1. Executive Overview & Scope
This technical guide provides definitive instructions for the safe, code-compliant electrical installation and wiring of the **GC5060 Industrial Generator System**. It is specifically released to resolve technical blockers and unblock ongoing deployment projects (such as those for United Oil & Gas Corp under **SAM1-11**).

This guide applies to L1/L2 Technical Support teams, Field Sales Engineers, and certified field electricians performing installation work.

---

## 2. Safety Specifications & Hazard Warnings

> [!DANGER]
> **HIGH VOLTAGE / ARC FLASH HAZARD**  
> Working on the GC5060 electrical terminal block involves exposure to lethal voltages up to 480VAC. Only certified industrial electricians wearing appropriate Personal Protective Equipment (PPE) compliant with NFPA 70E (Category 2 or higher) may perform these steps.

*   **Lockout/Tagout (LOTO):** Verify that all upstream circuit breakers and utility lines feeding the generator enclosure are locked out, tagged, and verified de-energized prior to removing any terminal shroud.
*   **Emergency Stop:** Locate and verify the functionality of the local Emergency Stop (E-Stop) switch before energizing any part of the generator.

---

## 3. Pre-Installation & Sizing Specifications

To ensure optimal safety and performance, the primary conductors must be sized in strict compliance with **NEC (National Electrical Code) Article 310** based on the GC5060's full load rating:

*   **Full Load Amperage (FLA):** 150 Amps at 480VAC.
*   **Conductor Type:** Copper (Cu) conductors only. THHN/THWN-2 rated for 90°C wet/dry locations is highly recommended.
*   **Conductor Sizing:** **2/0 AWG THHN Copper** (rated up to 195A at 90°C, providing a safe margin over 125% of FLA as per NEC Article 215).
*   **Conduit Sizing:** Minimum **2-inch Rigid Metal Conduit (RMC)** or Intermediate Metal Conduit (IMC) to accommodate conductors and grounding electrode.
*   **Terminal Torque Spec:** Tighten all primary terminal connections to exactly **120 in-lbs (13.5 N-m)** using a calibrated torque wrench.

---

## 4. Three-Phase Delta (480V) Wiring Configuration

The GC5060 generator system is designed to feed a **3-Phase 3-Wire + Ground Delta configuration** at 480VAC nominal.

```
                  [ GC5060 Terminal Block ]
               +----------------------------+
   Line 1 ---->|  [ L1 ] Terminal (Red)     |
   Line 2 ---->|  [ L2 ] Terminal (Black)   |
   Line 3 ---->|  [ L3 ] Terminal (Blue)    |
               |                            |
   Ground ---->|  [ G ] Ground Bus (Green)  |
               +----------------------------+
```

### Step-by-Step Connection Instructions:
1.  **Remove Terminal Panel:** Unscrew and remove the dead-front protective plate on the internal GC5060 main junction box.
2.  **Route Conductors:** Feed the three primary line conductors (L1, L2, L3) and the system ground conductor through the conduit entry point using an approved watertight strain relief connector.
3.  **Phase Connections:**
    *   Connect **Line 1 (Phase A / Red)** directly to terminal lug marked **L1**.
    *   Connect **Line 2 (Phase B / Black)** directly to terminal lug marked **L2**.
    *   Connect **Line 3 (Phase C / Blue)** directly to terminal lug marked **L3**.
4.  **Verify Clearances:** Ensure there is a minimum of **1.0 inch (25.4 mm)** air gap clearance between any live phase metal and the grounded metal housing.

---

## 5. Grounding and Bonding Requirements

Proper grounding is essential for system stabilization and ground-fault protection, in compliance with **NEC Article 250**:

*   **Grounding Conductor:** Connect a minimum **#4 AWG bare copper or green insulated wire** from the local generator Ground Bus (marked **G**) directly to the facility's primary Grounding Electrode System (ground ring, concrete-encased electrode, or ground rods).
*   **System Bonding Jumper:** If configured as a Separately Derived System, ensure the main bonding jumper is securely connected between the generator neutral star-point (if present) and the chassis Ground Bus. For standard Delta configurations, ground the metal enclosure chassis directly.
*   **Ground Resistance:** Verify grounding electrode path resistance is **less than 25 Ohms** using a fall-of-potential ground tester. If resistance is higher, additional ground rods must be driven.

---

## 6. Post-Installation Commissioning Checklist

Do not energize the system until all items on this checklist are successfully verified and logged:

1.  [ ] **Torque Verification:** Re-verify terminal lugs L1, L2, L3 are torqued to 120 in-lbs.
2.  [ ] **Insulation Resistance (Megger Test):** Perform a 1000V DC insulation resistance test between phase conductors and between each phase and ground. Resistance must exceed **100 Megaohms (MΩ)**.
3.  [ ] **Phase Rotation Test:** Connect a phase rotation meter to L1-L2-L3 and verify a **Clockwise (ABC) rotation** to prevent equipment damage.
4.  [ ] **Voltage Verification:** Once generator is started at no-load, verify output voltage is stable at **480VAC Phase-to-Phase** (± 5% tolerance).
5.  [ ] **Ground Continuity:** Ensure perfect electrical continuity (less than 0.1 Ohms) between the generator chassis and the auxiliary grounding bus.

---

## 7. Escalation & Engineering Support
For issues or abnormalities encountered during installation that are not resolved by this document, please contact the dedicated Deal/Support team quoting **SAM1-11**:
- **Technical Engineering Escalation:** Jira Project `SAM1` / Issue **SAM1-11**
- **Client Account Team:** United Oil & Gas Deal Desk (Reference Account Exposure: $1.34M)
- **24/7 Technical Support Hotline:** support-power@company.com
