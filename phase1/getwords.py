import nltk
import math
subs  = open('./Transcripts/apple.vtt',"r");
transcript  = "start##";

def getOccurences(nouns, word):
	occurences = []
	occurence_seconds = []
	i = 0
	#print len(nouns)
	#print word
	while i < len(nouns):
		if nouns[i] == word:
			
			j = i
			while  ':' not in nouns[j] and j >= 2:
				j = j-1
			occurence  = nouns[j-1]
			if ':' in occurence:
				seconds = ( int(occurence.split(':')[0])*3600 + int(occurence.split(':')[1])*60 + int(math.floor(float(occurence.split(':')[2]))) )
				occurence_seconds.append(str(seconds))
				




		i = i+1	 
	return (word,occurence_seconds)

for line in subs:
	transcript = transcript + line


#essays = u"""text here"""
essays = transcript
tokens = nltk.word_tokenize(essays)

tagged = nltk.pos_tag(tokens)

nouns = [word for word,pos in tagged \
	if ( pos == 'NNS' or pos == 'NNP' or pos == 'CD')]

nouns2 = [word for word,pos in tagged \
	if ( pos == 'NNS' or pos == 'NNP')]

unique_nouns  = set(nouns2)

terms = []
for ns in unique_nouns:
	if len(ns) > 2:
		terms.append(getOccurences(nouns, ns))

downcased = [x.lower() for x in nouns]
#joined = " ".join(downcased).encode('utf-8')
into_string = str(nouns)


print terms[1][0]
output  = open('./Transcripts/output.txt',"rw+");
for word,time in terms:
	output.write(' { "term": "' + word + '", "score": 0.005' +', "timestamps": [')
	for t in time:
		output.write(t + ',')
	output.write('] }, ') 

output.close()
	
 
