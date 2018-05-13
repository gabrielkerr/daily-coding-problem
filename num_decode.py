"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

m = {
    1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j',
    11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s',
    20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'
    }

def count_messages(c, i):
    """
    Count the number of possible decodings from index i of
    encoded message c.
    """

    # If encoded message is empty, return 0.
    if len(c[i:]) == 0:
        return 1

    # If encoded message has only 1 number and it is in m, return 1.
    if len(c[i:]) == 1 and int(c[i:]) in m.keys():
        return 1

    if len(c[i:]) == 1 and int(c[i:]) == 0:
        return 0

    # Number of possible decodings
    num_decodings = 0

    if int(c[i]) in m.keys():
        num_decodings += count_messages(c, i+1)

    if int(c[i:i+2]) in m.keys():
        num_decodings += count_messages(c, i+2)

    return num_decodings



if __name__ == '__main__':
    c = 1111 # kk, aaaa, aka, aak, kaa 
    i = 0
    cs = str(c)
    print(count_messages(cs, 0))