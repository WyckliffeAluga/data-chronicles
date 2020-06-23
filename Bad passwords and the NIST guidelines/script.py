
# coding: utf-8

# Importing the pandas module
import pandas as pd
# Loading in datasets/users.csv
users = pd.read_csv('datasets/users.csv')

# Printing out how many users we've got
print(users.shape[0])
# Taking a look at the 12 first users
users.head(12)

# Calculating the lengths of users' passwords
users['length'] = users['password'].str.len()

# Flagging the users with too short passwords
users['too_short'] = users['length'] < 8

# Counting and printing the number of users with too short passwords
print(users['too_short'].sum())
# Taking a look at the 12 first rows
users.head(12)

# Reading in the top 10000 passwords
common_passwords = pd.read_csv('datasets/10_million_password_list_top_10000.txt', header=None, squeeze=True)

# Taking a look at the top 20
common_passwords.head(20)

# Flagging the users with passwords that are common passwords
users['common_password'] = users['password'].isin(common_passwords)

# Counting and printing the number of users using common passwords
print(users['common_password'].sum())

# Taking a look at the 12 first rows
users.head(20)


# Reading in a list of the 10000 most common words
words = pd.read_csv('datasets/google-10000-english.txt', header=None, squeeze=True)

# Flagging the users with passwords that are common words
users['common_word'] = users['password'].str.lower().isin(words)

# Counting and printing the number of users using common words as passwords
print(users['common_word'].sum())

# Taking a look at the 12 first rows
users.head(12)

# Extracting first and last names into their own columns
users['first_name'] = users['user_name'].str.extract(r'(^\w+)', expand = False)
users['last_name'] = users['user_name'].str.extract(r'(\w+$)', expand = False)

# Flagging the users with passwords that matches their names
users['uses_name'] = (
    (users['password'].str.lower() == users['first_name']) |
    (users['password'].str.lower() == users['last_name']))

# Counting and printing the number of users using names as passwords
print(users['uses_name'].sum())
# Taking a look at the 12 first rows
users.head(12)

### Flagging the users with passwords with >= 4 repeats
users['too_many_repeats'] = users['password'].str.contains(r'(.)\1\1\1')

# Taking a look at the users with too many repeats
users[users['too_many_repeats']]


# Flagging all passwords that are bad
users['bad_password'] = (
    users['too_short'] |
    users['common_password'] |
    users['common_word'] |
    users['uses_name'] |
    users['too_many_repeats'] )

# Counting and printing the number of bad passwords
print(users['bad_password'].sum())
# Looking at the first 25 bad passwords
users['password'][users['bad_password']].head(25)
