<div align="center">
  <img width="60%" height="80" src="./.github/logotipo.svg">
  <p align="center">Configuration file generator conf_apps for Playstation 2 OPL.</p>
  <p align="center">
    <a href="#about">About</a> · 
    <a href="#installation">Installation</a> · 
    <a href="#usage">Usage</a> · 
    <a href="#contributing">Contributing</a> ·
    <a href="#license">License</a>
  </p>
</div>

### About
**conf_apps-opl** is a Python-based scripting tool designed to automate the listing of apps for the Playstation 2 OPL. This open source project aims to provide a cross-platform solution for creating **.cfg** files that list **.elf** applications in the **APPS/** folder. Currently, the tool already supports the listing of PS1 games, but this feature is still in **beta** and may present bugs.

<div align="center">
  <img width="60%" src=".github/screenshot.png">
</div>

### Installation
Before using this script, you must have Python installed on your machine. You can download the latest version of Python [here](https://www.python.org/downloads/).

To download the latest version of the **conf_apps-opl** script, go to the [releases page](https://github.com/wesleydmscn/conf_apps-opl/releases) and extract the **.zip** file to a folder containing your **APPS/** folder and **.elf** apps.

Once you have extracted the file, follow these commands in your terminal:

```bash
cd conf_apps-opl
python main.py
```

This will create the **conf_apps.cfg** file in the same folder.

### Usage
For more detailed documentation on how to use the tool, check out the [project's Wiki](https://github.com/wesleydmscn/conf_apps-opl/wiki). The Wiki provides an overview of all the features and instructions on how to use them.

#### Quick usage tutorials:

- OPL APPS:
  To use the tool to list only OPL Apps, make sure you have the **APPS/** folder in the same directory as the tool and inside it files with the **.ELF** extension.

- OPL POPS:
  To use the tool to list only POPS(PS1) games, make sure you have the **POPS/** folder in the same directory as the tool and inside it the **POPSTARTER.ELF** file and game files with the **.VCD** extension.

> **Warning**
> An important tip about the tool is that **conf_apps.cfg** accumulates data, that is, be sure to add your application or PS1 game only once, if you want to redo the process from the beginning, delete the generated file **conf_apps.cfg** and run the **script**.

### Contributing
If you are interested in contributing to **conf_apps-opl**, please read our [Contribution Guidelines](https://github.com/wesleydmscn/conf_apps-opl/blob/main/.github/CONTRIBUTING.md) before submitting a pull request. You can also use the [GitHub Discussions](https://github.com/wesleydmscn/conf_apps-opl/discussions) section to discuss a topic or ask questions. It is recommended to read the [Code of Conduct](https://github.com/wesleydmscn/conf_apps-opl/blob/main/.github/CODE_OF_CONDUCT.md) before contributing.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.