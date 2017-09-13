# Sites Monitoring Utility

Utility to check expiration date and 200 OK status

### How to install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

### How to use
##### Sample run
```bash
$ python check_sites_health.py urls.txt
Users who sent tasks between 04:00:00 and 08:00:00:
  1 pikabu.ru     Status code 200 OK: PASSED | Expiration date more 30 days: PASSED | 196 days left
  2 habr.ru       Status code 200 OK: FAILED | Expiration date more 30 days: PASSED | 210 days left
  3 facebook.com  Status code 200 OK: PASSED | Expiration date more 30 days: PASSED | 2749 days left
  4 twitter.com   Status code 200 OK: PASSED | Expiration date more 30 days: PASSED | 854 days left
  5 google.com    Status code 200 OK: FAILED | Expiration date more 30 days: PASSED | 1091 days left
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
