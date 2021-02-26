def get_relevant(docs, query):
    if not (docs and query):
        return None
    else:
        li = {}
        for i in docs.keys():
            words = docs[i].split(" ")
            count = 0
            total = 0
            for word in words:
                total += 1
                if word in query:
                    count += 1
            li[i] = count / total

        sort_li = []
        max_num = max(li.values())
        for doc, curr_n in li.items():
            if curr_n == max_num and curr_n != 0:
                sort_li.append(doc)
            else:
                continue
        return sort_li


print(get_relevant({'doc1': 'A cat sat on the mat', 'doc2': 'A cat had a kitten', 'doc3': 'I love ice cream'},
                   ['cat', 'cats', 'kitten']))
print(get_relevant({}, []))
print(get_relevant({'doc1': 'A dog and a cat', 'doc2': 'The dogs and the cats', 'doc3': 'I love ice cream'},
                   ['cat', 'cats', 'dog', 'dogs']))
