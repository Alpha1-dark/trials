# #                              (Question 1:)	 	 	 	
# # A bank ATM requires users to enter their 4-digit PIN to access their account.
# # The system allows the user only three attempts to enter the correct PIN.
# # If the user enters the correct PIN, display "Access Granted!" and exit the program.
# # If the user fails three times, display "Your account is locked. Contact customer service."
# # ✅ Requirements:
# # Use a while 	loop to allow a maximum of three attempts.
# # Use an if-else 	condition to check if the PIN is correct or incorrect.
# # Display appropriate messages for each attempt.

# # SOLUTION.

# repeat = 0


# while repeat < 3:
#     pin = input("please enter your pin in here.  ")
#     if len(pin) == 4:
#         print(f"Access Granted your pin is:",pin)
#         break
#     else:
#         repeat +=1
#         print(f"incorrect pin. You have",3 - repeat,"attempts remaining.")

#     if repeat == 3:
#         print("Your account is locked. Contact customer service")
#         print("Please call on +256759167361")
                                             
#                                                    #  END.




##                                        (Question 2:)
# # A restaurant has the following menu:
# # 3.Pizza - $10
# # 4.Burger - $5
# # 5.Pasta - $7
# # Write a program that:
# # Displays the menu to the customer.
# # Asks them to enter a number corresponding to their order.
# # Prints the name of the item they ordered along with the total price.
# # If they enter a number that is not on the menu, display "Invalid choice. Please order from the menu."
# # ✅ Requirements:
# # Use if-elif-else to handle different choices.
# # Use input() to take user input.


# # SOLUTION.

# print("\nBelow is Our Menu Your Choice Metters.")
# print("3.Pizza")
# print("4.Burger")
# print("5.pasta")

# numbre = int(input("please enter the number corresponding to your order. "))

# if numbre == 3:
#     print("You have picked a Pizza.")
#     print("each Pizza costs $10 ")
# elif numbre == 4:
#     print("You have picked a Burger.")
#     print("each Pizza costs $5")
# elif numbre == 5:
#     print("You have picked Pasta.") 
#     print("each plate costs $7 ") 
# else:
#     print("Invalid choice. Please order from the menu by entering corresponding number to your order")   
                                                        
#                                                                   # END.       




# ##                           (Question 3:)
# ## Write a program that asks the user to enter a sentence and
# ## then counts the number of vowels (a, e, i, o, u) in the sentence.
# ## ✅ Requirements:
# ## Use a for loop to iterate through each letter in the sentence.
# ## Use an if statement to check if a letter is a vowel.
# ## Convert all letters to lowercase before checking.
# ## Print the total count of vowels.

# ## SOLUTION.

# sentence = input("please put here your sentence: ")

# vowels_count = 0

# Sentence = sentence.lower()

# print(f"\nSentence in lower-case: {Sentence}")

# for vowels in Sentence:

#     if vowels in Sentence:

#         vowels_count += 1
#     print(f"\nThe total count of vowels is: {vowels_count}")


#                             #   END. (tho still lacking!)


# ##                        (Question 4:)
# ## Create a simple banking system where a user can:
# ## Deposit money
# ## Withdraw money (only if they have enough balance)
# ## Check their balance
# ## Exit the system
# ## Write a program that starts with an initial balance of 
# ## $1000 and allows the user to perform any of these operations using a menu.
# ## ✅ Requirements:
# ## Use a while loop to keep the menu running until the user exits.
# ## Use if-elif-else to handle different operations.
# ## Ensure withdrawals do not exceed the balance.

# ## SOLUTION.

# balance = 1000  # Initial balance

# while True:
#     print("\nBanking System Menu:")
#     print("1. Deposit Money")
#     print("2. Withdraw Money")
#     print("3. Check Balance")
#     print("4. Exit")
        
#     choice = input("Enter your choice (1-4): ")
        
#     if choice == '1':
#         deposit = float(input("Enter the amount to deposit: "))
#         balance += deposit
#         print(f"\n${deposit:.2f} deposited successfully. New balance: ${balance:.2f}")
        
#     elif choice == '2':
#         withdrawal = float(input("Enter the amount to withdraw: "))
#         if withdrawal <= balance:
#             balance -= withdrawal
#             print(f"${withdrawal:.2f} withdrawn successfully. New balance: ${balance:.2f}")
#     else:
#         print("Insufficient balance. Transaction failed.")
        
#     if choice == '3':
#         print(f"Current balance: ${balance:.2f}")
        
#     elif choice == '4':
#         print("Exiting the system. Have a nice day!")
#         break
        
#     else:
#         print("invalid choise please try again.")

#    #                                 #END.



# #                                (Question 5:)
# # The local library has hired you to create their late fee calculator.
# # They need a program that helps the librarian calculate fees for overdue books.
# #     Their rules are:
# # - First 7 days late: $0.50 per day
# # - 8-14 days late: $1 per day
# # - More than 14 days: $2 per day plus a $10 processing fee
# # Write a program that:
# # a) Asks the librarian how many days the book is overdue
# # b) Calculates the total fee
# # c) Displays a clear breakdown of the charges
# # Example: If a book is 16 days late, the fee would be:
# # (7 × $0.50) + (7 × $1) + (2 × $2) + $10 processing fee
# # Your program should handle any number of days and give accurate results.

# # SOLUTION.

days_overdue = int(input("\npleaseenter the days the book is overdue: "))

print(f"\nBreak down of overdue chargesare as follows;\nFirst 7 days late the fee is (7 * $0.50) + 10 processing fee.")
print(f'\n8 - 14 days the charge is (7 * $0.50) + (7 *$1) + 10 processing fee.')
print(f'\nAbove 14 days the charge is (7 * $0.50) + (7 + $1) + ((Days overdue - 14) * 2) + 10 processing fee\n.')

if days_overdue == 7:
    print(f"\nYour overdue book(s) fees is ${(7 * 0.50) + 10}\n")
elif 8 >= days_overdue <= 14:
    print(f"\nyour overdue books(s) fee is $S{(7 * 0.50) + (7 * 1) + 10}\n")
elif days_overdue > 14:
     print(f"\nyour overdue books(s) fee is ${(7 * 0.50) + (7 * 1) + ((days_overdue -14) * 2)+ 10}\n")

    

