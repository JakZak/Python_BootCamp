import sys
last_login = {}
users = {}
if len(sys.argv) > 1:
    nazwa_pliku = sys.argv[1]

    with open(nazwa_pliku) as f:
        for line in f:
            user, action, time = line.split(';')
            time = int(time)
            if action == "LOGIN":
                last_login[user] = time
            if action == "LOGOUT":
                users[user] = users.get(user, 0) + time-last_login[user]

def sort_key(x):
    return x[1]

print('Czas przebywania w systemie: ')
for items in sorted(users.items(), key=lambda x: x[1], reverse=True):
    print(items)

