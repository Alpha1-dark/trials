#                               (QUESTION 1)
# You run a small cinema and need a booking system for customers to reserve tickets. Your system should:
# Ask for the customer's name
# Ask how many tickets they need
# Charge $12 per ticket
# Print a booking confirmation showing their name, number of tickets, and total cost in a polite and engaging way


# CINEMA BOOKING SYSTEM.

name_of_the_customer = input("Please fill in your name... ")

ticket_number = int(input("Please enter the number of tickets you want... "))

print(f"Your ticket(s) cost $",12 * ticket_number)

print(f"Your tickets booking has been confirmed Mr/Mis",name_of_the_customer,)
print(f"Your number of ticket(s) is",ticket_number,) 
print(f"And your total cost is $",12 * ticket_number)
print("Thank you for your support.")

                                                       #    END.



#                              (QUESTION 2)
# You're building a login or sign-up system for a website. Users enter their email addresses. 
# And the system extracts useful information for display or validation.
# You're developing a registration system for a social media app.
# When users sign up, they need to choose a username that meets Instagram’s character limit of 30 characters.
# System Requirements:
# Ask the user to enter a username.
# Check if the username is 30 characters or less.
# Inform the user whether the username is valid or too long.
# Show the number of characters used.


# REGISTRATION SYSTEM FOR A SOCIAL MEDIA APP.

user_name = input("please put your user name here..")

if len(user_name) < 30:
    print('user name acceped')
elif len(user_name) > 30:
    print('invalid user name is too long.')
    print('please enter a user name with characters not exceeding 30 in number.')

                                                           # END.



#                            (QUESTION 3)
# You're filling out a form on a website.
# And the system needs to process your email address to personalize your experience.
# A website needs to extract information from users' email addresses for personalization.
# Write a program that:
# Takes an email address as input (e.g., student@school.com)
# Extracts and prints the username (everything before @)
# Extracts and prints the domain name (everything after @)


# BUILDING A FORM WEBSITE.

email_address = input("Please enter here you email address. ")

partistion = email_address.partition('@')

print(f"Your user name is; ",partistion[0])

print(f"Your domain name is; ",partistion[2])

                                           # END.




#                                (QUESTION 4)
# You're filling out an online form or signing up for a service that requires a valid phone number.
# The system should format your number correctly for readability and notify you if there's an issue.
# A customer service system needs to properly format phone numbers.
# Write a program that:
# Takes a 10-digit phone number as input (e.g., 1234567890)
# Formats it using string slicing as (123) 456-7890
# Prints the formatted number
# Displays an error if the number isn't exactly 10 digits



# ONLINE SITE FOR VALID PHONE NUMBER.

phone_number = input("please enter here your phone numbre:  ")

#  FORMULAR ONE.

import re
def the_valid_number(phone_number):
    working = r'^\d{10}$'
    return bool(re.match(working,phone_number))


if the_valid_number(phone_number):
    print("your phone number is valid congra congra.")
else:
    print("your phone number is invalid please only put ten characters.")

# FORMULAR TWO.

if len(phone_number) == 10: 
    print("valide phone number congra congra.")
else:
    print("invalide phone number please enter 10 characters.") 

formated_numbre = (f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}")
print(formated_numbre)    

#                                                            END.       




#                                   (QUESTION 5)
# You're developing a user registration system for an online service,
# and you need to validate email addresses to ensure they are properly formatted.
# A registration system needs to check if an email address is valid. Write a program that:
# Asks the user to enter an email address
# Checks if the email contains both @ and .
# Prints "Valid email" if both are present, otherwise prints "Invalid email"

# REGISTRATION SYSTEM.

#SOLUTION.

email_address = input("please input your email address here:  ")

if "@" in email_address and "." in email_address:
    print("Valid email congra congra.")
else:
    print("Invalid email please check your email well if it has '@' and '.' symble.") 
                                                                    
#                                                                            END.   



#                                    (QUESTION 6)
# Question: You are building a tool for formatting a list of words entered by a user. 
# The user enters a sentence with words separated by spaces,
#  and your task is to display the words in the sentence but joined together with hyphens instead of spaces.
# Write a Python program that:
# Takes a sentence as input from the user.
# Splits the sentence into individual words.
# Joins these words with hyphens (-) and prints the result.
# Example:
# Input: "Python is awesome"
# Output: "Python-is-awesome"


  # SOLUTION.

sentence = input("please write your desired sentence here: ")

formatted_words = sentence.split()
out_come = "-".join(formatted_words)

print("splited sentence: ",formatted_words)

print("joint words with hyphens: ",out_come)

                                   #  END.


 
#                                   (QUESTION 7)
# You're developing a text-processing tool for analyzing and manipulating sentences.
# The tool will help users with basic text analysis, formatting, and checking for specific keywords.
# A text analysis system needs to process a sentence. Write a program that:
# Asks the user to input a sentence
# Counts the number of words in the sentence (assuming words are separated by spaces)
# Converts the sentence to lowercase and prints it
# Uses slicing to reverse the sentence and prints it
# Checks if the sentence contains the word "Python" (case-insensitive) and prints
# "This sentence is about Python!" if true.


# SOLUTION.

sentence = input("please write here your desired statement: ")

words_numbre = len(sentence.split())
print("number of words is ",words_numbre)

lowercase_sentence = sentence.lower()
print("Sentence in lowercase: ",lowercase_sentence)

reversed_sentence = (lowercase_sentence[::-1])
print("Reverse sentence: ",reversed_sentence)

if "python" in lowercase_sentence:
    print("This sentence is about Python!")
else:
    print("This sentence is not about python!")    

                                   #    END.

#                                (QUESTION 8)
# You're building a security feature for an account creation or login system that checks the
# strength of the password provided by users.

# A security system needs to evaluate the strength of a password. Write a program that:
# Asks the user to input a password
# Checks if the password is at least 8 characters long
# Checks if the password contains either letter or digit
#Prints "Strong Password" if both conditions are met, otherwise prints "Weak Password"
# Uses slicing to print the first half of the password


# SOLUTION.

password = input("please enter your password here: ")
counted = password.count()

if len(counted) > 8:
    print("Strong Password.")
else:
    print("Weak Password at least it should contain 8 characters and mixed with letters and numbers.")   