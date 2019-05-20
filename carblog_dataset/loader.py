from .utils import installpath
from .utils import text_dir, index_dir, num_categories


text_path_base = '%s/{}.txt' % text_dir
date_path_base = '%s/{}.date' % index_dir
tags_path_base = '%s/{}.tags' % index_dir
title_path_base = '%s/{}.title' % index_dir
url_path_base = '%s/{}.url' % index_dir

def load_category_index():
    path = '{}/../car_index'.format(installpath)
    with open(path, encoding='utf-8') as f:
        index = [doc.strip() for doc in f]
    return index

def load_file(path):
    with open(path, encoding='utf-8') as f:
        docs = [doc.strip() for doc in f]
    return docs

def load_text(category):
    check_category(category)
    path = text_path_base.format(category)
    return load_file(path)

def load_index(category, date=False, tags=True, title=False, url=False):
    check_category(category)

    num_columns = date + tags + title + url
    if num_columns == 0:
        raise ValueError('Set column arguments as True at least one [date, tags, title, url]')

    loaded = []
    if date:
        path = date_path_base.format(category)
        loaded.append(load_file(path))
    if tags:
        path = tags_path_base.format(category)
        loaded_tags = load_file(path)
        loaded_tags = [tuple(t.split('\t')) for t in loaded_tags]
        loaded.append(loaded_tags)
    if title:
        path = title_path_base.format(category)
        loaded.append(load_file(path))
    if url:
        path = url_path_base.format(category)
        loaded.append(load_file(path))
    grouped = [element for element in zip(*loaded)]
    return grouped

def check_category(category):
    if isinstance(category, str):
        category = int(category)
    if not (0 <= category < num_categories):
        raise ValueError('Category id should be integer 0 ~ 26. However the inserted value is {}'.format(category))
    return True
