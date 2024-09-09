from parser.DrawioParser import DrawioParser
from CommandLine import lstm_command_line_args

# Get command line arguments or default values if not arguments
args = lstm_command_line_args()

p2d = DrawioParser()
p2d.parser(args.plantuml_file)
result = p2d.generate_drawio(args.output_file)
if result:
    print(result)
