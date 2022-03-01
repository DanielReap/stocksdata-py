import datetime

from polygon import RESTClient


def main():
    key = "9r904djsCqkANtfuHsVvqUDppDbSHSZ7"

    now = datetime.date.today()

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        resp = client.stocks_equities_daily_open_close("AAPL", (now - datetime.timedelta(days=1)))
        print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")


if __name__ == '__main__':
    main()