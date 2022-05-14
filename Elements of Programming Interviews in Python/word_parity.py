# The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. For
# example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect
# single bit errors in data storage and communication. It is fairly straightforward to write code that
# computes the parity of a single 64-bit word.

# How would you compute the parity of a very large number of 64-bit words?

def parity(x):
    result = 0
    while x > 0:
        result ^= x & 1
        x >>= 1
    return result

print(parity(0b100101))
print(parity(0b10001))

def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1