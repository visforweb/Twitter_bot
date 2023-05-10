import pywhatkit as w
import requests
from bs4 import BeautifulSoup
response = requests.get("https://bhagavadgita.io/verse-of-the-day/")
web_page = response.text

"""create soup object"""
soup = BeautifulSoup(web_page, "html.parser")
bhagwat_sloka = soup.find(name="p", class_="verse-sanskrit").text
print(bhagwat_sloka)
shloka_meaning = soup.find(name="p", class_="verse-meaning").text
print(shloka_meaning)
print()
final_text = f"The Geeta Shloka of the Day is:\n{bhagwat_sloka}\nIts meaning is:\n{shloka_meaning}"
# y = str(bhagwat_sloka)
print(final_text)
w.sendwhatmsg_instantly("+919835469964",f"{final_text}")