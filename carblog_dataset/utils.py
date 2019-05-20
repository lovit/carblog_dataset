import csv
from datetime import datetime
import os
import re


installpath = os.path.dirname(os.path.realpath(__file__))
text_dir = os.path.abspath('../texts/')
index_dir = os.path.abspath('../index/')
num_categories = 27

def load_list(path, dtype=None):
    """
    This function used to create carblog data with raw scraped data.
    """
    with open(path, encoding='utf-8') as f:
        docs = [doc.strip() for doc in f]
    return docs

def parse_date(s):
    """
    This function used to create carblog data with raw scraped data.

    Usage
    -----
        >>> parse_date('2012-01-23')       # datetime.datetime(2012, 1, 23, 0, 0)
        >>> parse_date('2012-01-23 15:23') # datetime.datetime(2012, 1, 23, 0, 0)
    """
    date_pattern = re.compile('\d{4}-\d{2}-\d{2}')
    d = date_pattern.findall(s)
    if not d:
        return None
    return datetime.strptime(d[0], '%Y-%m-%d')

def parse_tags(line):
    """
    This function used to create carblog data with raw scraped data.

    Usage
    -----
        >>> parse_tags("'자동차', '중고차', 'BMW'")   # ['자동차', '중고차', 'BMW']
        >>> parse_tags("['자동차', '중고차', 'BMW']") # ['자동차', '중고차', 'BMW']
        >>> parse_tags('[]')                        # []
        >>> parse_tags('')                          # []
    """
    def strip(s):
        return s.strip()[1:-1].strip()

    if not line:
        return []
    if line[0] == '[' and line[-1] == ']':
        line = line[1:-1]
    tags = list(csv.reader([line], delimiter=','))[0]
    tags = [strip(s) for s in tags]
    return tags
