from django.conf import settings

IMPORT_CSV_URL = getattr(
    settings,
    'ETL_IMPORT_CSV_URL',
    'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com'
    '/price-paid-data'
    '/pp-monthly-update-new-version.csv'
)

CSV_TMP_FILE = getattr(settings, 'ETL_CSV_TMP_FILE', '/tmp/tmp_csv_import_file')


