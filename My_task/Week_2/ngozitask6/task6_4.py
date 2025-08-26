#4. Create a unique Voters Registration System
print("Enter your name")

voter_names_1 = input("Enter your name")
voter_names_2 = input("Enter your name")
voter_names_3 = input("Enter your name")
voter_names_4 = input("Enter your name")
voter_names_5 = input("Enter your name")
# voters_names = {voter_names_1, voter_names_2, voter_names_3,voter_names_4,voter_names_5}

# voters = [voter_names_1, voter_names_2, voter_names_3,voter_names_4,voter_names_5]
voters = set()
for voter in  [voter_names_1, voter_names_2, voter_names_3,voter_names_4,voter_names_5]:
    if voter in voters:
        print(f"warning: {voter} has already registered.")
    else:
        voters.add(voter)
print("\nTotal number of voters:", len(voters))
print("Voters list:",",".join(voters))
