티스토리 자동 포스팅 
=

###### 내용 수정일: 2021-09-09

### 사용 기술
* Python
* Github Actions

### 주요 기능
1. 오늘자 미국 ETF 주가 정보를 API로 GET 요청하여 응답을 받는다.
    - JSON response parsing
    - API 정보: https://marketstack.com/documentation

3. 데이터를 가공하여 티스토리 글 작성 API에 POST 요청으로 포스팅을 한다.
    - XML response parsing
    - API 정보: https://tistory.github.io/document-tistory-apis/

5. 매일 경제 해외증시 페이지에서 하루 분의 기사를 크롤링하고 포스팅 내용에 링크를 작성한다.
    - HTML response parsing
    - 페이지 정보: https://www.mk.co.kr/news/stock/foreign-stock/

4. Github Actions를 이용하여 매일 아침 8시에 자동 포스팅 스크립트가 실행되도록 설정한다.
