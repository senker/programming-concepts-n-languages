# a. Create the dictionary with initial key-value pairs
specialle = {
    "Bob Builder": "IoT",
    "Dora Explorer": "Interactive Media",
    "Paw Patrol": "Data Engineering"
}

# b. Change Bob Builder's specialization to Data Engineering
specialle["Bob Builder"] = "Data Engineering"

# c. Add a new entry for "Farmer Pickles" with specialization "Climate Engineering"
specialle["Farmer Pickles"] = "Climate Engineering"

# d. Print Dora's specialization
print("Dora's specialization is:", specialle["Dora Explorer"])

# e. Print all the keys
print("The keys in the specialle dictionary are:")
for key in specialle:
    print(key)

# f. Print a string 5 times
print("This program prints a string 5 times")
for count in range(5):
    print("Python is cool")
