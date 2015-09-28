from celery.utils.log import get_logger
from pocfullstack.celery import app
from .settings import IMPORT_CSV_URL, CSV_TMP_FILE
from .models import SaleFacts, SaleFactsBad
import csv
import urllib.request
import uuid
import traceback


logger = get_logger(__name__)


@app.task
def create_import_chain():
    """
    Task creates import chain for CSV data
    """
    fetch_csv_file_si = fetch_csv_file.si()
    read_lines_si = read_lines.si()

    (fetch_csv_file_si | read_lines_si).delay()


@app.task(default_retry_delay=300, max_retries=10)
def fetch_csv_file():
    """
    Task fetching CSV file data. I must assume the URL is not being changed.
    """
    sd = urllib.request.urlopen(IMPORT_CSV_URL)
    with open(CSV_TMP_FILE, 'wb') as fd:
        fd.write(sd.read())


@app.task
def read_lines():
    """
    Task is used to insert rows into process queue
    """
    with open(CSV_TMP_FILE, 'r') as csv_fh:
        csv_reader = csv.reader(csv_fh)
        for row in csv_reader:
            process_data.delay(row)


@app.task
def process_data(row):
    if len(row) != 15:
        # wrong row
        logger.error('Wrong "row" with data: %s' % row)
        return
    uid = uuid.UUID(row[0])
    if row[14] == 'A':
        # append row
        try:
            logger.info('Creating UID: %s' % uid)
            SaleFacts.objects.create_from_row(row)
        except:
            SaleFactsBad.objects.create(row='%s' % row, exc=traceback.format_exc())
    elif row[14] == 'C':
        # change
        fact = SaleFacts.objects.filter(transaction_uid=uid).first()
        if fact is None:
            try:
                logger.info('Creating (instead of update) UID: %s' % uid)
                SaleFacts.objects.create_from_row(row)
            except:
                SaleFactsBad.objects.create(row='%s' % row, exc=traceback.format_exc())
        else:
            fact.update_from_row(row)
            fact.save()
            logger.info('Updating UID: %s' % uid)
    elif row[14] == 'D':
        SaleFacts.objects.filter(transaction_uid=uid).delete()
        logger.info('Deleting UID: %s' % uid)
