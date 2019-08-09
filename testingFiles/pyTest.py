import pytz
import datetime
d = datetime.datetime.now()
print(d.time())
tz = pytz.timezone("America/New_York")
d = tz.localize(d)
print(d.time())
