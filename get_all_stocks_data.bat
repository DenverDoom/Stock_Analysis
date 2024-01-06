@echo off
set /p start_date="Enter start date (YYYY-MM-DD): "
set /p end_date="Enter end date (YYYY-MM-DD): "
C:\Users\user\PycharmProjects\Stock_Analysis\venv\Scripts\python.exe C:\Users\user\PycharmProjects\Stock_Analysis\update_stock_data.py %start_date% %end_date%
pause