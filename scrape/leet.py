from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import csv

def check_url(url):
    try:
        res = requests.get(url)
        res.raise_for_status
    except HTTPError as http_err:
        print(http_err)  
        
    except Exception as e:
        print(e)

    else:
        return res

def main():
    res = check_url("https://leetcode.com/problemset/all/")

    soup = BeautifulSoup(res.text,"html.parser")

    problems = soup.find_all("div", class_ = "odd:bg-layer-1 even:bg-overlay-1 dark:odd:bg-dark-layer-bg dark:even:bg-dark-fill-4")

    for problem in problems:
        sn = problem.find("div", class_="truncate overflow-hidden").text.split(".")[0]
        ques =  problem.find("div", class_="truncate overflow-hidden").text.split(".")[1]
        per =  problem.find("span").text
        # diff = problem.find("div", class_="mx-2 py-[11px]").span.text
        
        with open ("file2.txt","a") as file:
            writer = csv.DictWriter(file,fieldnames=["S.N", "Question", "Acceptance"])

            writer.writerow({"S.N":sn, "Question":ques, "Acceptance":per})  

if __name__ == "__main__":
    main()

   