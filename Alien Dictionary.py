from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        # Step 1: Build graph
        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # Invalid: prefix case ("abc" before "ab")
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break
        
        # Step 2: Topological sort using queue
        queue = deque([c for c in indegree if indegree[c] == 0])
        order = []
        
        while queue:
            c = queue.popleft()
            order.append(c)
            for nei in graph[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        # Step 3: Check for cycles
        if len(order) < len(indegree):
            return ""
        
        return "".join(order)
