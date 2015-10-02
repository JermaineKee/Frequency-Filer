import re


def word_frequency(text):
    word = re.sub(r'[,.!-0-9]', "", text).lower().split()

    count = {}

    for x in word:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    return count


def main():
    with open('sample.txt') as s:
        text = s.read()
        for final_count in sorted(word_frequency(text).items(), key=lambda c: c[1], reverse=True)[:20]:
            print(final_count)

if __name__ == '__main__':
    main()
