import requests
from bs4 import BeautifulSoup
import pandas as pd


class WebScr:
    url = ""

    def __init__(self, purl):
        self.url = purl

    def get_data_frame(self):
        # 下載 Yahoo 首頁內容
        r_values = ""
        r = requests.get(self.url)
        # 確認是否下載成功
        if r.status_code == requests.codes.ok:

            soup = BeautifulSoup(r.text, 'html.parser')
            table = soup.find('table', attrs={'title': '牌告匯率'})
            table_rows = table.find_all('tr')
            line = []
            for tr in table_rows:
                td_dollar = tr.find_all('div', class_='hidden-phone print_show')
                td_rate = tr.find_all('td', class_='text-right display_none_print_show print_width')
                # row = [tr.text.strip() for tr in td_dollar]
                if [tr.text.strip() for tr in td_dollar]:
                    row = [tr.text.strip() for tr in td_dollar] + [tr.text for tr in td_rate]
                    line.append(row)
            df = pd.DataFrame(line, columns=["DOLLAR", "CASH_BUY", "CASH_SELL", "PD_BUY", "PD_SELL"])
            print(df)

            return df
