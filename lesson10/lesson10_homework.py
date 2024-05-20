from csv import DictReader

with open('個股日成交資訊.csv', encoding='utf-8', newline='') as file:
    reader: DictReader = DictReader(file)
    sites: list = list(reader)

for site in sites:
    print(site['證券代號'], site['證券名稱'], site['成交股數'], site['成交金額'], site['開盤價'],
          site['最高價'], site['最低價'], site['收盤價'], site['漲跌價差'], site['成交筆數'])
