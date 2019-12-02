from sklearn.neighbors import KDTree


def neighbors(pcloud, top=10):
    tree = KDTree(pcloud, leaf_size=40)
    distances, indices = tree.query(pcloud, k=3)
    return indices


def query_radius(pcloud):
    tree = KDTree(pcloud, leaf_size=2)
    return tree.query_radius(pcloud[:1], r=0.3, count_only=True)
