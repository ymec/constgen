import argparse
import yaml
from constgen.config import RootConfig


def process_input(conf: RootConfig):
    outputers = [getattr(conf.outputs, x) for x in conf.outputs.__fields_set__]

    for outputer in outputers:
        outputer.output_header()
        outputer.output_comment("constants")
        for constant in conf.constants:
            outputer.output_constant(constant)
        outputer.output_comment("enums")
        for enum in conf.enums:
            outputer.output_enum(enum)
        outputer.output_footer()
    

def main():
    parser = argparse.ArgumentParser(description='ConstGen - Share constant definitions between programming languages.')
    parser.add_argument('input', type=str, help='input file in yaml format')
    args = parser.parse_args()

    with open(args.input, "r") as yaml_input:
        python_obj = yaml.safe_load(yaml_input)
        conf = RootConfig.parse_obj(python_obj)
        process_input(conf)


if __name__ == "__main__":
    main()
