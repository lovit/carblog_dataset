## Carblog dataset analysis

여기는 carblog dataset 을 제공하기 위한 repository 입니다. 이 데이터셋을 이용한 분석 사례는 [여기](https://github.com/lovit/carblog_analysis)에 있습니다.

## Carblog dataset

이 데이터셋은 네이버 블로그에서 2010. 1. 1 부터 2015. 8. 1 까지 생성된 포스트를 수집한 데이터입니다. 총 27 개의 카테고리로 구성되어 있으며, 각 카테고리는 아래의 질의어가 포함되어 있습니다.

```
category 0: A6
category 1: BMW5
category 2: BMW
category 3: K3
category 4: K5
category 5: K7
category 6: QM3
category 7: 그랜저
category 8: 벤츠E
category 9: 산타페
category 10: 소나타
category 11: 스포티지
category 12: 싼타페
category 13: 쏘나타
category 14: 쏘렌토
category 15: 아반떼
category 16: 아반테
category 17: 제네시스
category 18: 코란도C
category 19: 투싼
category 20: 티구안
category 21: 티볼리
category 22: 파사트
category 23: 폭스바겐골프
category 24: 현기차
category 25: 현대자동차
category 26: 현대차
```

데이터는 fetch 함수를 이용하여 다운로드 받아야 합니다. 사용법은 아래에 있습니다. 15 GB 의 데이터 공간이 필요합니다.

## Usage

이 repository 를 복사한 뒤, `fetch` 함수를 한 번 실행해야 합니다. `fetch` 함수는 한 번만 실행하면 됩니다.

```
git clone https://github.com/lovit/carblog_dataset.git
```

```python
from carblog_dataset import fetch

fetch()
```

fetch 함수를 이용하여 데이터를 다운로드 받고나면 `check_setup` 함수를 실행하면 True 가 return 됩니다.

```python
from carblog_dataset import check_setup

check_setup()
# True
```

텍스트와 인덱스는 카테고리별로 로딩해야 합니다. `load_text` 함수를 이용하여 한 카테고리의 텍스트를 로딩할 수 있습니다.

```python
from carblog_dataset import load_text

category = 7
texts = load_text(category)
```

인덱스는 `load_index` 함수를 이용하여 불러올 수 있습니다. 기본은 각 텍스트에 해당하는 tags 가 return 됩니다. 그 외에 각 텍스트의 작성 날짜나 타이틀을 함께 return 하려면 아래처럼 옵션을 선택합니다. 옵션에 따라 list of tuple 이 구성됩니다.

```python
from carblog_dataset import load_index

category = 7
index = load_index(category)
# or
index = load_index(category, date=True, tags=False, title=False)
```

각 카테고리의 종류는 아래의 함수를 통하여 확인할 수 있습니다. list of str 형식으로 각 category 에 해당하는 질의어 (query) 가 로딩됩니다.

```python
from carblog_dataset import load_category_index

load_category_index()
```
