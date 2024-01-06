import requests
import json
import dataframeOps as dfo

timeout = 20
base_url = "http://www.nseindia.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json, application/xml, text/html, text/csv",
    "Accept-Language": "en-US,en;q=0.5"
}

drop_cols = ['_id', 'CH_MARKET_TYPE', 'CH_LAST_TRADED_PRICE', 'CH_PREVIOUS_CLS_PRICE', 'CH_TOT_TRADED_QTY',
             'CH_TOT_TRADED_VAL', 'CH_TOTAL_TRADES', 'TIMESTAMP', 'createdAt', 'updatedAt', '__v', 'SLBMH_TOT_VAL',
             'mTIMESTAMP','CA','symChange']
new_col_names = ['SYMBOL','SERIES','HIGH','LOW','OPEN','CLOSE','HI_52_WK','LO_52_WK','ISIN_NUMBER','PRICE_DATE','VWAP']

new_col_order = ['ISIN_NUMBER','SYMBOL','SERIES','PRICE_DATE','HIGH','LOW','OPEN','CLOSE','VWAP','HI_52_WK','LO_52_WK']


def set_cookies(b_url, t_out, h_ders):
    r = requests.get(b_url, timeout=t_out, headers=h_ders)
    cookies = dict(r.cookies)
    return cookies


def get_historical_data(symbol, from_date, to_date):
    try:
        symbol = symbol.replace('&', '%26')
        from_date = from_date.strftime('%d-%m-%Y')
        to_date = to_date.strftime('%d-%m-%Y')
        url = f"/api/historical/cm/equity?symbol={symbol}&from={from_date}&to={to_date}"
        print(base_url + url)
        response = requests.get(base_url + url, headers=headers, timeout=timeout,
                                cookies=set_cookies(base_url, timeout, headers))
        data = json.loads(response.content)
        df = dfo.normalize_data(data)
        temp = dfo.normalize_data(df['data'])
        #temp_norm = dfo.normalize_data(temp[34])
        final = dfo.initialize_empty_dataframe()
        for i in range(0,temp.size):
            final_temp = dfo.drop_columns_by_names(dfo.normalize_data(temp[i]), drop_cols)
            final = dfo.concat_dataframes(final, final_temp)
        final.CH_TIMESTAMP = dfo.convert_to_date(final.CH_TIMESTAMP, '%Y-%m-%d')
        #print(final.columns)
        final = dfo.rename_column_headers(final, new_col_names)
        final = dfo.reorder_column_headers(final, new_col_order)
        return final
    except Exception as ex:
        print(ex)
        return None
