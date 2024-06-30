import re
import string
import secrets

def password_generetor(length=8,nums=1,lower_case=1,upper_case=1,special_chars=1):
    num = string.digits
    letter = string.ascii_letters
    special_symbols = string.punctuation
    everything = num+letter+special_symbols

    while True:
        password = ''
        for _ in range(length):
            password += secrets.choice(everything)
            conditions = [
                        (nums,r'\d'),
                        (lower_case,r'[a-z]'),
                        (upper_case,r'[A-Z]'),
                        (special_chars,rf'[{special_symbols}]')
                          ]
        if all(condition <= len(re.findall(pattern,password)) for condition,pattern in conditions):
                break
        return password

if __name__ == '__main__':
    new_password = password_generetor(length = 5)
    print('Generated password:', new_password)
            
#In the same way the [0-9] class is equivalent to \d, the [^0-9] class is equivalent to \D. Alphanumeric characters can be matched with \w and non-alphanumeric characters can be matched with \W. Alphanumeric means the characters which are letters(lower or upper) and digits but the non alphanumeric means the characters other than letter or numbers like !,. etc.. the r actually handle the regex object and deals with forward slash and it counts forward slash as an actual character rather than an escaping character. ^a matches any string that starts with the letter "a".


# [^a] matches any single character that is not "a".
# ^[a-z] matches any string that starts with a lowercase letter.
# [^a-z] matches any single character that is not a lowercase letter.

#\W Character Class:

# \W: This is the inverse of the \w character class. It matches any character that is not a "word" character.
# Equivalent to: It is equivalent to the character set [^a-zA-Z0-9_], which means it matches any character that is not a letter, digit, or underscore.

# Special Characters: Because \W does not match underscores (since underscores are included in \w), it cannot be used to match all special characters if you want to include the underscore as a special character.





