import argh

__doc__ = """
Usage Instructions

from arghparser import Parser

parser = Parser()

@parser.reg
def command1(arg1, arg2=kw2):
	pass

parser.dispatch()
"""

class Parser(argh.ArghParser):
    def reg(self, func):
        self.add_commands([func])
        return func