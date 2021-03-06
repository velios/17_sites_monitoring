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
Checked url info:
1 Url https://devman.org... 200 OK checked: PASSED Expiration less than 30 days: PASSED
2 Url https://slack.com... 200 OK checked: PASSED Expiration less than 30 days: PASSED
```

##### File with checked format
Each url on separate line
```
https://devman.org
https://slack.com
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
