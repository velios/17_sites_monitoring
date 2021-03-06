from datetime import datetime
from argparse import ArgumentParser, FileType

import whois
import requests
from requests.exceptions import MissingSchema, ConnectionError


def fetch_cmd_arguments():
    parser_description = 'Scripts check response status and expiration date in urls from text file'
    parser = ArgumentParser(description=parser_description)
    parser.add_argument('file_path',
                        help='File with urls',
                        type=FileType('r', encoding='UTF-8'))
    return parser.parse_args()


def make_urls4check_generator(urls_file):
    with urls_file as file:
        for line in file:
            cleaned_line = line.rstrip()
            if cleaned_line:
                yield cleaned_line


def is_server_respond_with_200(url) -> bool:
    with requests.head('{}'.format(url)) as request:
            return request.status_code == requests.codes.ok


def is_whois_expiration_date_less_n_days(url, days=30) -> bool:
    whois_info = whois.whois(url)
    whois_expiration_date = whois_info.expiration_date[0]
    today = datetime.now()
    remaining_paid_period_in_days = (whois_expiration_date - today).days
    return remaining_paid_period_in_days > days


if __name__ == '__main__':
    cmd_arguments = fetch_cmd_arguments()
    urls_file = cmd_arguments.file_path
    checked_urls_generator = make_urls4check_generator(urls_file)
    print('Checked url info:')
    for index, url in enumerate(checked_urls_generator, start=1):
        try:
            is_respond_200 = 'PASSED' if is_server_respond_with_200(url) else 'FAILED'
            is_expiration_less_30_days = 'PASSED' if is_whois_expiration_date_less_n_days(url) else 'FAILED'
        except (MissingSchema, ConnectionError, TypeError) as err:
            print('Error: ', err)
        else:
            print(
                '{:3} Url {}... 200 OK checked: {} '
                'Expiration less than 30 days: {}'.format(index,
                                                          url,
                                                          is_respond_200,
                                                          is_expiration_less_30_days)
            )
