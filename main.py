import password_cracker

print("Welcome to my SHA1 password cracker.\n")
print("Type your hash below\n")
hash = input(">"); 
print("Try to crack using a known salt list?\n")
print("1: Yes")
print("2: No")
salted = input(">"); 
try:
  saltedNum = int(salted)
  if(saltedNum == 1):
    result = password_cracker.crack_sha1_hash(hash,True) 
    print("Checking the database for a match:\n")
    print(result)
  elif(saltedNum == 2):
    result = password_cracker.crack_sha1_hash(hash,False) 
    print("Checking the database for a match:\n")
    print(result)
  else:
    print("Input not recognized. Shutting down.")
    exit(0)
except ValueError:
  print("Received input is not a number. Shutting down.")
  exit(0);


