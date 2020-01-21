EXAMPLE_DATA = {
    'jobs': [{'frequency': '* * * * *',
              'jobconfig': [{'config': [('*',
                                         {'maxspeed': 1048576,
                                          'password': 'onesecretpassword',
                                          'port': 22,
                                          'url': 'basset://basset1.domain.com/tootsiepop/123.csv',
                                          'username': 'myusername'})],
                             'hasbro': 'basset'},
                            {'config': [('*',
                                         {'field_delim': ',',
                                          'field_line': True,
                                          'no_blanks': True,
                                          'quote_char': '"'})],
                             'hasbro': 'pen'},
                            {'config': [('*',
                                         {'db_database': 'mydatabase',
                                          'db_host': 'myhost',
                                          'db_password': 'anothersecretpassword',
                                          'db_table': 'mytable',
                                          'db_user': 'myuser'})],
                             'hasbro': 'dart'}],
              'jobdesc': 'Data from tootsiepop',
              'jobname': 'tootsiepop',
              'max_records_fail': '110%',
              'min_failure_time': '1000y'}],
    'vendor': 'tootsiepop'}
def get_all_key_value_pairs_where_values_are_simple(data):
    class Namespace(object):
        pass
    ns = Namespace()
    ns.results = []

    def inner(data):
        if isinstance(data, dict):
            for k, v in data.items():
                if (isinstance(v, dict) or
                    isinstance(v, list) or
                    isinstance(v, tuple)
                    ):
                    inner(v)
                else:
                    ns.results.append((k, v))
        elif isinstance(data, list) or isinstance(data, tuple):
            for item in data:
                inner(item)

    inner(data)
    return ns.results

from pprint import pprint
pprint(get_all_key_value_pairs_where_values_are_simple(EXAMPLE_DATA))