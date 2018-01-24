# coding: utf-8
# div class="listings-container"

# div class=listing-card-wrapper

#		title --> span class ="listing-name--display"
#		price --> span class="price-amount"
# 		guest --> span class="person-capacity"
#		reviews --> get all span inside block and get the final

from selenium import webdriver
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class Room():
	"""docstring for Room"""
	def __init__(self):
		self.title = ""
		self.price = ""
		self.guests = ""
		self.review = ""
		
def get_all_room_all_page():

	room_list = []

	url = 'https://www.airbnb.com/s/New-York--NY--United-States?checkin=09%2F13%2F2016&checkout=09%2F15%2F2016&guests=1&zoom=12&search_by_map=true&sw_lat=40.628328897408736&sw_lng=-74.21733629193693&ne_lat=40.806739059800066&ne_lng=-74.07588731732756&ss_id=puaxgepi&page=1&source=map&airbnb_plus_only=false&s_tag=y8aSVLPW'

	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver.get(url)

	soup = BeautifulSoup(driver.page_source,'lxml')


	# get number of pages

	div_paging = soup.find('div', class_ = 'pagination')

	page_num = int(div_paging.find_all('li')[len(div_paging.find_all('li')) - 2].text)

	print page_num

	for page in range(1,page_num + 1):

		new_url = url + '&page={0}'.format(page)

		driver.get(new_url)

		soup = BeautifulSoup(driver.page_source,'lxml')

		div = soup.find('div',class_ = 'listings-container')

		for s_div in div.find_all('div', class_ = 'listings-card-wrapper'):

			print s_div.find('span', class_ ='listing-name--display').text
			print s_div.find('span', class_ = 'price-amount').text
			print s_div.find('span', class_ = 'person-capacity').text.strip(' · ')
			if 'reviews' in s_div.text:
				# get the final span tag
				print s_div.find_all('span')[len(s_div.find_all('span')) - 1].text
			print('\n')

			room = Room()

			room.title = s_div.find('span', class_='listing-name--display').text
			room.price = s_div.find('span', class_ = 'price-amount').text
			room.guests = s_div.find('span', class_ = 'person-capacity').text.strip(' · ')
			room.review = s_div.find_all('span')[len(s_div.find_all('span')) - 1].text

			room_list.append(room)

	for room in room_list:
		print room.title
		print room.price
		print room.guests
		print room.review

		driver.quit()

get_all_room_all_page()


driver.quit()