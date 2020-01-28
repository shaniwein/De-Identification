import flask
import json

from .utilities import get_age_by_birth_date, get_stripped_zip_code, get_year_from_date_string, get_de_identified_note 

app = flask.Flask(__name__)

@app.route('/de_identify', methods=['GET'])
def de_identify_patient_record():
    '''
    Input: single patient record in a json format (as parameter "record").
    Output: De-identified record in a json format.
    
    This is the main API's entry point.
    It receives a patient's record and returns it de-identified.
    If an invalid parameter is inserted, an error code and message will be returned in a json format.
    '''
    record = flask.request.values.get('record')
    if not record:
        return {'error_code': 400, 'message':'Bad request- missing parameter "record".'}
    try:
        record = json.loads(record)
    except ValueError as e:
        return {'error_code': 400, 'message': 'Failed to load param value {} into a json object: {}'.format(record, e)}
    de_identified_record = {}
    if 'birthDate' in record:
        de_identified_record['age'] = get_age_by_birth_date(record['birthDate'])
    if 'zipCode' in record:
        de_identified_record['zipCode'] = get_stripped_zip_code(record['zipCode'])
    if 'admissionDate' in record:
        de_identified_record['admissionYear'] = get_year_from_date_string(record['admissionDate'])
    if 'dischargeDate' in record:
        de_identified_record['dischargeYear'] = get_year_from_date_string(record['dischargeDate'])
    if 'notes' in record:
        de_identified_record['notes'] = get_de_identified_note(record['notes'])
    return de_identified_record

