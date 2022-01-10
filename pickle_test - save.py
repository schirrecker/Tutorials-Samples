import pickle

friends = {"Alois" : ["Andre", "Chris", "Blake", "Reef", "Austin", "Reece", "Nadav"],
           "Stephan" : None,
           "Ismene" : ["Maddie", "Aya"]
           }

    
# Save to file

file_path = "friends.bin"
with open (file_path, 'wb') as f:
    pickle.dump(friends, f)

print ("State saved.")


