import utils
import sys

search_type = sys.argv[1]
L = list(sys.argv[2])
k = str(sys.argv[3])

if search_type == "linear":
    print(utils.linear_search(L, k))
elif search_type == "binary":
    indexed_list = utils.index_list(L)
    print(utils.binary_search(indexed_list, k))
