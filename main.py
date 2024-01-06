import dbConnect
import apiConnect
import dataframeOps
from datetime import date
username = 'system'
password = 'admin'
server = 'localhost:1521/xe'
query = 'select symbol from stock_master'
con = dbConnect.create_connection(username, password, server)
# insert_data = f"""insert into stock_historical_data
#                 (ISIN_NUMBER, SYMBOL, SERIES, PRICE_DATE, HIGH, LOW, OPEN, CLOSE, VWAP, HI_52_WK, LO_52_WK)
#                 select :1,:2,:3,TO_DATE(:4, 'YYYY-MM-DD'),:5,:6,:7,:8,:9,:10,:11
#                     from dual
#                     where not exists(
#                         select 1
#                             from stock_historical_data
#                             where ISIN_NUMBER = :1
#                             and SYMBOL = :2
#                             and SERIES = :3
#                             and PRICE_DATE = TO_DATE(:4, 'YYYY-MM-DD')
#                             and HIGH = :5
#                             and LOW = :6
#                             and OPEN = :7
#                             and CLOSE = :8
#                             and VWAP = :9
#                             and HI_52_WK = :10
#                             and LO_52_WK = :11
#                     )"""
# cols = apiConnect.new_col_order
# start_date = date(2023, 1, 1)
# end_date = date(2023, 9, 16)
# con = dbConnect.create_connection(username, password, server)
# df_final = dataframeOps.initialize_empty_dataframe()
# failure_symbol = []
# if con is not None:
#     cur = dbConnect.create_cursor(con)
#     if cur is not None:
#         exe = dbConnect.execute_query(cur, query)
#         if exe is not None:
#             result = dbConnect.fetch_data(exe, 1)
#             if result is not None:
#                 print("================================================================================")
#                 for symbol in result:
#                     print("Started for: "+symbol[0])
#                     try:
#                         df_temp = apiConnect.get_historical_data(symbol[0], start_date, end_date)
#                         df_final = dataframeOps.concat_dataframes(df_final,df_temp)
#                         for index, row in df_temp.iterrows():
#                             cur.execute(insert_data, (row[cols[0]],row[cols[1]],row[cols[2]],row[cols[3]],row[cols[4]],row[cols[5]],row[cols[6]],row[cols[7]],row[cols[8]],row[cols[9]],row[cols[10]]))
#                         con.commit()
#                         print(symbol[0] + " data inserted")
#                         print("===============================================================================")
#                     except Exception as e:
#                         print("Failed for: "+symbol[0])
#                         failure_symbol.append(symbol[0])
#                         print("================================================================================")
#                         pass
#
#     cur.close()
# con.close()
#
# #df = apiConnect.get_historical_data('AAATECH', date(2023,1,1), date(2023,9,9))
#
# #print(df_final.columns)
# if len(failure_symbol) != 0:
#     print("The failure symbols are")
#     print(failure_symbol)
# else:
#     print("No failure")