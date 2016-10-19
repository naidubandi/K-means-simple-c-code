
import sys
import bisect


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


def get_points(stream):
    points = []
    with open(stream, 'r') as fp:
        for line in fp:
            line.strip()
            points.append(map(int, line.split()))
    return points


def distance(a, b):
    # a and b are vectors
    undroot = 0
    for x in xrange(len(a)):
        undroot += abs(a[x]-b[x])**2
    return undroot**0.5


def smalldx(points, x):
    dist_sum = 0.0
    for i in xrange(len(points)):
        dist_sum += distance(x, points[i])
    return dist_sum/(len(points)-1)


def capDx(points, x):
    dist_sum = 0.0
    length = len(points)
    for i in xrange(length):
        if points[i] != x:
            for j in xrange(i+1, length):
                if points[j] != x:
                    dist_sum += distance(points[i], points[j])
    return dist_sum/((length-1)*(length-2))


def main():
    points = get_points(sys.argv[1])
    kneighbours = int(raw_input("number of neighbours(k)? "))
    assert kneighbours > 2
    deviations = []
    for x in xrange(len(points)):
        tmp_neighb = farthest_neighbours(points, x, kneighbours)
        neighbours = [points[y] for y in xrange(len(tmp_neighb))]
        xdev = smalldx(neighbours, points[x])
        xdev /= capDx(neighbours, points[x])
        deviations.append(xdev)
    print deviations


if __name__ == '__main__':
    main()
