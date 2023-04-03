from constgen.generators.common import Enum
from constgen.generators.javascript import JavascriptOutputer
import textwrap


# idea from https://stackoverflow.com/a/65734013/495995
class VueMixinOutputer(JavascriptOutputer):

    def output_enum(self, enum: Enum):
        super().output_enum(enum)
        name = enum.name
        self._output.write(textwrap.dedent(f"""\

            {name}.Mixin = {{
              created () {{
                  this.{name} = {name}
              }}
            }}
            """))
