class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = []
        min_block = 0
        l = 0
        window_block = 0
        for r in range(k):
            window.append(blocks[r])
            if blocks[r] == 'W':
                window_block += 1
                min_block = window_block
        
        for r in range(k, len(blocks)):
            if blocks[l] == 'W':
                window_block -= 1
            window.remove(blocks[l])
            l += 1
            window.append(blocks[r])
            if blocks[r] == 'W':
                window_block += 1
            min_block = min(min_block, window_block)
        return min_block


