from .utils import installpath

def load_category_index():
    path = '{}/../car_index'.format(installpath)
    with open(path, encoding='utf-8') as f:
        index = [doc.strip() for doc in f]
    return index
