# -*- coding: cp1250 -*-
import nltk, logging

from flask import Flask, jsonify, request, json

app = Flask(__name__)

@app.route("/getTags", methods=['POST'])
def getTags():
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

@app.route("/saveTags", methods=['POST'])
def saveTags():
# Webova sluzba 2:  in: {temata (z WS1), ID clanku}
#                  out: {ulozeno / neulozeno do DB}
    return "Ahoj vole"

@app.route("/getRelevant", methods=['GET'])
def getRelevant():
# Webova sluzba 3:  in: klicova slova a casove rozmezi
#                  out: články podle relevance
    return "Ahoj vole"


@app.route("/getSummary", methods=['GET'])
def getSummary():
# Webova sluzba 4:  in: ID clánku
#                  out: vycuc podstatného textu
    return "Ahoj vole"


if __name__ == "__main__":
	app.debug = True
	app.run()
