This was a problem I encountered when doing the Google Foobar challenge (Level 1). The basis of this problem
is that we have a cake with its edges lined with M&Ms of different colors. Each letter of the alphabet (a-z)
represents a uniquely colored M&M. We have to cut slices of the cake so that everyone gets the same colored
sequence of M&Ms, with no leftover slices of the cake. Also, we want to serve as many people as possible,
so we want to maximize the number of slices we cut.

The solution to the problem is easier than it may seem. The trick is to simply start at a slice/sequence
length of 1, then see if everyone would get the same colored sequence of M&Ms. If not, then we increment
the sequence length. Additionally, for every increment, we make sure that the total length of the given
string is evenly divisbile by the sequence length, to ensure no leftovers. Eventually, by running
through enough sequence lengths, we will find the final answer that ensures no leftovers, that everyone
gets the same sequence of M&Ms, and that we have maximized the number of slices we are going to cut (since
we're starting from the bottom up).
