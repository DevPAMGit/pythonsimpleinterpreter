from sys import argv

from interpreter import Interpreter

interpreter: Interpreter = Interpreter()
interpreter.interpret(argv)
