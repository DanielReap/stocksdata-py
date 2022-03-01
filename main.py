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
            #checks information from yesterday
            resp = client.stocks_equities_daily_open_close(str(ticker), (now - datetime.timedelta(days=1)))
            #prints variables given from the response
            print(vars(resp))
            #print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")
    #if an error occurs, define it as e
    except Exception as e:
        #gets the class of the error // type of error
        error = e.__class__.__name__
        #if HTTP error, invalid ticker is the issue
        if error == 'HTTPError':
            #re-run program so user can re-enter the ticker
            print('Invalid ticker, try again.')
            main()
        else:
            #print error type if it is not an HTTPError
            print(error)

#initialize function
if __name__ == '__main__':
    main()