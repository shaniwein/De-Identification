import collections
import csv
import os
import re

class Config(object):

    # zip code
    strip_size              = 3
    minimum_population_size = 20000
    default_csv_path        = '../../population_by_zcta_2010.csv'

    # notes
    email_regex     = re.compile('([a-zA-Z0-9._]*@[a-zA-Z0-9.]*)')
    phone_regex     = re.compile('(\([0-9]{3}\) ?[0-9]{3}[- ][0-9]{4})|([0-9]{3}-[0-9]{3}-[0-9]{4})')
    ssn_regex       = re.compile('(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}')
    date_regex      = re.compile('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))')
    sensible_symbol = 'X'

    def __init__(self, path):
        self.zip_code_to_population = self.parse_zip_code_to_population_csv(path or self.default_csv_path)

    def parse_zip_code_to_population_csv(self, path):
        with open(path, 'rb') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            headers = csv_reader.next()
            stripped_zip_code_to_population = collections.defaultdict(int)
            for zip_code, population_count in csv_reader:
                stripped_zip_code_to_population[zip_code[:self.strip_size]] += int(population_count)
        return stripped_zip_code_to_population 


config = Config(os.environ.get('ZIP_CODE_TO_POPULATION_CSV'))

