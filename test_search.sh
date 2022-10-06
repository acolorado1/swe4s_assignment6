test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run linear_test python3 search.py linear "a" "a"
assert_in_stdout 0
assert_exit_code 0


run binary_test python3 search.py binary "a" "c"
assert_in_stdout -1
