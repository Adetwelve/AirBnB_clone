#!/usr/bin/python3
""" This module defines a class `HBNBCommand` """
import cmd


class HBNBCommand(cmd.Cmd):
	"""contains the entry point of the command interpreter"""
	
	prompt = "(hbnb) "

	def do_quit(self, arg):
		"""  to exit the program """
		return True

	def do_EOF(self, arg):
		"""  to exit the program """
		return True
	
	def emptyline(self):
		"""  shouldn’t execute anything """
		return

if __name__ == '__main__':
	HBNBCommand().cmdloop()	
