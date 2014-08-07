import sys

file = sys.argv[1]

target = 'target'
if 'country' in file or 'countries' in file:
	target = 'country'
if 'profession' in file:
	target = 'profession'

f = open(file, 'r')
lines = f.readlines()
lines = [line.strip() for line in lines if line.strip() != '']

country_dict = {}
for i in range(0, len(lines),2):
	country = lines[i]
	words = lines[i+1]
	country_dict[country] = eval(words)

print 'Results for file: ' + file
print 'Number of ' + target + 's: ' + str(len(country_dict.keys()))

word_counts = {}
for country in country_dict.keys():
	for word_tuple in country_dict[country]:
		word = word_tuple[0]
		word_counts[word] = word_counts.get(word,0) + 1

print 'Number of unique words: ' + str(len(word_counts.keys()))
print 'Number of repeated words: ' + str(sum([1 for count in word_counts.values() if count > 1]))

num_empty = sum([1 for word_list in country_dict.values() if len(word_list) == 0])
print 'Number of ' + target + ' with no associated words: ' + str(num_empty)

words_per_country = [len(word_list) for word_list in country_dict.values()]
mean = sum(words_per_country)/len(words_per_country)
print 'Mean words per ' + target + ': ' + str(mean)
print 'Max words per ' + target + ': ' + str(max(words_per_country))