import logging
from datetime import datetime
from argparse import ArgumentParser
from contextlib import suppress

import whois
import requests
import validators


def make_cmd_arguments_parser():
    parser_description = 'Scripts check response status and expiration date in urls from text file'
    parser = ArgumentParser(description=parser_description)
    parser.add_argument('file_path',
                        help='File with urls')
    return parser.parse_args()


def load_urls4check_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.rstrip()


def is_server_respond_with_200(domain):
        checked_protocols = ['http://', 'https://', 'http://www.', 'https://www.']
        with suppress(BaseException):
            for protocol in checked_protocols:
                with requests.head('{}{}'.format(protocol, domain)) as request:
                    if request.status_code == requests.codes.ok:
                        return True


if __name__ == '__main__':
    cmd_arguments = make_cmd_arguments_parser()
    file_path = cmd_arguments.file_path
    today = datetime.now()
    for index, domain in enumerate(load_urls4check_generator(file_path)):
        index += 1
        try:
            if validators.url(domain):
                pass
            elif validators.domain(domain):
                url = 'www.{}'.format(domain)
            else:
                print('{:3} {:24} is not correct data'.format(index, domain))
                continue
            whois_data = whois.whois(domain)
            if not whois_data.domain_name:
                print('{:3} {:24} is not found in whois'.format(index, url))
                continue
        except (ValueError, ConnectionError, ConnectionRefusedError) as err:
            logging.warning('{:3} {:24}'.format(index, err))
        finally:
            site_status = 'PASSED' if is_server_respond_with_200(domain) else 'FAILED'
            site_expiration_date = whois_data.expiration_date[0] if isinstance(whois_data.expiration_date, list) else whois_data.expiration_date
            with suppress(TypeError):
                site_expiration_advice, site_expiration_timedelta = None, None
                if site_expiration_date:
                    site_expiration_timedelta = site_expiration_date - today
                    site_expiration_advice = 'PASSED' if site_expiration_timedelta.days > 30 else 'FAILED'
            print('{:3} {:24} Status code 200 OK: {} | Expiration date more 30 days: {} | {} days left'.format(
                index,
                domain,
                site_status,
                site_expiration_advice if site_expiration_advice else 'UNKNOWN',
                site_expiration_timedelta.days if site_expiration_timedelta else 'UNKNOWN',
            ))
