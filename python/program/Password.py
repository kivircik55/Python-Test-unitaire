import re

class Password:

    def validate_password(self, password):
        special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        password_list = ["azertyuiop", "qwertyuiop", "1234567890", "administrator", "password", "motdepasse", "abcdef"]

        password_len = len(password)

        if password_len < 10 or password_len > 25:
            print("Password length is not correct please change your password.")
            return False

        if not re.search(r"[\d]+", password) or not re.search(r"[A-Z]+", password) or not re.search(r"[a-z]+", password) or not any(c in special_characters for c in password):
            print("The password must contain at least 1 digit, 1 uppercase letter, 1 lower case letter and 1 special character.")
            return False

        if password in password_list or any(word for word in password_list if word in password):
            print("Please change your password into a strong password.")
            return False

        else:
            print("Your password is valid.")
            return True

password = Password()
password.validate_password("abcdefhjvkznvBJB9/")