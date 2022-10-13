"""Demonstrations of dicitonary capabilities"""


# Declarng the type of a dictionary 
schools: dict[str, int]

# Intialize to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dicitonary 
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150 

# Print a dicitonary literal representation 
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary 
# by its key.
schools.pop("Duke")

# Test for the existence of a key 
is_duke_present: bool = "Duke" in schools 
print(f"Duke is present: {is_duke_present}")

# can also do this 
# if "Duke" in schools:
#    print("Found the key 'Duke' in schools")
# else:
#   print("No key 'Duke in schools")

# Update / Reassign a key-value pair 
schools["UNC"] = 20000
schools["NCSU"] += 200 

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal 
schools = {} # Same as dict()
print(schools)

# Alternatively, intialize key-value pairs 
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print (schools) 

# What happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict 
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")