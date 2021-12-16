import os
files = {}
opt = {}
for file in os.listdir(f"{os.getcwd()}/tests/"):
  if file.endswith(".py"):
    files[file] = file
amt = 1
print("MENU:")
for item in files:
  print(f"{amt}. {item}")
  opt[str(amt)] = item
  amt += 1
query = input("INPUT NUMBER: ")
tr = opt[query]
os.system(f"cd {os.getcwd()}/tests/ && python {tr}")
  
