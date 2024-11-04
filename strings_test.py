import strings as m


def test_Solution1813():
    # 1813m Sentence Similarity III
    assert m.Solution1813().areSentencesSimilar("Hello Jane", "Hello my name is Jane") is True
    assert m.Solution1813().areSentencesSimilar("of", "A lot of words") is False
    assert m.Solution1813().areSentencesSimilar("Eating right now", "Eating") is True


def test_Solution3163():
    # 3163m String Compression III
    assert m.Solution3163().compressedString("abcde") == "1a1b1c1d1e"
    assert m.Solution3163().compressedString("aaaaaaaaaaaaaabb") == "9a5a2b"
