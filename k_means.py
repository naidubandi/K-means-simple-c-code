import sys
import random
import bisect


def get_points(stream):
    points = []
    with open(stream, 'r') as fp:
        for line in fp:
            line.strip()
            points.append(map(int, line.split()))
    return points


def farthest_neighbours(space, point, k):
    # space := total points
    # k := total number of farthest neighbours
    # point := which needs the farthest neighbours
    dist = []
    keys = []
    for x in xrange(len(space)):
        d = distance(space[point], space[x])
        tmp = bisect.bisect(dist, d)
        if len(dist) <= k:
            dist.insert(tmp, d)
            keys.insert(tmp, x)
            if len(dist) > k:
                del dist[0]
                del keys[0]
    return keys


def distance(a, b):
    # a and b are vectors
    undroot = 0
    for x in xrange(len(a)):
        undroot += abs(a[x]-b[x])**2
    return undroot**0.5


def nearest_point(points, cluster, avg):
    minimum = distance(points[cluster[0]], avg)
    minIndex = 0
    for x in xrange(1, len(cluster)):
        tmp = distance(points[cluster[x]], avg)
        if minimum > tmp:
            minimum = tmp
            minIndex = x

    return minIndex


def get_centroid(points, cluster):
    avg = [0.0 for x in xrange(len(points[0]))]
    for x in xrange(len(cluster)):
        for y in xrange(len(points[x])):
            avg[y] += points[x][y]
    for x in xrange(len(avg)):
        avg[x] /= len(cluster)
    return nearest_point(points, cluster, avg)


def nearest_centroid(points, centroids, point):
    # return the index of centroid in centroids
    minimum = distance(points[point], points[centroids[0]])
    minIndex = 0
    for x in xrange(1, len(centroids)):
        tmp = distance(points[point], points[centroids[x]])
        if tmp < minimum:
            minimum = tmp
            minIndex = x
    return minIndex


def k_means_clusterize(points, centroids):
    clusters = {}
    print centroids
    for x in xrange(len(centroids)):
        # initiating empty clusters for each centroid
        tmp = centroids[x]
        clusters[tmp] = []

    # main clusterizing happens here
    for x in xrange(len(points)):
        clusters[centroids[nearest_centroid(points, centroids, x)]].append(x)

    # calculating new centroids from the clusters
    for x in xrange(len(centroids)):
        centroids[x] = get_centroid(points, clusters[centroids[x]])
    print clusters


def main():
    # FIXME argv error
    if len(sys.argv) != 2:
        print 'bad number of arguments'
        sys.exit(1)
    points = get_points(sys.argv[1])
    nclusters = int(raw_input(
        'number of cluster ? '
    ))
    assert nclusters <= len(points)
    centroids = [random.randrange(len(points))]
    centroids.extend(farthest_neighbours(points, centroids[0], nclusters-1))
    centroids.sort()
    centroids_db = []
    while True:
        tmp = [centroids[x] for x in xrange(len(centroids))]
        centroids_db.append(tmp)
        k_means_clusterize(points, centroids)
        centroids.sort()
        if centroids in centroids_db:
            break

    clusters = {}
    for x in xrange(len(centroids)):
        # initiating empty clusters for each centroid
        clusters[centroids[x]] = []

    # main clusterizing happens here
    for x in xrange(len(points)):
        clusters[centroids[nearest_centroid(points, centroids, x)]].append(x)

    print clusters


if __name__ == '__main__':
    main()
