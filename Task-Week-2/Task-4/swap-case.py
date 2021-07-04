def swap_case(s):
    a=''.join([i.lower() if i.isupper() else i.upper() for i in s])
    return a