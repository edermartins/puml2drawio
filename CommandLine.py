from types import SimpleNamespace
import argparse

def lstm_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--plantuml_file', metavar="", type=str, help="path to a PlantUML file. Default: 'resources/container1.puml'", default='resources/container1.puml')
    parser.add_argument('-o', '--output_file', metavar="", type=str, help="path to a Drawio file. If empty the output will be the terminal. Default: 'resources/container1.drawio'", default='resources/container1.drawio')
    args = parser.parse_args()
    lstm_wrapper_values = {
        "plantuml_file" : args.plantuml_file,
        "output_file" : args.output_file
    }
    return SimpleNamespace(**lstm_wrapper_values)



