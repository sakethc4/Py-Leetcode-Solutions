import heapq as hq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for u, v, weight in zip(original, changed, cost):
            graph[u].append((v, weight))
        nodesToDistances = dict()

        def djikstras(start):
            distances = dict()
            pq = []
            hq.heappush(pq, (0, start))
            while pq:
                currDistance, currNode = hq.heappop(pq)
                if currNode in distances:
                    continue
                distances[currNode] = currDistance
                if currNode not in graph:
                    continue
                for neighborNode, weight in graph[currNode]:
                    hq.heappush(pq, (currDistance + weight, neighborNode))
            return distances

        for u in graph:
            distances = djikstras(u)
            nodesToDistances[u] = distances

        res = 0
        for sourceChar, targetChar in zip(source, target):
            if sourceChar == targetChar:
                continue
            if sourceChar not in nodesToDistances or targetChar not in nodesToDistances[sourceChar]:
                return -1
            res += nodesToDistances[sourceChar][targetChar]
        return res
            