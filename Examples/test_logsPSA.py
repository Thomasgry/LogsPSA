from LogsPSA import LogsPSA

def main():
	lpsa = LogsPSA("test_logsPSA")
	lpsa.info("test")
	lpsa.close()
	lpsa.openFile()

if __name__ == "__main__":
	main()
	
