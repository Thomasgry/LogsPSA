LogsPSA - Custom log message implementation
========================================================

THis module helps to store logs message easily.

You can install with:
	
	python setup.py install

Use case :

	>>> from LogsPSA import LogsPSA
	>>> lpsa	= LogsPSA(log="LogsPSA")
	>>> lpsa.error("test error")
	>>> lpsa.close()
	>>> lpsa.openFile()

Licence is MIT.
