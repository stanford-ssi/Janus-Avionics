# Creating FMUs
The following is a guidelines of standards that must be followed when developing any FMU (Functional Modular Unit).
Please adhere to these standards or your pull requests will not be merged into the main branch.

### What are FMUs?
**A Functional Modular Unit (FMU)** is SATS AV’s internal name for the following concept: An Integrated Circuit, Filter, Converter, or any other group of external components that fulfill a single task or purpose that can be accessibly integrated into any system that follows a set communication standard. FMUs must be easily integrable into boards that meet certain system-level defined power and communication standards and that require the functionality the particular FMU provides.

In order to implement FMU's, we take advantage of KiCAD 10's ability to create 'Design Blocks'. A **Design Block**, is KiCAD's internal feature that describes pre-built modules that combine both a schematic circuit and its matching PCB layout.These can be easily picked n' placed onto a schematic with ease for reusability.

We implement abstraction through hierarchical labels into each FMU. 

Please see the [FUNCTIONAL MODULAR UNIT DEVELOPMENT GUIDELINE](https://docs.google.com/document/d/1Rt5rdxxSY23N9fzfNevyRSlRJnNfZceG8D1mi94cfGE/edit?tab=t.0) document for more information.

## Organizational Requirements
These requirements outline how you must organize your folders/files when working with FMUs.

### Folder Conventions
When developing indivual FMU's, all work should follow the following structure:

```
Janus-Avionics
    ├── FMUs
    │   └── FMU Subsystem Category
    │       └── Your IC Part Number - IC Category
    │           ├── doc.md (All FMU application documentation and implementation instructions live here)
    │           └── KiCAD (Actual KiCAD files are placed here.)
    ├── LICENSE
    └── README.md
```

### Example
Base Part Number: LMR51430
Orderable Part Number: LMR51430XDDCR
Functional Descriptor: “SIMPLE SWITCHER® Power Converter 4.5-V to 36-V, 3-A, Synchronous Buck Converter in a SOT-23 Package”

Here is an example of how an FMU based on the LMR51430 buck converter should be organized within the repository:

```
Janus-Avionics
    ├── FMUs
    │   └── power
    │       └── LMR51430XDDCR - Buck Converter
    │           ├── doc.md (All FMU application documentation and implementation instructions live here)
    │           └── KiCAD (Actual KiCAD files are placed here.)
    ├── LICENSE
    └── README.md
```

As you can see, placeholder names have been replaced with the following:

FMU Subsystem Category --> power
Your IC Part Number --> LMR51430XDDCR 
IC Category --> Buck Converter

**Note on IC Categories:**

IC categories should be overarching descriptors of an IC and what it is, rather than explicit details about the IC itself.
For example, some common IC Categories are the following:
* Buck Converter
* Boost Converter
* Buck-Boost Converter
* Maximum Power Point Tracking IC
* CAN Transceiver IC
* . . .