import pickle

# Load from file

file_path = "friends.bin"

with open(file_path, 'rb') as f:
    friends = pickle.load(f)

print ("State loaded:")
print(friends)
print (friends["Alois"])

