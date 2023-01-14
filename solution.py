def find_pairs(synonyms):
    pairs = []
    processed = set()
    for i in synonyms:
        for k, v in i.items():
            if k not in processed:
                pair = [k, v]
                processed.add(k)
                processed.add(v)
                for j in synonyms:
                    for l, m in j.items():
                        if l in pair or m in pair:
                            pair += [l, m]
                            processed.add(l)
                            processed.add(m)
                pairs.append(list(set(pair)))
    return pairs

synonyms = [ {"Dg set": "Diesel generator"}, {"Organization": "Organisation"}, {"Group": "Organization"}, {"Orange": "Kinnu"}, {"Orange": "narangi"} ]
print(find_pairs(synonyms))
