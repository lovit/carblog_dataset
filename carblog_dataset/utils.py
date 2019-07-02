import csv
from datetime import datetime
from glob import glob
import os
import re
import requests
import zipfile

from .config import text_dir
from .config import index_dir
from .config import num_categories
from .config import index_url_form
from .config import text_url_form

sep = os.path.sep

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

def check_setup():
    """
    Check whether zip files are decompressed or not.
    If not, it will decompress all zip files automatically.
    If data files are set, it returns True. Else it will raise runtime error.
    """
    text_files = glob('{}/*.txt'.format(text_dir))
    index_files = glob('{}/*.date'.format(index_dir))
    if not text_files or not index_files:
        message = """You should first setup dataset using carblog_dataset.setup function.
        >>> from carblog_dataset import setup
        >>> setup(remove_zip=True) # or
        >>> setup(remove_zip=False)
        """
        raise RuntimeError(message)
    return True

def fetch(category=None, remove_zip=True):

    def sort(paths):
        return sorted(paths, key=lambda x:int(x.split(sep)[-1].split('.')[0]))

    if isinstance(category, int):
        text_sources = [text_url_form.format(category)]
        index_sources = [index_url_form.format(category)]
    else:
        text_sources = [text_url_form.format(category) for category in range(num_categories)]
        index_sources = [index_url_form.format(category) for category in range(num_categories)]

    text_sources = sort(text_sources)
    index_sources = sort(index_sources)

    for text_url, index_url in zip(text_sources, index_sources):
        name = text_url.split('/')[-1]
        text_source = '{}/{}'.format(text_dir, name)
        download_a_file(text_url, text_source)
        print('downloaded {}'.format(name))
        unzip(text_source, text_dir)
        print('unziped {}'.format(name))

        name = index_url.split('/')[-1]
        index_source = '{}/{}'.format(index_dir, name)
        download_a_file(index_url, index_source)
        print('downloaded {}'.format(name))
        unzip(index_source, index_dir)
        print('unziped {}'.format(name))

        if remove_zip:
            os.remove(text_source)
            os.remove(index_source)
    print('done')

def unzip(source, destination):
    """
    Arguments
    ---------
    source : str
        zip file address. It doesn't matter absolute path or relative path
    destination :
        Directory path of unzip
    Returns
    -------
    flag : Boolean
        It return True if downloading success else return False
    """

    abspath = os.path.abspath(destination)
    dirname = os.path.dirname(abspath)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    try:
        downloaded = zipfile.ZipFile(source)
        downloaded.extractall(destination)
        return True
    except Exception as e:
        print(e)
        return False

def download_a_file(url, fname):
    """
    Arguments
    --------
    url : str
        URL address of file to be downloaded
    fname : str
        Download file address
    Returns
    -------
    flag : Boolean
        It return True if downloading success else return False
    """

    fname = os.path.abspath(fname)
    dirname = os.path.dirname(fname)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # If you do not set user-agent, downloading from url is stalled.
    headers = {'user-agent': 'Wget/1.16 (linux-gnu)'}

    try:
        r = requests.get(url, stream=True, headers=headers)
        with open(fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return True
    except Exception as e:
        print(e)
        return False
