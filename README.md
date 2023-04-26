<div align="center">
  <img width="60%" height="80" src="./.github/logotipo.svg">
  <p align="center">Linux command line tool for Playstation 2 OPL.</p>
  <p align="center">
    <a href="#about">About</a> · 
    <a href="#installation">Installation</a> · 
    <a href="#usage">Usage</a> · 
    <a href="#contributing">Contributing</a> ·
    <a href="./LICENSE">License</a>
  </p>
</div>

### About
**OPL Helper for Linux** is a command line tool created to simplify the use of Open PS2 Loader (OPL)
on PlayStation 2. With this tool, you can easily perform common tasks such as installing games
on PS2 HD or Pendrive, editing files from OPL configuration and installation of Playstation 1 games
and applications.

Is an open source project, written in Python, and is free to use and distribute.
Anyone is welcome to contribute to the project, whether it's reporting issues, submitting pull requests,
or improving the documentation.

We hope that **OPL Helper for Linux** can be useful for PS2 players who want to use OPL in a more efficient
and simplified way.

<div align="center">
  <img width="60%" src=".github/screenshot.png">
</div>

### Installation
Before using this script, you must have Python installed on your machine. You can download the latest version of Python [here](https://www.python.org/downloads/).

To download the latest version of the **OPL Helper for Linux** script, go to the [releases page](https://github.com/wesleydmscn/conf_apps-opl/releases)
and extract the **.zip** file to a folder containing your **APPS/** folder and **.elf** apps.

Once you have extracted the file, follow these commands in your terminal:

```bash
python main.py
```

This will create the **conf_apps.cfg** file in the same folder.

### Usage
For more detailed documentation on how to use the tool,
check out the [project's Wiki](https://github.com/wesleydmscn/conf_apps-opl/wiki).
The Wiki provides an overview of all the features and instructions on how to use them.

#### Quick usage tutorials:

- OPL APPS:
  To use the tool to list only OPL Apps, make sure you have the **APPS/** folder in the same directory as the tool and inside it files with the **.ELF** extension.

- OPL POPS:
  To use the tool to list only POPS(PS1) games, make sure you have the **POPS/** folder in the same directory as the tool and inside it the **POPSTARTER.ELF** file and game files with the **.VCD** extension.

> **Warning**
> An important tip about the tool is that **conf_apps.cfg** accumulates data, that is, be sure to add your application or PS1 game only once, if you want to redo the process from the beginning, delete the generated file **conf_apps.cfg** and run the **script**.

### Contributing
If you are interested in contributing to **OPL Helper for Linux**,
please read our [Contribution Guidelines](https://github.com/wesleydmscn/conf_apps-opl/blob/main/.github/CONTRIBUTING.md)
before submitting a pull request. You can also use the [GitHub Discussions](https://github.com/wesleydmscn/conf_apps-opl/discussions)
section to discuss a topic or ask questions. It is recommended to read the [Code of Conduct](https://github.com/wesleydmscn/conf_apps-opl/blob/main/.github/CODE_OF_CONDUCT.md)
before contributing.