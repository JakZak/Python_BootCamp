import re

# pattern = re.compile("\d{3}-\d{3}-\d{3}")
kod_pocztowy = re.compile("^\d{2}-\d{3} | \d{2}-\d{3} | \d{2}-\d{3}$")
# adres_email = re.compile("(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)")
data = re.compile ("\d{2} \w{3} \d{4}")
with open ("input.txt") as f:
    text = f.read()
    print(kod_pocztowy.findall(text))
    # print(adres_email.findall(text))
    print(data.findall(text))
