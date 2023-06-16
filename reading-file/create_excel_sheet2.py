from openpyxl import Workbook

# Create a new workbook
workbook = Workbook()
sheet = workbook.active

# Define the questions from the forms
questions = [
    "Homework - Week 3",
    "First Name",
    "Last Name",
    "1. Install a VPN app of your choice, connect and share the screenshot here. (See example)",
    "Captionless Image",
    "2. When is the May bank holiday next year?",
    "3. What are the opening times of Sky Garden on a Sunday?",
    "4. Go to Indeed and search for how many ads there are for carpenter jobs in Brighton, East Sussex, posted in the last 2 weeks in a 5-mile radius. Put the number of jobs found.",
    "5. Using the TfL website, find how you can go to the Royal Observatory from The Museum of London. Using the Maps app, find how you can go to the Royal Observatory from The Museum of London. Take a screenshot for both cases and schedule to send to Diego's email on Sunday at 5:00 a.m.",
    "What option did you find more useful?",
    "TfL website",
    "Maps app",
    "6. Find out top 3 websites from where you can buy flowers. List them here.",
    "7. What is the monthly fee for a Current Account in Triodos Bank?",
    "8. Which of these banks DO NOT offer a cash deposit service?",
    "Monzo",
    "Starling",
    "Revolut",
    "Monese",
    "9. Scan the last junk mail you received at home (paper) or a poster nearby and upload it as a pdf in color.",
    "10. Search for the best price for Russell Hobbs Classic Glass Kettle (26080) and paste the link here. Be cautious of suspicious websites.",
    "Comments about the Homework"
]

# Write questions to the Excel sheet
for index, question in enumerate(questions):
    sheet.cell(row=index+1, column=1, value=question)

# Save the Excel file
workbook.save("questions-Homework-Week3.xlsx")
