#date-time for time-based analysis
import datetime
#stock api module
from polygon import RESTClient

#creating defition main
def main():
    #user-inputed ticker
    ticker = input("What ticker would you like to get information on? ")

    #api key
    key = "9r904djsCqkANtfuHsVvqUDppDbSHSZ7"

    #today's date
    now = datetime.date.today()

    #try and with statement that turns RESTCLIENT(key) to object client
    try:
        with RESTClient(key) as client:
            #Gets information from yesterday to today
            resp = client.stocks_equities_aggregates(str(ticker), multiplier=1, timespan="day", from_=(now - datetime.timedelta(days=5)), to=(now - datetime.timedelta(days=4)), adjusted='true')
            change = ((float(resp.results[1]['c'])-float(resp.results[0]['c']))/(float(resp.results[1]['c'])+float(resp.results[0]['c'])))*100
            if change > 0:
                print('Current price %s. Your stock has increased %s%s' % (resp.results[1]['c'], '%', change))
                exit()
            if change < 0:
                print('Current price %s. Your stock has decreased %s%s' % (resp.results[1]['c'], '%', change))
                exit()
            print('Current price %s. No change in stock' % (resp.results[1]['c']))
    #Error handling
    except Exception as e:
        print(e)
        main()

#initialize function
if __name__ == '__main__':
    main()