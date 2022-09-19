from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import csv

def get_valid_url(url):

    try:
        res = requests.get(url)
        res.raise_for_status

    except HTTPError as http_err:
        raise http_err
        
    except Exception as e:
        raise e

    else:
        return res

def main():

    page = get_valid_url("https://www.imdb.com/chart/top/")

    if page is Exception:
        print(Exception)
    
    else:
        soup = BeautifulSoup(page.text,"html.parser")

        movies = soup.find("tbody", class_="lister-list").find_all("tr")

        for movie in movies:
            
            rank = movie.find("td", class_="titleColumn").get_text(strip = True).split(".")[0]
            title = movie.find("td", class_="titleColumn").a.text
            year = movie.find("td", class_="titleColumn").find("span", class_="secondaryInfo").text.strip("()")
            rating = movie.find("td", class_="ratingColumn imdbRating").strong.text

            with open("file.txt","a") as file:
                writer = csv.DictWriter(file,fieldnames=["S.N","Name","Year","Rating"])
                writer.writerow({"S.N":rank, "Name":title, "Year":year, "Rating": rating})

      

if __name__ == "__main__":
    main()