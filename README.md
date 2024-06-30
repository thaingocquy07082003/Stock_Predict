# Crawl data and predict stock prices the next day (until April 16, 2024 ) 

## Team Dev ( 1 people )
- Thái Ngọc Quý | 0342280638

## Struture of Project

```
Driver_Notes/
Crawl_VNINDEX.py
STOCK_PREDICT.ipynb
VNINDEX_STOCK.csv
msedgedriver.exe
```

1. **Driver_Notes/**: This folder contains Microsoft's installation and usage instructions for the Microsoft Edge browser.

2. **Crawl_VNINDEX.py**: This file crawls data from **"https://cafef.vn/"** to get stock price information and time to make training data for the LSTM model.

3. **STOCK_PREDICT.ipynb**: This file trains the VN-INDEX stock price prediction model based on collected data and it uses GPU from google collab.

4. **VNINDEX_STOCK.csv**: file csv csv file contains collected data.

5. **msedgedriver.exe**: is the executable file of Microsoft Edge WebDriver, a tool used to automate tasks related to the Microsoft Edge browser.
It allows developers and test automation engineers to execute tests and interact with the Edge browser through scripting.


## I. Overall this applications
- model AI : LSTM  ( Long short term memory ).
- 💻Tech Stack : tensorflow , keras , sklearn , selenium - language Python.
- Collab Notebook.

## II. Demo Production
