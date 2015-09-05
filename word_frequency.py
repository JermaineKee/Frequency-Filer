import re

def word_frequency(text):
    count = re.sub(r'[A-Za-z\s]', "", text).lower().split()


    word_count = {}



    for x in words:
        if x in word_count:
            word_count[x] += 1
        else:
            word_count[x] = 1
    return word_count


def main():
    text = open('sample.txt')
    text.read()
    for final_count in sorted(word_frequency(text).items(), key=lambda c: c[1], reverse=True)[:20]:
        print(final_count)

if __name__ == '__main__':
    main()
