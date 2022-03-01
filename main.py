#date-time for time-based analysis
import datetime
#stock api module
from polygon import RESTClient

#creating defition main
def main():
    #api key
    key = "9r904djsCqkANtfuHsVvqUDppDbSHSZ7"

    #today's date
    now = datetime.date.today()

    #with statement that turns RESTCLIENT(key) to object client
    with RESTClient(key) as client:
        #checks information from yesterday
        resp = client.stocks_equities_daily_open_close("AAPL", (now - datetime.timedelta(days=1)))
        #prints variables given from the response
        print(vars(resp))
        #print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")

#runs function
if __name__ == '__main__':
    main()