from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

PEP_URL = 'https://peps.python.org/'

# directories
BASE_DIR = Path(__file__).parent
RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS

# formats and names
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_FORMAT = 'csv'
PEP_FILENAME = 'pep'
STATUS_SUMMARY_FILENAME = 'status_summary'

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
FEEDS = {
    f'{RESULTS}/{PEP_FILENAME}_%(time)s.{FILE_FORMAT}': {
        'format': FILE_FORMAT,
        'fields': ['number', 'name', 'status']
    },
}
