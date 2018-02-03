import sys

email_count_by_domain = {}

for line in sys.stdin:
    username, domain = line.strip('\n').split('@')
    if domain in email_count_by_domain:
        email_count_by_domain[domain] += 1
    else:
        email_count_by_domain[domain] = 1

sorted_emails_by_domain = []

for domain in sorted(email_count_by_domain, key=email_count_by_domain.get, reverse=True):
    sorted_emails_by_domain.append((domain, email_count_by_domain[domain]))

for element in sorted_emails_by_domain[:10]:
    print("%s %d" % (element[0], element[1]))
