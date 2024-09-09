# Very Simple Parser from PlantUML to Draw.io 

## Overview

This parser is capable to understand PlantUML notation specific for C4 Model, as describe at Github project [plantuml-stdlib/C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML)

Only Context and Container diagrams are almost fully supported and the Component Diagram has partial support:

| Diagram       | Supported |
|---------------|-----------|
| C4_Context    | Most      |
| C4_Container  | Most      |
| C4_Component  | Some      |
| C4_Deployment | No        |
| C4_Dynamic    | No        |
| C4_Sequence   | No        |
| Tabs          | No        |

## Libraries

This project uses `Python 3.11` and commons libraries and `argparse` for command line arguments.
 - `pip install argparse`

## Usage

Justa call the `puml2drawio.py`:

```text
usage: puml2drawio.py [-h] [-p] [-o]

options:
  -h, --help            show this help message and exit
  -p , --plantuml_file  path to a PlantUML file. Default: 'resources/container1.puml'
  -o , --output_file    path to a Drawio file. If empty the output will be the terminal. Default: 'resources/container1.drawio'

```

Example:

```shell
python puml2drawio.py -p plantuml-diagram.puml -o diagram.drawio 
```