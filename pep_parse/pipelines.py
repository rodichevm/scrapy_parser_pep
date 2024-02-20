import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import (
    DATETIME_FORMAT,
    RESULTS_DIR, STATUS_SUMMARY_FILENAME
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        with open(
                f'{RESULTS_DIR}/{STATUS_SUMMARY_FILENAME}{now_formatted}.csv',
                'w', encoding='utf-8'
        ) as f:
            csv.writer(f, dialect=csv.unix_dialect).writerows(
                [('Статус', 'Количество'),
                 *self.status_count.items(),
                 ('Всего', sum(self.status_count.values()))]
            )
