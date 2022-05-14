def swap_bits(x,i,j):
    # check if bits at position i, j are equal
    if (x >> i) & 1 != (x >> j) & 1:
        # swap if not equal
        mask = (1 << i) | (1 << j)
        x ^= mask
    return x

print(bin(swap_bits(0b01001001, 1, 6)))
