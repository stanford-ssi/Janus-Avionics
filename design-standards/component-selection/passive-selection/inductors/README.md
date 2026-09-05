# Design Standard: Inductor Selection

**Note On Package Form Factor**
Inductors don't typically come in typical imperial/metric SMD sizes, and are usually extended components on LCSC anyway. Coilcraft specializes in power inductorss

# Prototype Standard + Flight Standard (No Change)

## Power Inductors
*Power inductors are usually general purpose power devices for power regulation, distribution, and bypassing. They are not well suited for RF or any form of signal filterning other than basic coupling due to their high tolerances*

Manufacturer: Coilcraft
Product Name: Coilcraft XAL Family high-performance molded power inductors 
Family: XAL
Series links: [XAL Family](https://www.coilcraft.com/en-us/products/power/shielded-inductors/molded-inductor/xal/#/)

Quick Specs
* AEC-Q200 Compliant
* Temperature Rating: -55℃  to 125℃ (At Minimum, may be some out of spec options.)
* Wide variance of inductance and options for selection
* Very high tolerances (±20%)
* Large Inductance Value Range (.12 uH - 47 uH)

Note: Power Inductors typically have their own footpring patterns that are not standardized, so it is highly unlikely there are drop-in basic parts available in the first place.

## RF/Filtering Inductors
Manufacturer: Coilcraft
Family name: Ceramic Core Chip Inductors
Series Links: [Ceramic Core Chip Inductors](https://www.coilcraft.com/en-us/products/rf/ceramic-core-chip-inductors/#/)

Quick Specs/Notes:
 * Only the CS lines has the correct temperature compliance (AEC-Q200):
    * 0302CS/0402CS/0603CS/0805CS/1008CS 1206CS/1812CS 
* Wide Inductance Selections (0.67nH ~ 33 uH)
* Much tighter tolerances (2% - 5%)