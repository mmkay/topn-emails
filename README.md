# topn-emails

Given the input of 1 e-mail address per line, the program returns N domains that have the highest count of e-mail
addresses.

## Running

```bash
python3 topn-emails.py < data/emails.txt
```

By default, the script will return 10 top domains. If you want to get a different value, run

```bash
python3 topn-emails.py 15 < data/emails.txt
```

## Generating data

To generate a file that contains multiple e-mail addresses, you can run
```bash
cd data
python3 generate-emails.py
```

The script can be configured by modifying variables inside generate-emails. The file is by default generated in the
directory where the script runs.