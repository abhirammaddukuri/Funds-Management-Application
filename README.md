# Funds-Management-Application
The Funds Management Application is a simple and intuitive tool designed to help users manage their funds by tracking depositors, adding deposits, spending money, and displaying balances. Built using KivyMD, this application provides a user-friendly interface for managing financial contributions from multiple depositors.
# Features: 
Add Depositor: Users can add depositors along with the amount they contribute.
Spend Money: Users can spend a specified amount, which will be split among selected depositors.
Show Balances: Users can view the current balances of all depositors and the total funds available.
Installation
To run the application, ensure you have Python and KivyMD installed. You can install KivyMD using pip:

# bash code :
pip install kivymd
# Usage
Add Depositor:

Enter the depositor's name in the "Depositor Name" field.
Enter the amount in the "Amount" field.
Click the "Add Depositor" button to add the depositor.
Spend Money:

Enter the amount to spend in the "Amount to Spend" field.
Enter the names of the depositors (comma-separated) in the "Enter depositors (comma-separated)" field.
Click the "Spend Money" button to deduct the amount from the selected depositors.
Show Balances:

Click the "Show Balances" button to display the current balances of all depositors and the total funds.
# Code Structure
FundManager Class: Manages the depositors and their balances, handles adding depositors, spending money, and showing balances.
FundApp Class: The main application class that builds the user interface and connects user actions to the FundManager.
Example
# Here is a brief example of how to use the application:

Add a depositor named "Alice" with an amount of ₹1000.
Add another depositor named "Bob" with an amount of ₹500.
Spend ₹300, selecting both Alice and Bob, which will deduct ₹150 from each.
Show balances to see the updated amounts.
# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

# Acknowledgments
KivyMD for providing a great framework for building the application.
Open-source community for their continuous support and contributions.
