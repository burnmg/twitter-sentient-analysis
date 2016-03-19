import sys
import json


def main():
    with open(sys.argv[1]) as f:

        occ_list = {}
        num_all_terms = 0
        for line in f:
            object = json.loads(line)
            if 'text' in object.keys():
                for word in object['text'].split():
                    word = word.encode('utf-8')
                    num_all_terms += 1
                    if word not in occ_list.keys():
                        occ_list[word] = 1
                    else:
                        occ_list[word] += 1

        for key, value in occ_list.items():
            print key, float(value)/num_all_terms


if __name__ == '__main__':
    main()
