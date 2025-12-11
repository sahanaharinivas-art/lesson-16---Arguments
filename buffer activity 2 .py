def shutdown (s):
    if s - "yes":
        return "shutting down..."
    elif s -"no":
        return "shutdown aborted."
    else:
        return "sorry."

user_input = input("do you want to shut down? (yes/no):")
print(shutdown(user_input))