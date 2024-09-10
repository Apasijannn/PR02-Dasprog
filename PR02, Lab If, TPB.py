N = int(input().strip())

2<=N<=1000

if N <= 0 or N <= 1:
    print("IT IS NOT A PRIME")
elif N == 2:
    print("IT IS A PRIME")
else:
    prime = True
    for i in range(2, N):
        if N % i == 0:
            prime = False
            break
    if prime:
        print("IT IS A PRIME")
    else:
        print("IT IS NOT A PRIME")
