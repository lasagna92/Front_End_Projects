class Email(object):
    """
    Create a class definition for emails
    Set the two variables:
    has_been_read = false
    is_spam = false
    """
    has_been_read = False
    is_spam = False

    # Initialise the sender address and the email content
    def __init__(self, from_address, email_content):
        """
        create two instance
        from_address
        email_content
        """
        self.from_address = from_address
        self.email_content = email_content

    def mark_as_read(self):
        """
        this method change the value of the variable has_been_read to true
        :return: has_been_read = True
        """

        Email.has_been_read = True

    def mark_as_spam(self):
        """
        this method change the value of the variable is_spam to true
        :return: is_spam = True
        """
        Email.is_spam = True


# Create an empty list with the class objects
inbox = [Email('test@gmail.com', 'test'), Email('hello@gmail.com', 'hello')]

for obj in inbox:
    i = obj.email_content       # Save the email contents of the inbox list in a variable


def add_email():
    """
    Function to send emails to the inbox creating a new class object
    """
    inbox_content = str(input('\nEmail content:\t'))
    inbox_address = str(input('\nEmail address:\t'))
    inbox.append(Email(inbox_address, inbox_content))


def get_email():
    """
    Function to retrieve an email by his index number
    """
    content = []
    for obj in inbox:       # Loop through the inbox list
        email_c = obj.email_content
        content.append(email_c)
    try:
        i = int(input('Read an email by his index position:\n'))        # Index input
        email = content[i]
        print(email)        # Print the chosen email
        inbox[i].has_been_read = True       # Mark the email as read
        print('\nThe email has been mark as read\n')
    except IndexError:
        print('List index out of range. Please try again!\n')


def get_count():
    """
    Function to get the count of all the emails in the inbox list
    """
    counter = 0
    for c in inbox:
        counter += 1
    print(counter)


def get_unread_email():
    """
    Function to get a list of all the unread emails
    """
    unread = []
    for obj in inbox:
        if not obj.has_been_read:
            unread.append(obj.email_content)
    print(f'\nYour unread emails: {unread}')


def get_spam_email():
    """
    Function to get a list of all the email marked as spam
    """
    spam = []
    for obj in inbox:
        if obj.is_spam:
            spam.append(obj.email_content)
    print(f'Your spam emails: {spam}')


user_choice = ""
# Menu for the user input
while user_choice != "quit":
    user_choice = input("\nWhat would you like to do - read all / count / display spam / display unread / "
                        "mark as spam / send / mark as read / send / quit?\t")
    # Read the emails
    if user_choice == "read all":
        print('\nAll your email:')
        for obj in inbox:
            i = obj.email_content
            print(i)        # Display all the emails
        # Call the function get_email
        get_email()

    elif user_choice == 'count':
        # Display the count of all the emails calling the function get_count
        print('\nThe count of all your emails is: ', end=' ')
        get_count()

    elif user_choice == 'display unread':
        # Display the unread emails
        get_unread_email()

    elif user_choice == 'display spam':
        # Display the spam emails
        get_spam_email()

    # Mark emails as spam
    elif user_choice == "mark as spam":
        while True:
            content = []
            for obj in inbox:       # Loop through the inbox list
                email_s = obj.email_content
                content.append(email_s)
                content_str = '\n'.join(content)
            print(content_str)      # Print the email content
            try:
                # User choose the email by his index number
                i = int(input('\nPlease enter the index position of the email you want to mark as spam:\n'))
                email = content[i]
                print(email)
                inbox[i].is_spam = True     # Mark the chosen email as spam
                print('\nThe email has been mark as spam!\n')
                break
            except IndexError:
                print('List index out of range. Please try again!\n')
    # Mark email as read
    elif user_choice == 'mark as read':
        while True:
            content = []
            for obj in inbox:       # Loop through the inbox list
                email_s = obj.email_content
                content.append(email_s)
                content_string = '\n'.join(content)
            print(content_string)       # Print the emails content
            try:
                # User choose the email to mark by his index number
                i = int(input('\nPlease enter the index position of the email you want to mark as read:\n'))
                email = content[i]
                print(email)
                inbox[i].has_been_read = True       # Mark the email as read
                print('\nThe email has been mark as read!\n')
                break
            except IndexError:
                print('List index out of range. Please try again!\n')
    # Call the function to send email to the inbox object list
    elif user_choice == "send":
        add_email()

    elif user_choice == "quit":
        print("Goodbye")

    else:
        print("Oops - incorrect input")
