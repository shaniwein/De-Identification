import datetime

from config import config

def get_year_from_date_string(date_string):
    return datetime.datetime.strptime(date_string, '%Y-%m-%d').year

def get_age_by_birth_date(date_string):
    birth_year = get_year_from_date_string(date_string)
    age = datetime.datetime.now().year - birth_year
    return str(age) if age < 90 else '90+'

def get_stripped_zip_code(zip_code):
    stripped_zip_code = zip_code[:config.strip_size]
    if config.zip_code_to_population[stripped_zip_code] < config.minimum_population_size:
        return '0' * len(zip_code)
    return stripped_zip_code + '0' * (len(zip_code) - config.strip_size)

def replace_digits_and_alpha_with_sensible_symbol(match):
    value = match.group()
    return ''.join(config.sensible_symbol if c.isdigit() or c.isalpha() else c for c in value)
    
def replace_date_with_year(match):
    value = match.group()
    return str(get_year_from_date_string(value))

def get_de_identified_note(note):
    note = config.email_regex.sub(replace_digits_and_alpha_with_sensible_symbol, note)
    note = config.phone_regex.sub(replace_digits_and_alpha_with_sensible_symbol, note)
    note = config.ssn_regex.sub(replace_digits_and_alpha_with_sensible_symbol, note)
    note = config.date_regex.sub(replace_date_with_year, note)
    return note

