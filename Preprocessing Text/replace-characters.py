# Import library
import re

# Create text
text_data = ['Interrobang. By Aishwarya Henriette',
             'Parking And Going. By Karl Gautier',
             'Today Is The night. By Jarek Prakash']

# Remove periods
remove_periods = [string.replace('.', '') for string in text_data]

# Create function
def replace_letters_with_X(string: str) -> str:
    return re.sub(r'[a-zA-Z]', 'X', string)

# Apply function
[replace_letters_with_X(string) for string in remove_periods]
