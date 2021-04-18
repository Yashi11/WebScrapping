from bs4 import BeautifulSoup
import requests


def extract_news():
    # get html text for mentioned url
    html_text = requests.get('https://inshorts.com/en/read').text
    soup = BeautifulSoup(html_text, 'lxml')
    with open('news_data.txt', 'a') as f:
        titles = soup.find_all('div', class_='news-card-title news-right-box')
        contents = soup.find_all(
            'div', class_='news-card-content news-right-box')
        sources = soup.find_all('div', class_='read-more')

        i = 1
        for title in titles:
            heading = title.find('span').text
            print(f"\n\n#{i}\n\n\n ")
            f.write("\n\n#"+str(i)+"\n\n\n")
            print("HEADING: \t"+heading)
            try:
                f.write("HEADING:   "+heading)
            except:
                f.write(
                    "HEADING:     Couldn't Print this Data due to Unknown symbol encounter")
            description = contents[i-1].find('div').text

            print("\nDESCRIPTION:\t" + description)
            try:
                f.write("\nDESCRIPTION:\t"+description)
            except:
                f.write(
                    "\nDESCRIPTION:   Couldn't Print this Data due to Unknown symbol encounter")
            try:
                a = sources[i-1].find('a', class_='source')
            except:
                print("")
            try:
                print("\nSOURCES:\t"+a['href'])
                f.write("\nSOURCES:\t"+a['href'])
            except:
                print("\nSOURCES:\t Not Available")
                f.write("\nSOURCES:\t Not Available")
            i += 1


extract_news()
print("\n\n\n\nAll the data has been added to 'news_data.txt' for future use")

