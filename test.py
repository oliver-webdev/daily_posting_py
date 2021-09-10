import os
import datetime
import pytz


print(os.environ['MARKETSTACK_ACCESS_KEY'])
print(os.environ['TISTORY_ACCESS_TOKEN'])

now = datetime.datetime.utcnow()
print(now)

KST = pytz.timezone('Asia/Seoul')
now_kst = now.astimezone(KST)
print(now_kst.strftime("%Y-%m-%d %H:%M:%S %Z%z"))


print(now_kst.strftime("%Y"))
print(now_kst.strftime("%m"))
print(now_kst.strftime("%d"))


def get_news():
    result = ''

    url = 'https://www.mk.co.kr/news/stock/foreign-stock/'
    response = requests.get(url)

    if response.status_code == 200:
        html = response.content.decode('euc-kr', 'replace')
        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.select('.article_list')
        for content in contents:

            content_title = content.select_one('dt.tit > a').get_text()
            content_link = content.find('a')['href']
            content_desc = content.select_one('dd.desc > span.desctxt').get_text()
            content_date = content.select_one('dd.desc > span.date').get_text()

            # 시간
            now = datetime.datetime.utcnow()
            KST = pytz.timezone('Asia/Seoul')
            now_kst = now.astimezone(KST)

            content_datetime = datetime.datetime.strptime(content_date, '%Y.%m.%d %H:%M')
            content_datetime_kst = content_datetime.astimezone(KST)
            # print(content_datetime_kst)

            test_time = now_kst - datetime.timedelta(1)
            compare_time = test_time.replace(hour=8, minute=0, second=0, microsecond=0)
            # print(compare_time)

            # print(content_datetime_kst > compare_time)

            if content_datetime_kst > compare_time:
                result += '''
<p data-ke-size="size16"><a href="''' + content_link + '''" target="_blank" rel="noopener">'''+ content_title + '''"&nbsp;'''+ content_date + '''</a></p>'''
            else:
                break

    else:
        result = '[뉴스 가져오기에 실패했습니다.]'
        print('RESPONSE ERROR status_code: ', response.status_code)

    return result


print(get_news())
