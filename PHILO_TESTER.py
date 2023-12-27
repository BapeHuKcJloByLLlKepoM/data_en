
import json
import os
import random

base_name = "PHILO_BASE"

def write_data_to_json(data, filename):
    ext_dir = os.path.dirname(os.path.abspath(filename))
    if not os.path.exists(ext_dir):
        os.mkdir(ext_dir)

    with open(filename, mode='w', encoding="utf-8") as f_json:
        json.dump(data, f_json, default=str, ensure_ascii=False)

def parse_base(filename):
    with open(filename, mode='r') as f:
        lines = f.readlines()

        lines = ' '.join(lines)

        i = 0
        base = []

        for l in lines.split('@'):
            t = l.strip().replace('\xa0', ' ').split('=')
            d = {}

            d['q'] = t[0]
            if len(t) > 1:
                d['a'] = t[1:]

            base.append(d)

    return base

def get_json_base(filename):
    with open(filename, mode='r') as f:
        base = json.load(f)

    return base

def lets_test(base):

    random.shuffle(base)

    qlen = len(base)
    for i, q in enumerate(base):
        print(f" Q #{i} from {qlen} ============\n {q['q']} \n ============")
        t = input()
        print(f" ANSWER: ====== \n {q['a']} \n ============")
        t = input()


if __name__ == "__main__":
    base = parse_base(base_name)
    write_data_to_json(base, "BASE.json")

    base = get_json_base("BASE.json")
    lets_test(base)

    
