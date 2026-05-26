#!/usr/bin/env python3

def validate_user(username, minlen):
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

# Map usernames to names
name_map = {}

try:
    with open('file.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            user, name = line.strip().split(', ')
            name_map[user] = name

    username = input("Enter a username: ")
    if validate_user(username, 5):
        if username in name_map:
            print(f"Hi, {name_map[username]}! You have been authenticated.")
        else:
            print("Username not found.")
    else:
        print("Invalid username.")
except OSError:
    print("Error: Unable to open file.txt")
