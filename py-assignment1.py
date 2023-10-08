""" 
- Recipient's name
- Year of birth
- Personalized message
- Sender's name
"""

# variable needed
recipient_name = input("Hi, what's your name? ")
print("Your name is {}". format(recipient_name))

year_of_birth = int(input("Please enter your year of birth. "))

current_year = 2023 - int(year_of_birth)
print("Your age is {}". format(current_year))

print(
    f"{recipient_name}, let's celebrate your {current_year} years of awesomeness!"
    )
print(
    f"Wishing you a day filled with joy and laughter as you turn {current_year}!"
    )

personalized_messsage ="Happy birthday!! Wishing you success and happiness in your future." 
print(personalized_messsage)

sender_name = "Li"
print("With love and best wishes,")
print(sender_name)