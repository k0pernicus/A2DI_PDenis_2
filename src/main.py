#-*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

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

def get_reduced_elements(docs, q, k=2):
    """
    Réduit la matrice des documents.
    """

    U, sigma, V = np.linalg.svd(docs, full_matrices=False)
    U_k = U[:, :k]
    sigma_k = np.fill_diagonal(np.zeros((k, k)), sigma[:k])
    sigma_k = np.diag(sigma[:k])
    V_k = V[:k, :]
    docs_k = np.dot(sigma_k, V_k)
    q_k = np.dot(np.linalg.inv(sigma_k), np.dot(U_k.T, q))

    return (q_k, docs_k)

def plot_2D_data(docs, q):
    """
    Plotte les données réduites.
    """

    colors = ["red", "green", "blue", "grey", "orange"]

    for i, doc in enumerate(docs.T):
        plt.scatter(doc[0], doc[1], color=colors[i], label="d" + str(i + 1))

    plt.scatter(q[0], q[1], color="black", label="query")

    plt.legend(loc=2)
    plt.show()

def main():
    q, docs = create_doc_matrix(parse_doc("data/documents.txt"), query)

    print("===== AVANT LA SVD =====")
    print("\n")
    print("Documents et leurs distance à la requête :")

    for i, doc in enumerate(docs.T):
        print("d" + str(i + 1) + " : {0}".format(get_cos_distance(doc, q)))

    print("\n")
    print("Les documents sont donc dans l'ordre suivant : {0}".format(get_order(docs, q)))
    print("\n")

    q_k, docs_k = get_reduced_elements(docs, q)

    print("===== APRÈS LA SVD =====")
    print("\n")
    print("Documents et leurs distance à la requête :")

    for i, doc in enumerate(docs_k.T):
        print("d" + str(i + 1) + " : {0}".format(get_cos_distance(doc, q_k)))

    print("\n")
    print("Les documents sont donc dans l'ordre suivant : {0}".format(get_order(docs_k, q_k)))
    print("\n")

    plot_2D_data(docs_k, q_k)

if __name__ == '__main__':
    main()
