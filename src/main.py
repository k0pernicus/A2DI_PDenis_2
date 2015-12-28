#-*- coding: utf-8 -*-

import numpy as np
import scipy.spatial

query = "die dagger"

def parse_doc(path):
    """
    Lit les documents présent dans un fichier donné.
    """

    lines = []

    with open(path, 'r') as file:
        lines = file.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip().replace(",", "")
        lines[i] = lines[i].strip().replace(":", "")
        lines[i] = lines[i].strip().replace(".", "")
        lines[i] = lines[i].strip().replace(";", "")
        lines[i] = lines[i].strip().replace("?", "")
        lines[i] = lines[i].strip().replace("!", "")

    return lines

def create_doc_matrix(docs_list, query):
    """
    Crée les vecteurs des documents.
    """
    all_words = []

    # Crér la liste de tous les mots
    for doc in docs_list:
        for word in doc.split(" "):
            all_words.append(word)

    all_words = np.unique(all_words).tolist()

    n = len(all_words)
    query_vector = np.zeros(n)
    res = np.zeros([n, len(docs_list)])

    # Crée les vecteurs des documents
    for i, doc in enumerate(docs_list):
        for word in doc.split(" "):
            res[all_words.index(word)][i] += 1

    for word in map(lambda word: word.strip(), query.split(" ")):
        query_vector[all_words.index(word)] += 1

    return query_vector, res

def get_cos_distance(doc, q):
    """
    Donne la distance cosinus entre un document et une requête.
    """

    return np.dot(doc, q) / (np.linalg.norm(doc, 2) * np.linalg.norm(q, 2))

def get_order(docs, q):
    """
    Donne les documents dans l'ordre décroissant de leur distance à la requête.
    """

    res = {}

    for i, doc in enumerate(docs.T):
        res["d" + str(i + 1)] = get_cos_distance(doc, q)

    return map(lambda couple: couple[0], sorted(res.items(), key=lambda couple: couple[1], reverse=True))

def main():
    q, docs = create_doc_matrix(parse_doc("data/documents.txt"), query)

    for doc in docs.T:
        print("cos_distance : {0}".format(get_cos_distance(doc, q)))

if __name__ == '__main__':
    main()
