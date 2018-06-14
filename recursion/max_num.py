def max_sum(S, start, end, max):
    print(start, end, max)
    if end <= start:
        print('returning max', max)
        return max
    
    if S[start] > S[end] and S[start] >= max:
        max = S[start]
        return max_sum(S, start+1, end-1, max)
    elif S[start] < S[end] and S[end] >= max:
        max = S[end]
        return max_sum(S, start+1, end-1, max)
    else:
        return max_sum(S, start+1, end-1, max)

S = [1,2,37,10,121,4,56,15,5,83]
max_elem = max_sum(S, 0, len(S)-1, 0)
print(max_elem)