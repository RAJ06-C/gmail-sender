# THIS PYTHON CODE IS WRITTEN TO SEND THE EMAILS USING THE PYTHON LANGUAGE
# Steps required:
# - Go to Gmail and enable 2-step authentication in your account (email sender)
# - Generate an app password
# - Run this script

# Required packages
import email
import keyboard
import ssl
import smtplib
from email.message import EmailMessage

# Function to input the email body
def body_input():
    cond = True
    email_body = []
    print("Enter your message. Press esc to finish and exit.")
    while cond:
        # Check if the ESC key is pressed
        if keyboard.is_pressed('esc'):
            print("\nESC key pressed, exiting...")
            cond = False
            break
        
        # Get input from the user (single line of the email body)
        user_input = input()  # Wait for user input
        
        if user_input == "":  # If the user presses Enter without typing anything
            print()  # Print a blank line (go to a new line)
            continue  # Continue to the next iteration
        
        # Add the input line to the email body list
        email_body.append(user_input)
        
        # Optionally, you can print the entered line immediately
        print(f"Line added: {user_input}")

    # After the loop ends, join the list and print the entire email body content
    email_content = "\n".join(email_body)

    # Return the entire email body as a string
    return email_content

# Main execution
if __name__ == "__main__":
    print('Welcome!')
    print('\nGo to Gmail and enable 2-step authentication in your account email sender.')
    print('Generate an app password\n')
    
    # Input email details
    sender_email = input("Enter sender email: ")
    app_key = input("Enter the app password: ")
    receiver_email = input("Enter the receiver email: ")
    subject = input("Enter the subject: ")
    
    # Get the email body
    message = body_input()
    
    print("\n--- Entire message entered by the user ---")
    print(f'\n{message}\n')
    
    # Create email message
    em = EmailMessage()  # Corrected the creation of the EmailMessage instance
    em["From"] = sender_email
    em["To"] = receiver_email
    em["Subject"] = subject
    em.set_content(message)  # Set the plain text content of the email
    
    # Set up SSL context
    context = ssl.create_default_context()

    # Sending the email using SMTP with SSL (port 465 for SSL)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender_email, app_key)
            smtp.sendmail(sender_email, receiver_email, em.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
