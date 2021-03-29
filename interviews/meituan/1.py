




def decode(n, s):
    left = 0
    right = n-1
    while s[left] != 'M':
        left = left + 1
    left = left + 1
    while s[left] != 'T':
        left = left + 1
    left = left + 1
    while s[right] != 'T':
        right = right - 1
    right = right - 1
    while s[right] != 'M':
        right = right - 1
    right = right - 1
    decode_s = s[left:right+1]
    return decode_s



import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    # n = 10
    # s = "MMATSATMMT"
    dec_s = decode(n, s)
    print (dec_s)