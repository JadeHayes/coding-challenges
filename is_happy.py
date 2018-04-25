def is_happy(n):
    seen = set()
    while n!=1:
        n = sum(int(d)**2 for d in str(n))
        if n not in seen:
            seen.add(n)
        else:
            return False
    return True