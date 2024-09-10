#print("hello")

p=["Merkurs", "Venēra", "Zeme", "Marss", "Jupiters", "Saturns", "Urāns", "Neptūns"]

a=len(p)
print(f"Saules sistēmā ir {a} planētas.")

for i, item in enumerate(p,1):
    print(f"{item,i}.vieta")