import numpy as np
import math
import csv
import json

class Beer:
	
	def __init__(self,style_name,flavor_profile_number,abvmin,abvmax,srmmin,srmmax,ibumin,ibumax,tmin,tmax):
		flavor_profiles = {1:"crisp",2:"hoppy",3:"malty",4:"roasty",5:"smokey",6:"fruit-spice",7:"sour"}

		self.style_name = style_name
		self.profile = flavor_profiles[flavor_profile_number]
		self.abv = np.linspace(abvmin,abvmax,23)
		self.srm = range(srmmin,srmmax+1)
		self.ibu = range(ibumin, ibumax+1)
		self.serving_temperature = range(tmin,tmax+1)


	def list_all_possible_beer(self):
		style_list = []
		for a in self.abv:
			a = np.around(a, decimals=1)
			for s in self.srm:
				for i in self.ibu:
					for t in self.serving_temperature:
						#paired_weather_temp = t
						beerTuple= (self.style_name, self.profile, a, s, i, t)
						#beerTuple (style name, flavor profile, abv, srm, ibu, serving temperature, calculated weather pairing temp)
						style_list.append(beerTuple)
		return(style_list)

def make_beer_csv():
	#style_name,flavor_profile_number,abvmin,abvmax,srmmin,srmmax,ibumin,ibumax,tmin,tmax
	beer_data=[]
	
	print "loading beers..."
	beer1 = Beer("American Amber Ale",1,4.4,6.1,11,18,25,45,45,55)
	beer2 = Beer("American Pale Ale",2,4.4,5.5,6,14,30,50,45,55)
	beer3 = Beer("English-Style Bitter",3,3,4.2,5,12,20,35,50,55)
	beer4 = Beer("American IPA",2,6.3,7.6,6,14,50,70,50,55)
	beer5 = Beer("Blonde Ale",1,4.1,5.1,3,7,15,25,45,50)
	beer6 = Beer("English-Style Pale Ale",3,4.4,5.3,5,12,20,40,50,55)
	beer7 = Beer("American Amber Lager", 1,4.8,5.4,6,14,18,30,43,50)
	beer8 = Beer("German-Style Dunkel",3,4.8,5.3,15,17,16,25,45,50)
	beer9 = Beer("German-Style Marzen / Oktoberfest",1, 5.1,6.0,4,15,18,25,45,50)
	beer10 = Beer("German-Style Schwarzbier",4,3.8,4.9,25,30,22,30,45,50)
	beer11 = Beer("Vienna-Style Lager",1,4.8,5.4,12,26,22,28,45,50)
	beer12 = Beer("American Brown Ale",3,4.2,6.3,15,26,25,45,50,55)
	beer13 = Beer("English-Style Brown Ale",3,4.2,6.0,12,17,15,25,50,55)
	beer14 = Beer("English-Style Mild",3,3.4,4.4,17,34,10,24,50,55)
	beer15 = Beer("English-Stlye IPA",2,5.1,7.1,6,14,35,63,45,50)
	beer16 = Beer("Imperial IPA",2,7.6,10.6,5,16,65,100,50,55)
	beer17 = Beer("American-Style Wheat Wine Ale",3,8.5,12.2,5,15,45,85,50,55)
	beer18 = Beer("American Wheat",1,3.5,5.6,2,10,10,35,40,45)
	beer19 = Beer("Belgian-Style Witbier",6,4.8,5.6,2,4,10,17,40,45)
	beer20 = Beer("Berliner Weiss",7,2.8,3.4,2,4,3,6,45,50)
	beer21 = Beer("Dunkelweizen",6,4.8,5.4,10,25,10,15,45,50)
	beer22 = Beer("German-Style Hefewizen",6,4.9,5.6,3,9,10,15,40,45)
	beer23 = Beer("American Barley Wine",2,8.5,12.2,11,18,60,100,50,55)
	beer24 = Beer("American Imperial Red Ale",2,8,10.6,10,17,55,85,50,55)
	beer25 = Beer("British-Style Barley Wine Ale",3,8.5,12,14,22,40,60,50,55)
	beer26 = Beer("English-Style Old Ale",3,6.5,9,12,22,30,60,43,45)
	beer27 = Beer("Belgian-Style Blonde Ale",1,6.3,7.9,4,7,15,30,45,50)
	beer28 = Beer("Belgian-Style Dubbel",6,6.3,7.6,16,36,20,35,50,55)
	beer29 = Beer("Belgian-Style Golden Strong Ale",6,7.1,11.2,3,10,20,50,40,45)
	beer30 = Beer("Belgian-Style Pale Ale",3,4.1,6.3,6,12,20,30,40,50)
	beer31 = Beer("Belgian-Style Quadrupel",6,9.1,14.2,8,20,25,50,50,55)
	beer32 = Beer("Belgian-Style Saison",6,4.4,8.4,4,14,20,38,45,55)
	beer33 = Beer("Belgian-Style Tripel",6,7.1,10.1,4,9,20,45,40,45)
	beer34 = Beer("American Cream Ale",1,4.3,5.7,2,5,10,22,40,45)
	beer35 = Beer("Biere de Garde",3,4.4,8,7,16,20,30,45,55)
	beer36 = Beer("California Common",2,4.6,5.7,8,15,35,45,50,55)
	beer37 = Beer("Altbier",3,4.6,5.6,11,19,25,52,45,50)
	beer38 = Beer("Kolsch",1,4.8,5.3,3,6,18,28,40,45)
	beer39 = Beer("Irish-Style Red",3,4.1,4.6,11,18,20,28,45,55)
	beer40 = Beer("American Imperial Porter",3,7,12,38,41,35,50,50,55)
	beer41 = Beer("Baltic-Style Porter",3,7.6,9.3,38,41,35,40,45,50)
	beer42 = Beer("English-Style Brown Porter",3,4.4,6,30,35,20,30,50,55)
	beer43 = Beer("Robust Porter",3,5.1,6.6,30,40,25,40,50,55)
	beer44 = Beer("Smoke Porter",5,5.1,8.9,20,40,20,40,50,55)
	beer45 = Beer("American Imperial Stout",4,7,12,38,41,50,80,50,55)
	beer46 = Beer("American Stout",4,5.7,8.9,38,41,35,60,50,55)
	beer47 = Beer("English-Style Oatmeal Stout",4,3.8,6.1,20,40,20,40,50,55)
	beer48 = Beer("English_Style Sweet Stout",3,3.2,6.3,38,41,15,25,50,55)
	beer49 = Beer("Irish-Style Dry Stout",4,4.2,5.3,38,41,30,40,50,55)
	beer50 = Beer("German-Style Bock",3,6.3,7.6,20,30,20,30,45,50)
	beer51 = Beer("German-Style Doppelbock",3,6.6,7.9,12,30,17,27,45,50)
	beer52 = Beer("German-Style Maibock",1,6.3,8.1,4,9,20,38,45,55)
	beer53 = Beer("German-Style Weizenbock",6,7,9.5,4,30,15,35,45,55)
	beer54 = Beer("Scotch Ale/Wee Heavy",3,6.6,8.5,15,30,25,35,50,55)
	beer55 = Beer("Scottish-Style Ale",3,2.8,5.3,6,15,9,25,50,55)
	beer56 = Beer("Belgian-Style Flanders",7,4.8,6.6,12,25,5,18,45,50)
	beer57 = Beer("Belgian-Style Fruit Lambic",7,5,8.9,1,25,15,21,45,50)
	beer58 = Beer("Gueuze",7,6.3,8.9,6,13,9,13,40,50)
	beer59 = Beer("Gose",7,4.4,5.4,3,9,10,15,40,50)
	beer60 = Beer("American Lager",1,4.1,5.1,2,6,5,15,33,45)
	beer61 = Beer("Bohemian-Style Pilsener",1,4.1,5.1,3,7,30,45,35,45)
	beer62 = Beer("European-Style Export",3,5.1,6.1,3,6,23,29,45,50)
	beer63 = Beer("German_Stlye Helles",1,4.8,5.6,4,6,18,25,45,50)
	beer64 = Beer("German-Style Pilsener",1,4.6,5.3,3,4,25,40,35,45)
	beer65 = Beer("American Black Ale",4,6.3,7.6,35,40,50,70,50,55)
	beer66 = Beer("Smoked Beer",5,4.8,5.5,22,30,29,32,45,55)
	beer67 = Beer("Grodziskie",5,2.5,5,2,5,20,30,45,50)
	beer68 = Beer("Classic Rauchbier",5,4.8,6.6,12,22,20,30,45,55)
	beer69 = Beer("American Pilsener",1,3.9,4.7,3,6,25,40,33,40)
	beer70 = Beer("Robust Porter",4,5.1,6.6,30,40,25,40,50,55)
	beer71 = Beer("Helles Lager",1,4.6,6,2,6,15,25,33,45)
	beer72 = Beer("Dortmunder Export",1,4.8,6,4,6,23,30,35,45)
	beer73 = Beer("Black IPA",2,5.5,9,25,40,50,90,50,55)
	beer74 = Beer("Oud Bruin",7,4.6,6.5,10,16,10,25,40,50)
	
	
	beer_list=[beer1, 
	beer2,
	beer3,
	beer4,
	beer5,
	beer6,
	beer7,
	beer8,
	beer9,
	beer10,
	beer11,
	beer12,
	beer13,
	beer14,
	beer15,
	beer16,
	beer17,
	beer18,
	beer19,
	beer20,
	beer21,
	beer22,
	beer23,
	beer24,
	beer25,
	beer26,
	beer27,
	beer28,
	beer29,
	beer30,
	beer31,
	beer32,
	beer33,
	beer34,
	beer35,
	beer36,
	beer37,
	beer38,
	beer39,
	beer40,
	beer41,
	beer42,
	beer43,
	beer44,
	beer45,
	beer46,
	beer47,
	beer48,
	beer49,
	beer50,
	beer51,
	beer52,
	beer53,
	beer54,
	beer55,
	beer56,
	beer57,
	beer58,
	beer59,
	beer60,
	beer61,
	beer62,
	beer63,
	beer64,
	beer65,
	beer66,
	beer67,
	beer68,
	beer69,
	beer70,
	beer71,
	beer72,
	beer73,
	beer74
	]
	print "starting...."
	for beer_style in beer_list:
		for beer in beer_style.list_all_possible_beer():
			beer_data.append(beer)
	
	with open('beerfile4.csv','wb') as out:
	    csv_out=csv.writer(out)
	    csv_out.writerow(['style_name','flavor_profile','abv','srm','ibu','temp'])
	    for row in beer_data:
	        csv_out.writerow(row)
	    print "Done!"
	    

def beerTemp(min,max):
	eMin = 32.0
	eMax = 100.0
	sMin = 33.0
	sMax = 55.0
	servTemp = {}
	envTemp = range(min,max)
	for t in envTemp:
		if t < eMin: 
			servTemp[t]=sMax
		elif t > eMax:
			servTemp[t]=sMin
		else:
			servTemp[t] = (-(sMax-sMin)/(eMax-eMin))*t+(eMax-sMin-1)
			print (t, -(sMax-sMin), eMax-eMin, eMax-sMin)
			print (-(sMax-sMin)/(eMax-eMin))*t+(eMax-sMin-1)

	for row in servTemp:
		pass
	    #print(row,servTemp[row])

#	with open('weather_abv.csv','wb') as out:
#	    csv_out=csv.writer(out)
#	    csv_out.writerow(['Ambient','Beer'])
#	    for row in servTemp:
#	    	for i in range(25):
#	    		csv_out.writerow((row,servTemp[row]))

def top_beer(beer_json, return_amount,step=10, max_multi=100):
	best = []
	beers = beer_json['predictedScores']
	i=step
	max_best = return_amount

	while len(best) <= max_best:
		multi = 1
		while i >= 0:
			for b in beers:
				#print("beer: ",b)
				score = float(beers[b]) # exctract score
				if score*multi*i > 1: 
					best.append((b,score))
					print len(best)
					multi += 11
					
			i-=1

		print best
		if multi >= max_multi:
			max_best = len(best)
			

	
	return(best)
	    

def list_top_beers(beer_json,list_length=10,max_multiplier=100):
	beer_list = {}
	multiplier = 1
	beers = beer_json['predictedScores']
	lowest_score = 1
	highest_score = None
	smallest = None
	top_list = []
	


	while len(top_list)<list_length:
		
		for b in beers:
			score = float(beers[b])
			beer_list[b] = score 
			
			for s in beer_list:
				#print beer_list[s]
				if beer_list[s]>highest_score:
					highest_score = beer_list[s]

		



				
			




	

	return beer_list






file = '''
{
    "Prediction": {
        "details": {
            "Algorithm": "SGD",
            "PredictiveModelType": "MULTICLASS"
        },
        "predictedLabel": "American Wheat",
        "predictedScores": {
            "Altbier": 0.00005008252992411144,
            "American Amber Ale": 0.031345464289188385,
            "American Amber Lager": 0.0024085496552288532,
            "American Barley Wine": 0.0006729489541612566,
            "American Black Ale": 0.0005472858902066946,
            "American Brown Ale": 0.003061392344534397,
            "American Cream Ale": 0.03183748200535774,
            "American IPA": 0.00039526086766272783,
            "American Imperial Porter": 0.00041129632154479623,
            "American Imperial Red Ale": 0.0006138182361610234,
            "American Imperial Stout": 0.0006588642136193812,
            "American Lager": 0.017590006813406944,
            "American Pale Ale": 0.00017562491120770574,
            "American Stout": 0.00046322972048074007,
            "American Wheat": 0.3265956938266754,
            "American-Style Wheat Wine Ale": 0.000054418924264609814,
            "Baltic-Style Porter": 0.0003742260450962931,
            "Belgian-Style Blonde Ale": 0.003693891456350684,
            "Belgian-Style Dubbel": 0.0026197293773293495,
            "Belgian-Style Flanders": 0.0016251771012321115,
            "Belgian-Style Fruit Lambic": 0.00020706243230961263,
            "Belgian-Style Golden Strong Ale": 0.005131822545081377,
            "Belgian-Style Pale Ale": 0.0014157355763018131,
            "Belgian-Style Quadrupel": 0.00004437037932802923,
            "Belgian-Style Saison": 0.000005290320586937014,
            "Belgian-Style Tripel": 0.004187232349067926,
            "Belgian-Style Witbier": 0.0007207707967609167,
            "Berliner Weiss": 0.0002310557320015505,
            "Biere de Garde": 0.000013320075595402159,
            "Blonde Ale": 0.0009315207717008889,
            "Bohemian-Style Pilsener": 0.06288553029298782,
            "British-Style Barley Wine Ale": 0.0016911060083657503,
            "California Common": 0.00040253953193314373,
            "Classic Rauchbier": 0.0005234486889094114,
            "Dunkelweizen": 0.0005421492387540638,
            "English-Stlye IPA": 0.00019711811910383403,
            "English-Style Bitter": 0.00006657448102487251,
            "English-Style Brown Ale": 0.00017206543998327106,
            "English-Style Brown Porter": 0.00028075859881937504,
            "English-Style Mild": 0.003821906866505742,
            "English-Style Oatmeal Stout": 0.001573257613927126,
            "English-Style Old Ale": 0.23961865901947021,
            "English-Style Pale Ale": 0.00002986168874485884,
            "English_Style Sweet Stout": 0.0003742646367754787,
            "European-Style Export": 0.00008209158841054887,
            "German-Style Bock": 0.0021670504938811064,
            "German-Style Doppelbock": 0.0005621368763968349,
            "German-Style Dunkel": 0.00022519868798553944,
            "German-Style Hefewizen": 0.0010248641483485699,
            "German-Style Maibock": 0.009021246805787086,
            "German-Style Marzen / Oktoberfest": 0.0017808856209740043,
            "German-Style Pilsener": 0.025259027257561684,
            "German-Style Schwarzbier": 0.0010117196943610907,
            "German-Style Weizenbock": 0.00006056849815649912,
            "German_Stlye Helles": 0.0008907640585675836,
            "Gose": 0.00027682905783876777,
            "Grodziskie": 0.00009354094800073653,
            "Gueuze": 0.000830676406621933,
            "Imperial IPA": 0.0004551514866761863,
            "Irish-Style Dry Stout": 0.00031176823540590703,
            "Irish-Style Red": 0.00006778650276828557,
            "Kolsch": 0.03038702718913555,
            "Robust Porter": 0.00018402066780254245,
            "Scotch Ale/Wee Heavy": 0.0006992684793658555,
            "Scottish-Style Ale": 0.000029690600058529526,
            "Smoke Porter": 0.0027280559297651052,
            "Smoked Beer": 0.0029786129016429186,
            "Vienna-Style Lager": 0.16861017048358917
        }
    }
}
'''


beer_scores = json.loads(file)['Prediction']
#beerTemp(-30,120)
#make_beer_csv()


topbeerlist= list_top_beers(beer_scores)

for beer in topbeerlist:
	#print (beer,topbeerlist[beer]), "\n"
	pass




