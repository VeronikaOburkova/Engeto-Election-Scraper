import sys
import csv
import requests
from bs4 import BeautifulSoup

def get_data():
    website = requests.get(sys.argv[1])
    return BeautifulSoup(website.text, "html.parser")

def get_codes(website):
    codes = []
    links = []
    all_links = website.find_all
    for link in all_links:
        if link.text.isnumeric() and len(link.text) == 6:
            codes.append(link.text)
            links.append("https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ" + link["href"])
    return codes, links

def create_columns(link):
    columns = ["code", "location", "registered voters", "envelopes", "valid votes"]
    website = requests.get(link)
    parsing = BeautifulSoup(website.text, "html.parser")
    for object in parsing.find_all("td"):
        if object.text != "-":
            columns.append(object.text)
    return columns

def location_codes(lc_link, lc_code):
    location_code = [lc_code]
    lc_data = requests.get(lc_link)
    lc_data_bs = BeautifulSoup(lc_data.text, "html.parser")
    location_code.append(str(lc_data_bs.find_all("h3")[2].text).split(":")[1].strip()) # location
    location_code.append("".join(str(lc_data_bs.find_all("td")[3].text).split())) # registred voters
    location_code.append("".join(str(lc_data_bs.find_all("td")[4].text).split())) # envelopes
    location_code.append("".join(str(lc_data_bs.find_all("td")[7].text).split())) # valid votes
    for party in lc_data_bs.find_all("td")[11::5]:
        location_code.append(party.text) # objekt
        return location_code
    
def main():
    data = get_data()
    print("Exporting. Please wait!", sys.argv[1])
    codes, links = get_codes(data)
    header = create_columns(links[0])
    with open(sys.argv[2] + ".csv", "w", newline="") as file:
        file_writer = csv.writer(file, delimiter=";")
        file_writer.writerow(header)
        for i in range(len(codes)):
            file_writer.writerow(location_codes(links[i], codes[i]))
    print("Finished.")

main()
    


