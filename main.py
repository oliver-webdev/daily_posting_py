import os
import requests
from xml.etree import ElementTree
from datetime import datetime


def test():
    print(datetime.today().year)
    print(datetime.today().month)
    print(datetime.today().day)
    print(datetime.today().hour)


# test()


def change_percentage(new, old):
    return round((float(new) - float(old)) / float(old) * 100, 2)


def gap(new, old):
    return round(float(new) - float(old), 2)


def set_color(num):
    if num < 0:
        return '#006dd7'
    else:
        return '#ee2323'


def data_of_today():
    params = {
        'access_key': os.getenv('MARKETSTACK_ACCESS_KEY'),
        'symbols': 'SPY'
    }

    api_result = requests.get('http://api.marketstack.com/v1/eod', params)
    api_response = api_result.json()
    # for stock_data in api_response['data']:
    #     print(r'open: %s / high: %s / low: %s / close: %s / volume: %s / date: %s' % (
    #         stock_data['open'],
    #         stock_data['high'],
    #         stock_data['low'],
    #         stock_data['close'],
    #         stock_data['volume'],
    #         stock_data['date']
    #     ))

    data_symbol = api_response['data'][0]['symbol']

    data_today_close = api_response['data'][0]['close']
    data_today_open = api_response['data'][0]['open']
    data_today_high = api_response['data'][0]['high']
    data_today_low = api_response['data'][0]['low']
    data_today_volume = api_response['data'][0]['volume']

    data_1_day_ago_close = api_response['data'][1]['close']
    data_5_days_ago_close = api_response['data'][4]['close']
    data_30_days_ago_close = api_response['data'][29]['close']
    data_100_days_ago_close = api_response['data'][30]['close']

    gap_of_1_day = gap(data_today_close, data_1_day_ago_close)
    gap_of_5_days = gap(data_today_close, data_5_days_ago_close)
    gap_of_30_days = gap(data_today_close, data_30_days_ago_close)
    gap_of_100_days = gap(data_today_close, data_100_days_ago_close)

    percentage_1_day = change_percentage(data_today_close, data_1_day_ago_close)
    percentage_5_days = change_percentage(data_today_close, data_5_days_ago_close)
    percentage_30_days = change_percentage(data_today_close, data_30_days_ago_close)
    percentage_100_days = change_percentage(data_today_close, data_100_days_ago_close)

    color_1_day = set_color(percentage_1_day)
    color_5_days = set_color(percentage_5_days)
    color_30_days = set_color(percentage_30_days)
    color_100_days = set_color(percentage_100_days)

    dataset = {
        'data_symbol': data_symbol,

        'data_today_close': data_today_close,
        'data_today_open': data_today_open,
        'data_today_high': data_today_high,
        'data_today_low': data_today_low,
        'data_today_volume': data_today_volume,

        'data_1_day_ago_close': data_1_day_ago_close,
        'data_5_days_ago_close': data_5_days_ago_close,
        'data_30_days_ago_close': data_30_days_ago_close,
        'data_100_days_ago_close': data_100_days_ago_close,

        'gap_of_1_day': gap_of_1_day,
        'gap_of_5_days': gap_of_5_days,
        'gap_of_30_days': gap_of_30_days,
        'gap_of_100_days': gap_of_100_days,

        'percentage_1_day': percentage_1_day,
        'percentage_5_days': percentage_5_days,
        'percentage_30_days': percentage_30_days,
        'percentage_100_days': percentage_100_days,

        'color_1_day': color_1_day,
        'color_5_days': color_5_days,
        'color_30_days': color_30_days,
        'color_100_days': color_100_days
    }

    write_post(dataset)


def write_post(dataset):
    print(dataset)
    params = {
        'access_token': os.getenv('TISTORY_ACCESS_TOKEN'),
        'output': '',
        'blogName': 'binit',
        'title': '하루 한 번 체크하는 미국 ETF (' + dataset['data_symbol'] + ') - ' + str(datetime.today().year) + '.' + str(datetime.today().month) + '.' + str(datetime.today().day),
        'content': """<p>[##_Image|kage@cjZ35L/btrd7SCbmoJ/kucRgJToCfCSd7iPNh1wV0/img.png|alignCenter|data-origin-width="580" data-origin-height="580" data-filename="blob" data-ke-mobilestyle="widthOrigin"|||_##]</p>
<table style="border-collapse: collapse; width: 100%; height: 170px;" border="1" data-ke-align="alignLeft">
<tbody>
<tr style="height: 20px;">
<td style="width: 33.3333%; height: 20px; text-align: center; background-color: #66ccff; font-size: 18px;" colspan="3"><b>SPY</b></td>
</tr>
<tr style="height: 20px;">
<td style="width: 33.3333%; height: 20px; text-align: center; background-color: #ccffcc;">종가</td>
<td style="width: 33.3333%; height: 20px; text-align: center;" colspan="2"><span style="color: """ + dataset['color_1_day'] + """;"><b>""" + str(dataset['data_today_close']) + """ (""" + str(dataset['percentage_1_day']) + """%)</b></span></td>
</tr>
<tr style="height: 20px;">
<td style="width: 33.3333%; height: 20px; text-align: center; background-color: #ccffcc;">시가</td>
<td style="width: 33.3333%; height: 20px; text-align: center;" colspan="2">""" + str(dataset['data_today_open']) + """</td>
</tr>
<tr style="height: 20px;">
<td style="width: 33.3333%; height: 20px; text-align: center; background-color: #ccffcc;">고가</td>
<td style="width: 33.3333%; height: 20px; text-align: center;" colspan="2">""" + str(dataset['data_today_high']) + """</td>
</tr>
<tr style="height: 20px;">
<td style="width: 33.3333%; height: 20px; text-align: center; background-color: #ccffcc;">저가</td>
<td style="width: 33.3333%; height: 20px; text-align: center;" colspan="2">""" + str(dataset['data_today_low']) + """</td>
</tr>
<tr style="height: 20px;">
<td style="width: 33.3333%; height: 20px; text-align: center; background-color: #ccffcc;">거래량</td>
<td style="width: 33.3333%; height: 20px; text-align: center;" colspan="2">""" + str(dataset['data_today_volume']) + """</td>
</tr>
<tr style="height: 20px;">
<td style="width: 33.3333%; height: 50px; text-align: center; background-color: #ccffcc;" rowspan="3">기간별 등락(률)</td>
<td style="width: 33.3333%; height: 20px; text-align: center;">5일</td>
<td style="width: 33.3333%; height: 20px; text-align: center;"><span style="color: """ + dataset['color_5_days'] + """;">""" + str(dataset['gap_of_5_days']) + """ (""" + str(dataset['percentage_5_days']) + """%)</span></td>
</tr>
<tr style="height: 10px;">
<td style="width: 33.3333%; height: 10px; text-align: center;">30일</td>
<td style="width: 33.3333%; height: 10px; text-align: center;"><span style="color: """ + dataset['color_30_days'] + """;">""" + str(dataset['gap_of_30_days']) + """ (""" + str(dataset['percentage_30_days']) + """%)</span></td>
</tr>
<tr style="height: 20px;">
<td style="width: 33.3333%; height: 20px; text-align: center;"><span>100일</span></td>
<td style="width: 33.3333%; height: 20px; text-align: center;"><span style="color: """ + dataset['color_100_days'] + """;">""" + str(dataset['gap_of_100_days']) + """ (""" + str(dataset['percentage_100_days']) + """%)</span></td>
</tr>
</tbody>
</table>
<p data-ke-size="size16">&nbsp;</p>""",
        'visibility': '3',
        'category': '1006317',
        'published': '',
        'slogan': '',
        'tag': '미국etf,미국주식,장기투자,spy,적립식투자',
        'acceptComment': '',
        'password': ''
    }

    # ETF 데이터 활용하여 content 작성 필요

    api_result = requests.post('https://www.tistory.com/apis/post/write', params)
    tree = ElementTree.fromstring(api_result.content)
    print(tree.find('status').text)
    print(tree.find('postId').text)
    print(tree.find('url').text)


data_of_today()
