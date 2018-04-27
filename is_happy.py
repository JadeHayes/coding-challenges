def is_happy(n):
    # create a set seen, for the sum of the squares we have
    seen = set()
    # while the number we get isn't 1
    while n!=1:
        # n is the sum of the digits squared and added together
        n = sum(int(d)**2 for d in str(n))
        # if n isn't in the seen set, add it.  If it is return False b/c it'll have us in a loop
        if n not in seen:
            seen.add(n)
        else:
            return False
    # if this all passes return true
    return True