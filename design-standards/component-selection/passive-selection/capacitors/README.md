# Design Standard: Capacitor Selection

**Acronyms:**
EIA: Electronic Industries Alliance

## Capacitor types and best use cases:
**Ceramic MLCC Capacitor EIA temperature characteristic codes**
* C0G/NP0
    * Best Standard for precision-critical use caes such as timing, filtering, and RF due to its tendency for temperature stability, low ESR, lack of piezoelectric microphonics, and negligible aging effects.
    * C0G uses **temperature-compensating dielectrics** (Class I) with predictible, tiny capacitance change over temperature
    * Temp Range: -55°C ~ +125°C
* X7R
    * Best for bulk decoupling/bypass capacitors where tolerance and exact values aren't too important
    * X7R uses Ferroelectric dielectrics (Class II)
    * Can typically handle higher capcitance values than C0G but has worse temperature drift and voltage coeffients (C0G has virtually no capacitance drift when voltage is applied).
    * Temp Range: -55°C ~ +125°C


*(We ignore class III since they're pretty much useless for our use case, google them if you want)*

Note: Every standard uses conventional SMD imperial code sizings and are drop-in capable.(i.e 0603, 0805)

# Prototype Standard

Manufacturer: Samsung Electro-Mechanics
Product Name: Multilayer Ceramic Capacitors\
Series Name: CL\
Datasheet: [Multilayer Ceramic Capacitors](./datasheets/Samsung_Multilayer_Ceramic_Capacitors.pdf)\
LCSC Lookup: [Ceramic Capacitors - Samsung Electro-Mechanics](https://www.lcsc.com/category/1142.html?sid=D236DADC7E500240DADFE46DF9A687D2)

Quick Specifications:
 * Contains Class I and Class II Ceramics with variable ranges:
    * C0G: 0.5 pF ~ 130 nF
    * X7R: 0.1 uF ~ 100 uF
* Temp Range: -55°C ~ +125°C

# Flight Standard
Note: The only reason a flight standard is necessary is because most basic capacitors result in tin whiskering.

Manufacturer: TDK\
Product Name: MULTILAYER CERAMIC CHIP CAPACITORS\
Series Name: CGA (This series is an LCSC Extended Component)

Datasheet: [Multilayer Ceramic Capacitors](./datasheets/TDK_MULTILAYER_CERAMIC_CHIP_CAPACITORS.pdf)
LCSC Lookup: [Ceramic Capacitors - Samsung Electro-Mechanics](https://www.lcsc.com/category/1142.html?sid=D236DADC7E500240DADFE46DF9A687D2)


Quick Specifications:
 * Resistant to whiskering (AEC-Q200 compliant)
 * Contains both C0G and X7R standards:
    C0G: 100pF - 150nF
    X7R: 1nF -47 nF
* Temp Range: -55°C ~ +125°C
    
## Some extra notes on capacitors
Note: We prioritize Ceramic capacitors for all intents and purposes due to its flight heritage and to mitigate the tendency of aluminum capacitors and their poor thermal cycling. Electrolytics also have many outgassing problems and are avoided at all costs. Tantalum capacitors also tend to short unders urge current and are at risk of catastrophic, irreperable failure if something goes wrong in space.