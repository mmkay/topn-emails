# topn-emails

Given the input of 1 e-mail address per line, the program returns N domains that have the highest count of e-mail
addresses.

## Running

```bash
python3 topn-emails.py < data/emails.txt
```

## Generating data

To generate a file that contains multiple e-mail addresses, you can run
```bash
cd data
python3 generate-emails.py
```

The script can be configured by modifying variables inside generate-emails. The file is by default generated in the
directory where the script runs.