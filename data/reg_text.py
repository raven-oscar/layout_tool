#!/usr/bin/python2
# -*- coding: utf-8 -*-

import csv
import re
import os
import images_plain_folder
import json


'''schema = {'page':string
			'header':string
			'text':string
			'mcc art':string
			'mgb art':string
			'price':string
			'image':string
			}'''


def init(images_path,data_path):
	#adv init
	adv_data = {}
	path = os.path.join(data_path,'adv.csv')	 
	with open(path,'rb') as csvfile:
		reader = csv.reader(csvfile,delimiter=';',quotechar='"')
		row_number = -1
		for row in reader:
			row_number += 1
			if row_number > 7:
				adv_data[row[1]] = {'header':row[9],
									'text':row[10],
									'image':row[0]}

	#PLR json
	#json_file = open(os.path.join(data_path,'plr_data.txt'))
	#json_data = json.load(json_file)
	#json_file.close()
	#plr_images = {}
	#for cataloge_id,cataloge_data in json.loads(json_data).iteritems():
	#	for prop_name,prop in cataloge_data.iteritems():
	#		if prop_name == 'Pages':
	#			for page_num,pages in prop.iteritems():
	#				for page_market,frames in pages.iteritems():						
	#					for frame_num,frame_data in frames.iteritems():
	#						if frame_data['mcc_art'] != None:
	#							try:
	#								plr_images[frame_data['mcc_art'][0]] = frame_data['images'][0]
	#							except IndexError:
	#								plr_images[frame_data['mcc_art'][0]] = None
	#reg init
	offers = {}
	image_pool = images_plain_folder.init(images_path)
	path = os.path.join(data_path,'68.csv')
	print path
	with open(path,'rb') as csvfile:
		reader = csv.reader(csvfile,delimiter=';',quotechar='"')
		row_number = -1
		for row in reader:
			row_number += 1
			if row_number > 7:
				mcc_art = row[8]
				mgb_art = row[2]
				
				header = adv_data[mcc_art]['header']
				text = adv_data[mcc_art]['text']				
				price = row[10].replace('.','')[:-1].replace(',','.')
				page = row[16]
				place_on_page = row[17]
				markets = row[1]
				image_art = adv_data[mcc_art]['image']
				if str(image_art) not in image_pool:
					image = {'text': 'place holder', 'image path': '/home/raven/git/pages/imageDb/test1.jpg', 'clipping path': False}
				else:
					image = image_pool[image_art]
				
				offer = {
						'page':page,
						'header':header,
						'text':text,
						'mcc art':mcc_art,
						'mgb art':mgb_art,
						'price':price,
						'image':image,
						'image override': None,
						'markets':markets,
						'feild':place_on_page
						}
				if page not in offers:
					offers[page] = [offer]
				else:
					array = offers[page]
					array.append(offer)
					offers[page] = array

	return offers 

if __name__ == '__main__':
	init('/home/raven/gen_projects/horeca_23/images/done/','/home/raven/gen_projects/horeca_23')
#	offers = {}
#	for key,value in init('/home/raven/git/pages/data/reg_source/horeca_reg.csv','/home/raven/git/pages/imageDb/horeca/').iteritems():
#		print key
#		ver_count = {}
#		for offer in value:
#			if offer['feild'] not in ver_count:
#				ver_count[offer['feild']] = 1
#			else:
#				counter = ver_count[offer['feild']]
#				counter += 1
#				ver_count[offer['feild']] = counter
		
		#cat versions
#		offers[key] = {}
#		if max(ver_count.values()) > 1:
#			for ver in range(1,max(ver_count.values())):
#				dt = offers[key]
#				dt[ver] = []
#				offers[key] = dt
#		else:
#			offers[key] = {ver:[]}
#		for offer in value:
#			if ver_count[offer['feild']] == 1:
#				for ver,ver_content in offer[key]:
#					print ver,ver_content
#				array = offers[key]
#				array.append(offer)
#				offers[key] = array 
			#print '\t',offer['mcc art']
#			print '\t\t',offer['feild'],ver_count[offer['feild']]
			#print '\t\t\t',offer['markets']