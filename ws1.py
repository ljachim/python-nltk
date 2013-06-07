import nltk, logging

from flask import Flask, jsonify, request, json

app = Flask(__name__)

@app.route("/ws1", methods=['POST'])
def ws1():
# Webova sluzba 1:  in: {sentence:"English text to be processed"}
#                  out: {keywords}

# TODO length a vyskyt taky jako parametr, ale bude k tomu v kodu default 

	sentence  = request.json["sentence"]
	min_delka = 1 #request.json["min_length"]
	min_dist  = 0 #request.json["min_dist"]

        logging.warning (sentence)

	tags = nltk.pos_tag(nltk.word_tokenize(sentence))
	words = []
	retval = []

	for i in tags:
	    if not i[0] in nltk.corpus.stopwords.words('english'):
	        if i[1] in ('NNP','NNS','NN','JJ','JJR','JJS'):
	            words.append(i[0])

	fdist = nltk.FreqDist(words)

	for w in fdist.keys():
		if len(w) > min_delka and fdist[w] > min_dist:
			retval.append(w) 

	return jsonify(keywords=retval)


@app.route("/ws2", methods=['POST'])
def ws2():
# Webova sluzba 2:  in: {temata (z WS1)}
#                  out: {}
    return "Ahoj vole"


@app.route("/ws3", methods=['POST'])
def ws3():
# Webova sluzba 3:  in: klicova slova a clanky
#                  out: summary vychazejici z nejrelevantnejsiho clanku
    return "Ahoj vole"


if __name__ == "__main__":
	app.debug = True
	app.run()
