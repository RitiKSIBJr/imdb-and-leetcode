from bs4 import BeautifulSoup
import requests
from requests import HTTPError
import os
import csv


def check_url(url):
    try:
        res = requests.get(url)
        res.raise_for_status
    except HTTPError as http_err:
        return http_err 
        
    except Exception as e:
        return e

    else:
        return res

def main():
    # file_size = os.path.getsize("filename.txt")

    # if file_size == 0:

    base_url = "http://books.toscrape.com/catalogue/category/books/fantasy_19/"
    with open("url.txt") as file:
        page = file.readline()

    res = check_url(base_url + page)
    if str(res) == "<Response [200]>":

        soup = BeautifulSoup(res.text,"html.parser")
        footer = soup.find("li", class_="current")
        next_url = soup.find("li", class_="next").a
        
        books = soup.find_all("li", class_ ="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for book in books:
            b= book.find("article", class_ = "product_pod")
            a = b.find("h3").a.text
            price = b.find("div", class_ = "product_price").p.text
            
            with open("filename.txt","a", encoding="utf-8") as f:
                writer = csv.DictWriter(f,fieldnames=["name","price"])
                writer.writerow({"name":a, "price":price})
            

        with open("url.txt","w") as file:
            file.write(next_url["href"])

        print(footer.text.strip())

    else:
        print(res)


    # else:
    #     with open("filename.txt") as file:
    #         for line in file:
    #             print(line.strip())
            

            

if __name__ == "__main__":
    main()

