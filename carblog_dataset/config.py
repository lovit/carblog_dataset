import os

aws_dir = 'https://lovit-carblog-dataset.s3.ap-northeast-2.amazonaws.com/zips'
text_suffix = '.txt.zip'
index_suffix = '.index.zip'
text_url_form = '%s/{}%s' % (aws_dir, text_suffix)
index_url_form = '%s/{}%s' % (aws_dir, index_suffix)

sep = os.path.sep
installpath = os.path.dirname(os.path.realpath(__file__))
text_dir = sep.join(installpath.split(sep)[:-1]) + '{0}texts{0}'.format(sep)
index_dir = sep.join(installpath.split(sep)[:-1]) + '{0}index{0}'.format(sep)

num_categories = 27
