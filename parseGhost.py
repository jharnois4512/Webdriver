from bs4 import BeautifulSoup
import json

adv = []
siteAna = []
custInt = []
social = []
essential = []
audio = []
adultAdv = []
comments = []
buildJson = {}

f = open("ghostery_extract.html", "r")
soup = BeautifulSoup(f, "html.parser")
outer = soup.find('div', {"class":"trackers-list"})
# outer = soup.find_all('div', {"class":"blocking-category"})
second = outer.find_all('div', {"class":"global-blocking-trk"})
for ents in second:
    adv.append(ents.find('div', {'class', 'columns trk-title'}).contents[0].contents[0])
f.close()

f = open("ghostery_social_media.html", "r")
soup = BeautifulSoup(f, "html.parser")
outer = soup.find('div', {"class":"trackers-list"})
# outer = soup.find_all('div', {"class":"blocking-category"})
second = outer.find_all('div', {"class":"global-blocking-trk"})
for ents in second:
    social.append(ents.find('div', {'class', 'columns trk-title'}).contents[0].contents[0])
f.close()

f = open("ghostery_adult.html", "r")
soup = BeautifulSoup(f, "html.parser")
outer = soup.find('div', {"class":"trackers-list"})
# outer = soup.find_all('div', {"class":"blocking-category"})
second = outer.find_all('div', {"class":"global-blocking-trk"})
for ents in second:
    adultAdv.append(ents.find('div', {'class', 'columns trk-title'}).contents[0].contents[0])
f.close()

f = open("ghostery_comment.html", "r")
soup = BeautifulSoup(f, "html.parser")
outer = soup.find('div', {"class":"trackers-list"})
# outer = soup.find_all('div', {"class":"blocking-category"})
second = outer.find_all('div', {"class":"global-blocking-trk"})
for ents in second:
    comments.append(ents.find('div', {'class', 'columns trk-title'}).contents[0].contents[0])
f.close()

f = open("ghostery_customer_interaction.html", "r")
soup = BeautifulSoup(f, "html.parser")
outer = soup.find('div', {"class":"trackers-list"})
# outer = soup.find_all('div', {"class":"blocking-category"})
second = outer.find_all('div', {"class":"global-blocking-trk"})
for ents in second:
    custInt.append(ents.find('div', {'class', 'columns trk-title'}).contents[0].contents[0])
f.close()

f = open("ghostery_site_analytics.html", "r")
soup = BeautifulSoup(f, "html.parser")
outer = soup.find('div', {"class":"trackers-list"})
# outer = soup.find_all('div', {"class":"blocking-category"})
second = outer.find_all('div', {"class":"global-blocking-trk"})
for ents in second:
    siteAna.append(ents.find('div', {'class', 'columns trk-title'}).contents[0].contents[0])
f.close()

f = open("ghostery_audio.html", "r")
soup = BeautifulSoup(f, "html.parser")
outer = soup.find('div', {"class":"trackers-list"})
# outer = soup.find_all('div', {"class":"blocking-category"})
second = outer.find_all('div', {"class":"global-blocking-trk"})
for ents in second:
    audio.append(ents.find('div', {'class', 'columns trk-title'}).contents[0].contents[0])
f.close()

f = open("ghostery_essential.html", "r")
soup = BeautifulSoup(f, "html.parser")
outer = soup.find('div', {"class":"trackers-list"})
# outer = soup.find_all('div', {"class":"blocking-category"})
second = outer.find_all('div', {"class":"global-blocking-trk"})
for ents in second:
    essential.append(ents.find('div', {'class', 'columns trk-title'}).contents[0].contents[0])
f.close()

buildJson['adv'] = adv
buildJson['siteAna'] = siteAna
buildJson['custInt'] = custInt
buildJson['social'] = social
buildJson['ess'] = essential
buildJson['audio'] = audio
buildJson['adultAdv'] = adultAdv
buildJson['comments'] = comments

with open('ghostery_json.json', 'w') as f:
    json.dump(buildJson, f)

