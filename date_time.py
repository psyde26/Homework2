from datetime import date, timedelta, datetime
import monthdelta

month = monthdelta.monthdelta

today = date.today()
yestarday = today - timedelta(days=1)
mnth_ago = today - month(1)

print(yestarday)
print(today)
print(mnth_ago)
