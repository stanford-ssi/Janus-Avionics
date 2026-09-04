# Component Selection

## Component Selection Considerations
Due to the harsh nature of space, all designs must consider worst-case scenarios in their designed environment. In the case of Project Janus, we aim to design a robust satellite designed to handle Low-Earth-Orbit (LEO) conditions. Therefore, the following conditions must be addressed during every selection of the design process:

## Temperature Variation
1. Internal components
    * Two Standard options to choose from
        1. Standard internal LEO component temperature requirements
        2. New Space alternative Standards
            * –40°C to +125°C 
            * ICs use **AEC-Q100**
            * Passives use **AEC-Q200**
            * discrete Semiconductors use **AEC Q-101**
2. External components
    * External components/panels/sensors require wider temperature ranges and must deal with more thermal shock variation
        * Must be rated from –150°C to +150°C

## Radiation Tolerances
1. Total Ionizing Dose (**TID**) must typically withstand 20 - 50 krad over a 3-5 year LEO mission lifespan in LEO orbit.
2. Single Event Effects (SEE) should be rated up to a Linear Energy Transfer (**LET**) of 30 to 43 MeV * cm^2 / mg 

Note: Many COTS components use specialized rad-hard ICs that monitor other components, power-cycling the monitored componet if a radiation-induced current spike is detected. This is a cheaper solution for manual rad-hardening if rad-hard compnents are either unavailable or too expensive.

## Outgassing + Material Requirements
1. Components , especially ICs, must comply with ASTM E595 standard manufacturing quality ratings. This standard comprises the following ratings:
    1. Total Mass Loss (TML) < 1.0%
    2. Collected Volalite Condensabile Material (CVCM) < 0.1%

2. Components can not use pure matte tin finishes whichc ommonly cause circuit shorts in zero-gravity. Mitigation typically encorporates the replacement of tin-lead components with NiPdAu (Nickel-Palladium-Gold) or SnPb (Tin-Lead Alloy) finishes.

3. High-Reliability components strictly require gold bond wires over copper wires to avid corrosion and stess failures during thermal flexing. For flight IC's, prioritize gold bond wire packages if available.



## Prototyping vs Flight Boards Notes & Requirements
* Due to the increased costs of military standard components, early designs and prototypes should use standard, non-radhardened components according to its categories recommended manufacturer if applicable. I.E, all passives have recommended radhardened and temperature tolerant variations, but some IC's may not. Some ICs may be standalone and have no rad-hardened alternative.

## Helpful Links
1. [NASA Electrical, Electronicvand Electromechanical (EEE) Parts Assurance](https://nepp.nasa.gov/files/29637/NEPP-CP-2017-Sampson-Presentation-STEP-EEE-Parts-TN65338-NEPPweb-reuse-TN45954.pdf)
    - AEC-Q qualified/teted components can be found on Page 38
2. [Satellite Constellation Component Manufacturing: Mission-Critical Solutions for LEO Systems](https://www.modusadvanced.com/resources/blog/satellite-constellation-component-manufacturing-mission-critical-solutions-for-leo-systems)
    - Outlines requirements for LEO system radiation standards