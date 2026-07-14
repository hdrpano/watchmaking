# Watchmaking Gear Simulator

## 📘 Learn More

If you would like to understand the theory behind the software, gear geometry, contact analysis and practical watchmaking calculations, please see the book:

## 📖 Watchmaking with Python

From Traditional Gear Geometry to Modern Contact Analysis

## ➡️ Available here: [watchmaking](https://watchmaking.com)

The book explains the mathematical foundations, the Belot profile format, gear generation, contact analysis, Monte Carlo simulation, Hertzian contact pressure, and many of the algorithms implemented in this software.

Professional analysis tools for Swiss watch gear trains.

The **Watchmaking Gear Simulator** is a collection of applications for analysing, editing and converting traditional watch wheel and pinion profiles based on the Belot geometry format.

The software has been developed with a strong focus on practical watchmaking applications, including contact analysis, efficiency calculations, Hertzian pressure, manufacturing tolerances and CAD integration.

![Contact Analyses](/img/contact.png)

# Features

## Watchmaking Gear Simulator

* Graphical contact analysis
* Active contact zone calculation
* Gear mesh efficiency
* Torque ripple analysis
* Hertzian contact pressure
* Contact window calculation
* Wheel and pinion drive simulation
* Contact path visualisation
* Monte Carlo tolerance simulation
* Batch processing
* Automatic PDF reports
* SVG and PNG graphics export
* Fusion 360 MCP export

## Profile Editor

The Profile Editor allows direct modification of Belot gear profiles.

Features include:

* Interactive profile editing
* Wheel and pinion support
* Profile mirroring
* Contact analysis comparison
* Material selection
* Immediate simulation of edited geometry

![Profile Editor](/img/editor.png)

## Profile Converter

The Converter supports conversion between different watch gear profile formats.

Supported formats include:

* Belot TXT
* DXF
* ENO
* EGR
* NIHS 20-30

The converter preserves the original geometry whenever possible and supports exact arc and line reconstruction.

![DXF](/img/dxf.png)

## NIHS Generator

The NIHS Generator creates standard NIHS 20-30 watch gear profiles.

Features include:

* Wheel generation
* Pinion generation
* Automatic Belot export
* Direct compatibility with the Gear Simulator

![HIHS to Belot](/img/nihs.png)

# Belot Parser Source Code

This repository also includes the complete source code of

```
Debug.py
```

![Debug.py](/source/Debug.py)

The parser demonstrates how Belot profile files are read and interpreted.

It is intended as a reference implementation for developers who want to

* read Belot files
* build their own applications
* generate custom profiles
* integrate Belot geometry into CAD or CAM software

# Supported Operating Systems

Precompiled applications are available for:

* Windows 11 (64-bit)
* macOS (Apple Silicon)

The macOS applications are digitally signed.

# Installation

Download the latest release from the **Releases** section.

Unzip the package.

Start the desired application:

* Watchmaking Gear Simulator
* Profile Editor
* Profile Converter
* NIHS Generator

No Python installation is required.

# Typical Workflow

1. Generate or import wheel and pinion profiles.
2. Inspect and edit the geometry.
3. Run contact analysis.
4. Evaluate efficiency and Hertzian pressure.
5. Perform Monte Carlo tolerance simulations.
6. Export geometry for Fusion 360.

# Documentation

Additional documentation, tutorials and theory papers are available in the project documentation.

The generated PDF reports explain the calculated results in detail.

# License

The applications are distributed as freeware binaries.

The included parser source code is released under the MIT License.

Please see the LICENSE file for details.

# Contributing

Bug reports and feature suggestions are always welcome.

If you discover incorrect geometry, unsupported profile formats or calculation issues, please open an Issue.

Contributions improving documentation are also appreciated.

# Disclaimer

The software is intended for engineering, educational and research purposes.

Although every effort has been made to verify the calculations, users remain responsible for validating results before applying them to production components.

# Acknowledgements

The project builds upon many years of practical experience in Swiss watchmaking, gear geometry and escapement development.

Special thanks to everyone who has provided valuable feedback during testing.

# Screenshots

* Gear Simulator
* Contact Analysis
* Monte Carlo Simulation
* Profile Editor
* Converter
* Fusion Export

![Monte Carlo](/img/MonteCarlo.png)
![Fusion MCP](/img/fusion.png)
![Fusion MCP](/img/fusion_d.png)

# Example Applications

*(Add example images here.)*

* Escape wheel
* Fourth wheel
* Third wheel
* Centre wheel
* Pinion profiles
* NIHS examples

# Contact

Questions, suggestions and bug reports are welcome through the GitHub Issues page.
