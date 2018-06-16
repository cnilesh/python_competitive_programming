def reverse(S, index1, index2):
    if index1 >= index2:
        return S
    S[index1], S[index2] = S[index2], S[index1]
    return reverse(S, index1+1, index2-1)

S=[1,2,3,4,5]
print(reverse(S, 0, len(S)-1))