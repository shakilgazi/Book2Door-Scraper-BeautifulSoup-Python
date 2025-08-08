
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from openpyxl.workbook import Workbook
import re


page_number = 1

books_store = []

proceed = True


while(proceed):
    
    print(f"Scraping page number is : {page_number}")


    url = "https://www.books2door.com/collections/new-fiction?page="+str(page_number)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")


    # books_dic = {}



    # proceed = True



    if soup.find_all("div", class_="productgrid--no-results"):
        proceed = False
        # s <div class="productgrid--no-results">
            #   <h2 class="productgrid--no-results-title">There are no products matching your search
    else:
        all_books = soup.find_all("div", class_= "productgrid--item")

        for books in all_books:
            book_items = {}

            try:


                book_items["Page Number"] = page_number
                
                books_name_tag = books.find("img")
                book_items["Book Name"] = books_name_tag['alt'] if books_name_tag else "N/A"

                books_price_before_tag = books.find("span", class_ = "money price__compare-at--single")
                book_items["Price Before Discount"] = books_price_before_tag.text.strip() if books_price_before_tag else "N/A"

                
                books_discount_tag = books.find("span", class_= "productitem__badge--sale")
                
                if books_discount_tag:
                    discount_number_search = re.search(r'\d+', books_discount_tag.text)

                    if discount_number_search:
                        
                        book_items["Discount"] = discount_number_search.group(0) + "%"
                    else:
                        book_iteams["Discount"] = "N/A"

                else: 
                    book_iteams["Discount"] = "N/A"


                books_final_price_tag = books.find("span", class_="money")
                book_items["Final Price"] = books_final_price_tag.text.strip() if books_final_price_tag else "N/A"
            
                books_stock_status_tag = books.find("div", class_ = "product-stock-level__badge-text")
                book_items["Stock Status"] = books_stock_status_tag.text.strip() if books_stock_status_tag else "N/A"

                books_store.append(book_items)
            
            except Exception as e:
                print(f"Error processing book: {e}")
                continue

    page_number += 1

    # print(books_store)
    # print(f"total number of books data stored: {len(books_store)}")

# for i, book in enumerate(books_store, 1):
#     print(f"Book {i} :")
#     print(f"Name : {book['Name']}")
#     print(f"Price_Before : {book['Price_Before']}")
#     print(f"Discount : {book['Discount']}")
#     print(f"Final_Price : {book['Final_Price']}")
#     print(f"Stock_Status : {book['Stock_Status']}")
#     print("_" * 50)
#     print()



dataframe = pd.DataFrame(books_store)
dataframe.to_excel("Books_store.xlsx")
    # dataframe.to_csv("Books_store.csv")




# python3 book_store_scraping.py



