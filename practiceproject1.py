from bs4 import BeautifulSoup
import requests


#Declaration Of Function
def codechef_extract(url):
    html_text = requests.get(url).text  #get html text for mentioned url
    soup = BeautifulSoup(html_text, 'lxml')
    f = open('data.txt','a')
    #Extraction of Information Starts---------------------------------


    #Extraction of User Details
    f.write("\n\n\n---------------->New CodeChef User Scrapping\n\n\n")
    name = soup.find_all('h2')[1].text
    f.write("User Details \n")
    f.write("\nName :\t"+name)
    country = soup.find('span', class_='user-country-name').text
    rating = soup.find('span', class_='rating').text
    f.write("\nRating :\t"+rating[0])
    f.write("\nCountry: \t"+country)
    details = soup.find('ul', class_='side-nav').text
    details1 = list(details.split(':'))
    state = details1[3].split()[0]
    f.write("\nState : \t"+state)
    city = details1[4].split()[0]
    f.write("\nCity : \t"+city)
    role = details1[5].split()[0]
    f.write("\nStudent/Professional : \t"+role)
    instn = details1[6].split("\n")[0]
    f.write("\nInstitution : \t"+instn)

    #Extraction of Performance Details

    rating_num = soup.find('div', class_='rating-number').text
    ranks = soup.find('div', class_='rating-ranks')
    r = ranks.find_all('li')
    rank_list = [r[0].text, r[1].text]
    global_rank = rank_list[0].split()[0]
    country_rank = rank_list[1].split()[0]
    f.write("\n\n User's Performance\n")
    f.write("\nHighest Rating : \t"+rating_num)
    f.write("\nGlobal Rank : \t"+global_rank)
    f.write("\nCountry Rank : \t"+country_rank)
    #Extraction of Contest Ranks From Rating Table

    table1 = soup.find('table', class_='rating-table')
    cr = []
    for element in table1.find_all('td'):
        cr.append(element.text)

    #Extraction of Team List from Hyperlinked URL

    url_teams = url + "/teams"
    html_text1 = requests.get(url_teams).text
    soup1 = BeautifulSoup(html_text1, 'lxml')
    table = soup1.find('table')
    teams = []
    for team in table.find_all('tbody'):
        rows = team.find_all('tr')
        for row in rows:
            team_details = row.find_all('td')
            r1 = []
            for detail in team_details:
                r1.append(detail.text)
            teams.append(r1)

    #Final Print of Information Starts----------------------------------------
    print("\n\n----> User Details")
    print(f" \nName:\t {name}\n Rating:\t {rating}\n Country:\t {country}\n State: {state}\n City: {city}\n Student\Professional: {role}\n Institution: {instn}")
    print("\n\n----> User's Performance")
    print(f"\nHighest Rating: {rating_num}\n Global Rank: {global_rank}\n Country Rank: {country_rank}")
    j = 0
    while j < 3:
        print(f"\n#CONTEST {j+1}")
        f.write("\n\n\n#CONTEST"+ str(j+1))
        print(f"\n\nContest Name: {cr[4*j]}\n Rating: {cr[(4*j) + 1]}\n Global Rank: {cr[(4*j)+2]}\n Country Rank: {cr[(4*j)+3]}")
        f.write("\nContest Name:\t"+cr[4*j])
        f.write("\nRating:\t"+cr[(4*j)+1])
        f.write("\nGlobal Rank:\t"+cr[(4*j)+2])
        f.write("\nCountry Rank:\t"+cr[(4*j)+3])
        j += 1
    print("\n\n----> Team Details")
    i = 1
    for team in teams:
        print(f"\n#{i}\n")
        f.write("\n\n Team #"+str(i))
        print(f"Team Name: {team[0]}")
        f.write("\nTeam Name:\t"+team[0])
        print(f"Contest: {team[1]}")
        f.write("\nContest:\t"+team[1])
        print(f"Role: {team[2]}")
        f.write("\nRole:\t"+team[2])
        i += 1

print("\tProgram to Extract Codechef User Information\n")  #introduction
user_name = input("Enter the user-name of the Chodechef User:\t")  #to get url of webpage
url = "https://www.codechef.com/users/" + user_name
codechef_extract(url)
print("\n\n Data Printed On the Screen has been stored in file: 'data.txt'  for future use. ")
