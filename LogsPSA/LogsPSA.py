#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Class to logs userfriendly log messages
	
	Usage :
	
	>>> from LogsPSA import LogsPSA
	>>> lpsa	= LogsPSA(log="LogsPSA")
	>>> lpsa.error("test error")
	>>> lpsa.close()
	>>> lpsa.openFile()
"""
import os,re,sys
from datetime import datetime

__all__ = ['LogsPSA']

class LogsPSA:
	"Definition d une classe de logs pour PSA"
	
	def __init__(self,log=None,path=os.environ.get('PYTHONLOGS'),d=0):
		self.debug			= d
		## verification affection log file name
		if log is None:
			raise Exception('option "log" (file name) is required')
			
		## affectation d'un fichier de sortie
		self.log	= path + "\\" + log + "." + str(os.getpid()) + ".log"
			
		if(self.debug):
			print ("fichier de log" + self.log + "\n")
		
		self.LOG	= open(self.log,'a')
		self.info("Starting")
			
	def close(self):
		self.info("Ending")
		print ("Fichier de log : " + self.log + "\n")
		self.LOG.close()
	
	def write(self,text="",level=""):
		self.LOG.write(str(datetime.now()) + ";"+ level +";" + text + "\n")
		
	def debug(self,text):
		self.write(level="DEBUG",text=text)
		
	def info(self,text):
		self.write(level="INFO",text=text)
		
	def warning(self,text):
		self.write(level="WARNING",text=text)
		
	def error(self,text):
		self.write(level="ERROR",text=text)
		
	def openFile(self):
		"Ouvrir le fichier de sortie"
		os.startfile(self.log)

if __name__ == "__main__":
	lpsa	= LogsPSA(log="LogsPSA")
	lpsa.error("test error")
	lpsa.warning("test warning")
	lpsa.info("test info")
	lpsa.close()
	lpsa.openFile()
