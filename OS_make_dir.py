import os 

if not os.path.exists("Data"):
    os.mkdir("Data")

for i in range(100):
    os.mkdir(f"Data/Folder {i+1}")