import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
url = "https://shiveshcodes.github.io/wncc-soc.github.io/soc/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
topics = soup.find_all('div', class_="rounded hover-wrapper pr-3 pl-3 pt-3 pb-3 bg-white")

for project in topics:
    item = {}  # Reset the dictionary for each project
    link = "https://shiveshcodes.github.io" + project.find('a')["href"]
    name = project.find('p', class_="lead text-center font-weight-bold text-dark").text
    item['project_name'] = name
    item['link'] = link
    
    individual_page = requests.get(link)
    soup = BeautifulSoup(individual_page.text, "html.parser")
    project_details = soup.find('div', class_="col-sm-10 col-md-8")
    mentor_names=""
    number_of_mentees=""
    mentor_tag = project_details.find_all('p', class_='lead')[0].text.strip()
    for char in mentor_tag:
     if char.isalpha():
      mentor_names+=char

     else :
      number_of_mentees+=char
    
    
    
    item["mentor_name"]=mentor_names
    item["number_of_mentees"]=number_of_mentees
    # Debug prints
    print(f"Project: {item['project_name']}")
    print(f"Mentors: {item['mentor_name']}")
    print(f"Mentees: {item['number_of_mentees']}")
    
    data.append(item)

df = pd.DataFrame(data)
df.to_excel("soc8.xlsx", index=False)
print("Data extraction complete. Excel file created.")