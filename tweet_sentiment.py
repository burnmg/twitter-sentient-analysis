import sys
import json

def hw(sent_file, tweet_file):
    # score
    sum = 0
    scores = {}
    with open(sent_file) as f:
        for line in f:
            term, score = line.split("\t", 1)
            scores[term] = int(score)

    # get json structures
    with open(tweet_file) as f:
        for line in f:
            tweet_score = 0
            object = json.loads(line)
            if 'text' in object.keys():
                sentence = object['text']
                words = sentence.split()
                for word in words:
                    word = word.encode('utf-8')
                    if word in scores.keys():
                        tweet_score = tweet_score + scores[word]

                print tweet_score
            else:
                print 0


def lines(fp):
    print str(len(fp.readlines()))


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sys.argv[1], sys.argv[2])
    # lines(sent_file)
    # lines(tweet_file)


if __name__ == '__main__':
    main()
