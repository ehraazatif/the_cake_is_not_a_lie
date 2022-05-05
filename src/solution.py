def solution(s):
    valid = True
    for slice_length in range(1, len(s)):
        if len(s) % slice_length == 0:
            for i in range(0, len(s), slice_length):
                if s[:slice_length] != s[i:i+slice_length]:
                    valid = False
                    break
                
            if valid:
                return len(s)/slice_length
            else:
                valid = True
            
    return 1            