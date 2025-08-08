# Book2Door-Scraper-BeautifulSoup-python

A Python script using BeautifulSoup to scrape book data from Books2Door (https://www.books2door.com/collections/new-fiction), including book name, price before discount, discount percentage, final price, and stock status. Designed for e-commerce analysis, it exports clean, structured data to Excel for price monitoring, market research, or inventory tracking. This project complements other scraping initiatives (e.g., news or product data) to provide holistic market insights.

Overview

This project automates the extraction of book listings from Books2Door, a UK-based online bookstore, using the requests library and BeautifulSoup for web scraping. It targets the "New Fiction" collection, scraping key data points: book name, price before discount, discount percentage, final price, and stock status. The script handles pagination, processes dynamic HTML, and exports results to an Excel file (Books_store.xlsx) using Pandas, making it ideal for e-commerce businesses or researchers analyzing book pricing trends.

Developed as part of a broader e-commerce data scraping portfolio, this tool complements projects like news scraping (e.g., The Daily Star) and product scraping (e.g., eBay) to combine retail data with market trends. It’s suitable for price tracking, competitor analysis, or inventory management.

Features

Automated Scraping: Extracts book data from Books2Door’s "New Fiction" collection across multiple pages.

Data Points: Captures book name, price before discount, discount percentage, final price, and stock status.

Data Export: Saves results to Excel (Books_store.xlsx) for easy analysis.

Pagination Handling: Navigates all available pages until no results are found.

Error Handling: Robust exception handling ensures reliable scraping despite missing or dynamic elements.

Regex Parsing: Extracts discount percentages using regular expressions for accuracy.

Customizable: Adaptable for other Books2Door collections or e-commerce websites.

Technologies

Python: Core language for scripting.

BeautifulSoup: HTML parsing for data extraction.

Requests: Fetches web pages from Books2Door.

Pandas: Data manipulation and Excel export.

NumPy: Supports data processing (included for potential extensions).

OpenPyXL: Handles Excel file creation.

Regular Expressions (re): Parses discount percentages.
