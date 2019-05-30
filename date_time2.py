from datetime import datetime

str_date = '01/01/17 12:10:03.234567'
date_tm = datetime.strptime(str_date, '%d/%m/%y %H:%M:%S.%f')
print(date_tm)
