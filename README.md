## Carblog dataset

This dataset consists of blog posts that have been scraped from Naver blog which created from 2010. 01. 01 to 2015. 08. 01.

This dataset includes 27 sub-datasets that scraped with a query term (Each blog posts in a sub-dataset includes the query term). Query terms (term index) are below.

| A6 (0) | BMW5 (1) | BMW (2) | K3 (3) |
| K5 (4) | K7 (5) | QM3 (6) | 그랜저 (7) | 벤츠E (8) |
| 산타페 (9) | 소나타 (10) | 스포티지 (11) | 싼타페 (12) | 쏘나타 (13) |
| 쏘렌토 (14) | 아반떼 (15) | 아반테 (16) | 제네시스 (17) | 코란도C (18) |
| 투싼 (19) | 티구안 (20) | 티볼리 (21) | 파사트 (22) | 폭스바겐골프 (23) |
| 현기차 (24) | 현대자동차 (25) | 현대차 (26) | . | . |

It needs about 15 GB disk space to decompress zip files and store text files.

## Usage

To load text data

```python
from carblog_dataset import load_text

category = 7
texts = load_text()
```

To load meta information such as date, user generated tags, or title.

```python
from carblog_dataset import load_index

category = 7
index = load_index(category)
# or
index = load_index(category, date=True, tags=False, title=False)
```
