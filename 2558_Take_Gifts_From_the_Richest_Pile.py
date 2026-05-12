class Solution:
    def pickGifts(self, gifts, k):
        import heapq
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            x = -heapq.heappop(heap)
            heapq.heappush(heap, -int(x ** 0.5))
        return -sum(heap)
