def my_strs(strs):
    # (a) uppercase
    print(strs.upper())
    # (b) even/odd length n
    if len(strs) % 2 == 0:
        print(f"'{strs}' has an even length")
    else:
        print(f"'{strs}' has an odd length")
    # (c) print n characters
    for s in strs:
        print(s)
    # (d) print 'hello' n times
    for i in range(len(strs)):
        print("hello")

my_strs("Good luck!")
