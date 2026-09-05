# Component Selection

## Component Selection Considerations
Due to the harsh nature of space, all designs must consider worst-case scenarios in their designed environment. In the case of Project Janus, we aim to design a robust satellite designed to handle Low-Earth-Orbit (LEO) conditions. Therefore, the following conditions must be addressed during every selection of the design process:

## Temperature Variation
1. Internal components
    * ICs/Silicon devices must support an operating range of -55°C to +125°C as per Nasa's MIL-SPEC recommendations.
2. External components
    * External components/panels/sensors require wider temperature ranges and must deal with more thermal shock variation
        * Must be rated from –150°C to +150°C

## Radiation Tolerances
1. Total Ionizing Dose (**TID**) must typically withstand 20 - 50 krad over a 3-5 year LEO mission lifespan in LEO orbit.
2. Single Event Effects (SEE) should be rated up to a Linear Energy Transfer (**LET**) of 30 to 43 MeV * cm^2 / mg 

Note: Many COTS components use specialized rad-hard ICs that monitor other components, power-cycling the monitored componet if a radiation-induced current spike is detected. This is a cheaper solution for manual rad-hardening if rad-hard compnents are either unavailable or too expensive.

## Outgassing + Material Requirements
1. Components , especially ICs, must comply with **ASTM E595** standard manufacturing quality ratings. This standard comprises the following ratings:
    1. Total Mass Loss (**TML**) < 1.0%
    2. Collected Volalite Condensabile Material (**CVCM**) < 0.1%

2. Components can not use pure matte tin finishes which commonly cause circuit shorts in zero-gravity. Mitigation typically encorporates the replacement of tin-lead components with NiPdAu (Nickel-Palladium-Gold) or SnPb (Tin-Lead Alloy) finishes.

3. High-Reliability components strictly require gold bond wires over copper wires to avid corrosion and stess failures during thermal flexing. For flight IC's, prioritize gold bond wire packages if available.

4. Avoid 100% Tin Leads as they can cause "whiskering" at extreme temperatures. This leads to tin particles being spread out, causing the possibility of shorts. Avoid pure tin leads and instead use Tin-Lead alloy/solder/finishes for components if possible. 

Definition: Outgassing refers to the release of gas which is dissolved or trapped inside materials when the surrounding temperature or pressure changes. Changes in surroundings result in sublimation or evaporation of the trapped volatile substances or chemicals. Outgassing can directly degrade signals in an active circuit, hence why it needs to be considered during final board bring-ups.

## Other Notes About Component Selection
A lot of decisions about component selection depend on expected maximum parameters like voltage, current, temperature, radiation tolerance, etc. As a result, its usually easier to just derate components and pick components rated way higher than needed if its not too expensive. Using the helpful links at the bottom of this page is a great resource if you're having any troubles finding parts or choosing safety margins and need some guidance.

## Prototyping vs Flight Boards Notes & Requirements
* Due to the increased costs of military standard components, early designs and prototypes should use standard, non-radhardened components according to its categories recommended manufacturer if applicable. I.E, all passives have recommended radhardened and temperature tolerant variations, but some IC's may not. Some ICs may be standalone and have no rad-hardened alternative.

## Helpful Links
1. [EEE-INST-002: Instructions for EEE Parts Selection, Screening, Qualification, and Deratin](./NASA-guidelines/EEE-INST-002.pdf)

2. [NASA Parts Selection List (NPSL)](https://nepp.nasa.gov/npsl/)
    - Parts selection tool for design engineers and parts engineers supporting NASA space flight programs. Large list of parts that NASA recommends for flight projects based on evaluations, risk assessments and quality levels. This list automatically screens for components in strong supply.
    