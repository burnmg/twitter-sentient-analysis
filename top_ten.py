import sys
import json
import operator

def main():
    sorted_dict = get_top_ten(sys.argv[1])
    for item in sorted_dict:
        (key, value) = item
        print key, value


def get_top_ten(senti_file):

    with open(sys.argv[1]) as f:
        occ_list = {}
        for line in f:
            json_data = json.loads(line)
            if 'text' in json_data.keys():
                for word in json_data['text'].split():
                    word = word.encode('utf-8')
                    if word not in occ_list.keys():
                        occ_list[word] = 1
                    else:
                        occ_list[word] += 1
    return sorted(occ_list.iteritems(), key=operator.itemgetter(1))[0:10]

if __name__ == '__main__':
    main()
