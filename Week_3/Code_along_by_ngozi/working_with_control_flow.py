#if statement is used to print a block when the condition is true
age = 20
if age >= 18:
    print("you are eligible to vote")
# **Some usecases**

# - Checking for eligibility.

# - Validating login attempts.

# - Ensuring a minimum purchase requirement, etc.

#if-else statement : thus provides two alternative paths.
wallet = 400
price = 500
if wallet >= price:
    print("Purchase sucessful")
else:
    print("Insufficient balance")

# **Some usecases**

# - Deciding success or failure of a payment.

# - Granting or denying access to a system.

# - Determining pass/fail in an exam, etc.


#if-elif-else statement: this is used for multiple conditions

score = 85
if score >= 70:
    print("Grade")
