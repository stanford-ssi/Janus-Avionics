# Design Standard: Resistor Selection

*Note to new members: When designing, make sure you check the datasheet to ensure you are meeting the proper wattage/voltage/current specifications of the resistor you have chosen to use*

#### Acronym List:
* TCR: Temperature Coefficient

# Resistor Standards
Note: Every standard uses conventional SMD imperial code sizings and are drop-in capable.(i.e 0603, 0805)

Note: Both the Prototype and Flight Standard is E-95 E-standard for nominal resistance values.

## Prototype Standard
Manufacturer: UNI-ROYAL\
Product Name: Thick Film Chip Resistors\
Series Name: 01005/0201/0402/0603/0805/1206/1210/1812/2010/2512 Series\
Datasheet: [Thick Film Chip Resistors – Data Sheet](./datasheets/Uniroyal_Thick_Film_Chip_Resistors.pdf)\
LCSC Lookup: [Uniroyal Resistors](https://www.lcsc.com/category/1199.html?sid=2B66260A33639B3D2E02917D5B2E3D09)

Quick Specifications:  
* Operating Temperature: -55℃ ~ 125℃ 
    * Temperature Coefficient varies depending on resistance below 10 ohms.
    * TCR: ±100ppm / ℃  (R > 10 Ohms)
    * Resistance Range: 10 mOhms ~ 10 MOhms
    * Value Tolerances: 0.5%, 1%, 2%, 5%

*Note: UNI-ROYAL is the dominating manufacturer on LCSC for the 'Basic' part category and is best for early prototyping*

## Flight Standard 
Manufacturer: Vishay\
Product Name: High Stability Thin Film Flat Chip Resistors\
Series Name: TNPW e3\
Datasheet: [Vishay - High Stability Thin Film Flat Chip Resistors](./datasheets/Vishay_High_Stability_Thin_Film_Flat_Chip_Resistors.pdf)\
LCSC Lookup: [TNPW Vishay Resistors](https://www.lcsc.com/category/1199.html?scene=FULL_MATCH&globalKeyword=TNPW&s_z=n_q_TNPW)

Quick Specifications:  
* Operating Temperature: -55 °C to 125 °C
* TCR: temp coefficient depends on type/size
    * Variable TCR from 10 ppm/°C to 50 ppm/°C (Please reference datasheet during resistor selection).
* Resistance Range: 1 Ohms ~ 3.01 MOhms
* Value Tolerances: 0.5%, 1.0%
* Tin Whisker Resistant
* AEC-Q200 Qualified (Whisker free)

## Flight Standard: Sense & Shunt Resistors (Extremely Low Values)
Manufacturer: Vishay\
Product Name: Power Metal Strip® Resistors, Very High Power (to 3 W),Low Value (Down to 0.0005 Ω), Surface-Mount\
Series Name: WSLP\
Datasheet: [Power Metal Strip® Resistors, Very High Power (to 3 W),Low Value (Down to 0.0005 Ω), Surface-Mount](datasheets/Vishay_Power_Metal_Strip_Resistors_High_Power_Low_Value.pdf)\
LCSC Lookup: [WSLP Vishay Resistors](https://www.lcsc.com/category/1199.html?scene=FULL_MATCH&globalKeyword=WSLP&s_z=n_q_t_WSLP&spm=wm.ssy.tc.0.tz&lcsc_vid=EVFfBAZSQlMKU1VXFlRXBlNRR1ZeBQUCQVVeXlBWRAIxVlNeT1RYUVxRQVVaVDsOAxUeFF5JWBYZEEoKFBINSQcJGk4NBhADEA4cHktXRlhXSQwSGg0%3D)

Quick Specifications:  
* Operating Temperature: -55 °C to 125 °C
* TCR: Variable Per Part # (75 ~ 400 ppm /°C )
* Resistance Range:0.5 mOhms ~ 100 mOhms
* Value Tolerances: 0.5%, 1.0%
* AEC-Q200 Qualified (Whisker free)