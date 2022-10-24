# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File two output when __name__ is equal to __main__; in other words when called directly")
else:
   print("File two executed when imported")