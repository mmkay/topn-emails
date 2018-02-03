import random
import string

EMAILS_COUNT = 100000
DOMAIN_LENGTH = 2
USERNAME_LENGTH = 10
DOMAIN_SUFFIX_LENGTH = 1
FILENAME = 'emails.txt'


def generate_random_ascii_string(length):
    return ''.join(random.sample(string.ascii_lowercase, length))

email_file = open(FILENAME, 'w')
for i in range(EMAILS_COUNT):
    username = generate_random_ascii_string(USERNAME_LENGTH)
    domain = generate_random_ascii_string(DOMAIN_LENGTH)
    domain_suffix = generate_random_ascii_string(DOMAIN_SUFFIX_LENGTH)
    email_file.write('%s@%s.%s\n' % (username, domain, domain_suffix))
email_file.close()
