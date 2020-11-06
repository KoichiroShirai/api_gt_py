# coding: utf_8
from pytrends.request import TrendReq
pytrends = TrendReq(hl='ja-JP', tz=360)  # hl : 接続言語 , tz : タイムゾーン

import os
print('現在地:{}'.format(os.getcwd()))

# 関連KW取得
kw = [input('input kw: ')]
pytrends.build_payload(kw, cat=0, timeframe='today 5-y', geo='JP', gprop='')

res = pytrends.interest_over_time()
print(res)

import pandas as pd
df = pd.DataFrame(res)

k = ''.join(kw)

import datetime
now = datetime.datetime.now()
df.to_csv(k + '_' + now.strftime('%Y%m%d_%H%M%S') + '.csv')
