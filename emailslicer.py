email = input("Enter Your Email: ").strip() # full email + breaks down email
username = email[:email.index("@")] # the part of the email before the @
domain_name = email[email.index("@")+1:] # the part of the email after the @
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'") # breaks down email
print(format_) # prints the email breakdown
