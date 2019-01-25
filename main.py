import argparse
import json

from core import CodeProgression, Tones


def main(data):
    tones = Tones()
    chords = list(map(lambda x: {
        'root': tones.get(x['root']),
        'harmony': x['harmony']
    }, data))

    for i in range(len(chords)-2):
        c1 = chords[i]
        c2 = chords[i+1]
        c3 = chords[i+2]

        type_251 = CodeProgression.is_251(c1, c2, c3)
        if type_251 is None:
            print(f"{c1['root'].name}{c1['harmony']}")
        else:
            print(f"{c1['root'].name}{c1['harmony']}\t({type_251})")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_file')
    args = parser.parse_args()

    with open(args.data_file, 'r') as fp:
        data = json.load(fp)
        main(data)
