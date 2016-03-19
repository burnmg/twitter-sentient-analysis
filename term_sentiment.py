import sys
import json

def hw(sent_file, tweet_file):

    scores = {}
    with open(sent_file) as f:
        for line in f:
            term, score = line.split("\t", 1)
            scores[term] = int(score)

    est_sent = {}
    # estimate est_sent
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
                    else:
                        if word not in est_sent:
                            est_sent[word] = 0
                for word in words:
                    word = word.encode('utf-8')
                    if word in est_sent.keys():
                        est_sent[word] += tweet_score

    for key, value in est_sent.items():
        print key,value


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
