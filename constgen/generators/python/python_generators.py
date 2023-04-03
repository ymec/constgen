from constgen.generators.common import Outputer, Constant, Enum
import inflection


class Python2Outputer (Outputer):

    def output_enum(self, constant : Constant):
        super().output_enum(constant, prefix=f"{inflection.underscore(constant.name).upper()}_")


class Python3Outputer (Outputer):

    def output_header(self):
        super().output_header()
        self._output.write("from enum import Enum\n")

    def output_enum(self, enum : Enum):
        self._output.write(f"class {enum.name}(Enum):\n")
        super().output_enum(enum, prefix=f"\t")
        self._output.write(f"\n")
