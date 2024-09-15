import hashing


#  1371m Find the Longest Substring Containing Vowels in Even Counts
def test_Solution1371():
    assert hashing.Solution1371().findTheLongestSubstring('eleetminicoworoep') == 13
    assert hashing.Solution1371().findTheLongestSubstring('leetcodeisgreat') == 5
    assert hashing.Solution1371().findTheLongestSubstring('bcbcbc') == 6
