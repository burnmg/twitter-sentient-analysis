import sys
import json
import operator


def main():
    scores = get_scores(sys.argv[1])

    states_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    for key, value in states_dict.items():
        states_dict[key] = value.islower()

    print get_happiest_state(scores, sys.argv[2], states_dict)


def get_scores(sent_file):
    scores = {}
    with open(sent_file) as f:
        for line in f:
            term, score = line.split("\t", 1)
            scores[term] = int(score)
    return scores


def get_happiest_state(scores, tweet_file, states_dict):

    states_scores = {}
    for key, item in states_dict.items():
        states_scores[key] = 0

    # get json structures and update scores for each state
    with open(tweet_file) as f:
        for line in f:
            tweet_score = 0
            json_data = json.loads(line)
            if 'text' in json_data.keys():
                sentence = json_data['text']
                words = sentence.split()
                for word in words:
                    word = word.encode('utf-8')
                    if word in scores.keys():
                        tweet_score = tweet_score + scores[word]
            if 'location' in json_data.keys() and json_data['location'] is not None:
                strings = json_data['location'].split(',| ')
                for place in strings:
                    assert isinstance(place,str)
                    place = place.islower()
                    if place in states_dict.values():
                        state_code = get_key_by_value(states_dict, place)
                        states_scores[state_code] += tweet_score

    return max(states_scores.iteritems(), key=operator.itemgetter(1))[0]


def get_key_by_value(dict, t_value):
    for key, value in dict.items():
        if t_value is value:
            return key
    raise ValueError('this value is not in the dict')

if __name__ == '__main__':
    main()
