with open("py_33_email_id.txt") as py_33_email:
    for mail in py_33_email.readlines():
        user_name = mail.split("@")[0]
        if user_name.isalnum():
            with open("user_num.txt", mode="a") as new_user_num:
                new_user_num.write(user_name)
                new_user_num.write("\n")
