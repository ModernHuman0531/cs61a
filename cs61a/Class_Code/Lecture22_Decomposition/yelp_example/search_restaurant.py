#First idea, to find the key word that picks the most similar three restaurant
def search(query, ranking = lambda r:-r.stars):# query is the key word we search, add - in order to give the high ranking first
    results = [r for r in Restaurant.all if query in r.name]
    #Determine how we return the result fo the finding restaurant.(Usually it'll sort by ranking)
    return sorted(results, key = ranking)#Maybe we can make a default of ranking function
#------------------------------------------------------------------------For the upper code, we just assume the code know what is contain in restautant, and do the search
#------------------------------------------------------------------------Now we arre going to actually define what is in the restaurant
def reviewed_both(r, s):
    return len([x for x in r.reviewers if x in s.reviewer])
class Restaurant:
    #How to keep track of all restaurant:
    all = []
    #Instead of use the global name, we can use Class instance to leep track of
    def __init__(self, name, stars, reviewers):#We already know we need the name, and stars to give the rank
        self.name, self.stars, self.reviewers = name, stars, reviewers
        Restaurant.all.append(self)
    def similar(self, k, similarity = reviewed_both):#Pass in the similarity func that determine how similar two restaurant are
        """Return the k most similar restaurants to SELF"""
        other = list(Restaurant.all)
        other.remove(self)# Other should exclusive itself
        return sorted(other, key = lambda r:-similarity(self, r))[:k]#Key function must be one argument function
    def __repr__(self):
        return '<' + self.name +'>'
#Restaurant('Thai Delight', 2)
#Restaurant('Thai Basil', 3)
#Restaurant('Top Dog', 5)
#Read the restaurant through the file.
import json

reviewers_for_restaurant = {}
for line in open('reviews.json'):
    r = json.loads(line)
    biz = r['business_id']
    if biz not in reviewers_for_restaurant:
        reviewers_for_restaurant[biz] = [r['user_id']]
    else:
        reviewers_for_restaurant[biz].append(r['user_id'])
for line in open('restaurants.json'):
    r = json.loads(line)#r receive a dictionary
    reviewers = reviewers_for_restaurant[r['business_id']]
    Restaurant(r['name'], ['stars'], reviewers)

results = search('Thai')# Key word we search
for r in results:
    print(r,'is similar to', r.similar(3))#We must create a similar function, to help us find the similar restairant
