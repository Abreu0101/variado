from math import sqrt

# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

def sim_distance(prefs,person1,person2):
	item_shared = {}
	for item in prefs[person1]:
		if item in prefs[person2]: item_shared[item] = 1

	if len(item_shared)==0: return 0

	distancia = sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in item_shared])

	return 1/(1+distancia)

def sim_pearson(prefs,person1,person2):
	item_shared = {}
	for item in prefs[person1]:
		if item in prefs[person2]: item_shared[item] = 1

	if len(item_shared)==0: return 0

	sum_person1 = sum([prefs[person1][item] for item in item_shared])
	sum_person2 = sum([prefs[person2][item] for item in item_shared])

	sum_sq_person1 = sum([pow(prefs[person1][item],2) for item in item_shared])
	sum_sq_person2 = sum([pow(prefs[person2][item],2) for item in item_shared])

	prod_ratings = sum([prefs[person1][item]*prefs[person2][item] for item in item_shared])

	num = prod_ratings - (sum_person1 * sum_person2/len(item_shared))
	den = sqrt((sum_sq_person1-pow(sum_person1,2)/len(item_shared))*(sum_sq_person2-pow(sum_person2,2)/len(item_shared)))

	if den == 0: return 0

	return num/den
	
def getTopMatches(prefs,person1,n=3,similitud=sim_pearson):
	score = [(similitud(prefs,person1,person2),person2) for person2 in prefs if person1 != person2]
	
	score.sort()
	score.reverse()
	
	return score
	
def getRecomendation(prefs,person1,n=5,similitud=sim_pearson):
	total={}
	sim_total = {}
	for other in prefs:
		if other == person1: continue
		sim = similitud(prefs,person1,other)
		if sim > 0:
			for item in prefs[other]:
				if item not in prefs[person1] or prefs[person1][item]==0:
					total.setdefault(item,0)
					total[item]+= sim * prefs[other][item]
					
					sim_total.setdefault(item,0)
					sim_total[item]+= sim
			
	ranking = [(total[item]/sim_total[item],item) for item in total]
	ranking.sort()
	ranking.reverse()
	
	return ranking
	
		
		
			
	
	
	


