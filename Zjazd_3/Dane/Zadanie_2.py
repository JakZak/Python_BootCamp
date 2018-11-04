# import sys
# last_login = {}
# users = {}
# if len(sys.argv) > 1:
#     nazwa_pliku = sys.argv[1]
#     email = set()
#     with open(nazwa_pliku) as f:
#         for line in f:
#             email=line.split("\n")
#             print(email)
#     print(type(email))
#         for i in email:

def validate_email(line):
    line = line.strip().lower()
    if line.count('@') == 1:
        return line

import sys

if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    emails = set()
    with open(input_file) as f:
        for line in f:
            email = validate_email(line)
            if email:
                emails.add(email)
            print(emails)