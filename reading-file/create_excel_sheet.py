from openpyxl import Workbook

# Create a new workbook
workbook = Workbook()
sheet = workbook.active

# Define the questions from the forms
questions = [
    "Day-to-day Digital Skills Course Registration",
    "Do you feel there's a lot more to your mobile phone than what you already know?",
    "Do you think you could improve your life if only you could learn to make better use of your phone?",
    "This is an in-person training program.",
    "This free course is between 3-5 weeks long, depending on regional arrangements.",
    "The specific times and dates will be available according to the city-region you choose, and you would need to attend all classes to be eligible for the certificate of completion.",
    "For more information, please go to https://codeyourfuture.io/dds/.",
    "Personal Information",
    "Thank you for your interest. To proceed, we need to collect some basic, personal information.",
    "First Name",
    "Last Name",
    "Email address",
    "Home Address",
    "Postcode",
    "Mobile Number (with country code)",
    "Household Income (per month)",
    "Number of people in the household",
    "Are you a refugee or an asylum seeker?",
    "Where did you hear about this program?",
    "Which CodeYourFuture region are you applying to?"
]

# Write questions to the Excel sheet
for index, question in enumerate(questions):
    sheet.cell(row=index+1, column=1, value=question)

# Save the Excel file
workbook.save("questions.xlsx")
