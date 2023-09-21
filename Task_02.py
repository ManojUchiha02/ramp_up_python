import random
import string
class UsernameGenerator:
    def __init__(self):
        self.used_usernames = set()
    def generate_username(self, length=8):
        while True:
            username = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
            if len(self.used_usernames) == 10:
                for i in self.used_usernames:
                    print(f"Unique Usernames:{i}")
            if username not in self.used_usernames:
                self.used_usernames.add(username)
                yield username
if __name__ == "__main__":
    generator = UsernameGenerator()

    for i in range(12):
        unique_username = next(generator.generate_username())
