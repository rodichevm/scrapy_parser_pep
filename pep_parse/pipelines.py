import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import (
    BASE_DIR, DATETIME_FORMAT,
    FILE_FORMAT, TABLE_FOOTER, TABLE_HEADER, RESULTS,
    STATUS_SUMMARY_FILENAME
)


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        file_path = self.results_dir / STATUS_SUMMARY_FILENAME.format(
            now_formatted=dt.datetime.now().strftime(DATETIME_FORMAT),
            file_format=FILE_FORMAT)
        with (open(file_path, 'w', encoding='utf-8') as f):
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows((
                TABLE_HEADER,
                *self.status_count.items(),
                (TABLE_FOOTER, sum(self.status_count.values()))
            ))
