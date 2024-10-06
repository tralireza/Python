import strings as m


def test_Solution1813():
    # 1813m Sentence Similarity III
    assert m.Solution1813().areSentencesSimilar("Hello Jane", "Hello my name is Jane") is True
    assert m.Solution1813().areSentencesSimilar("of", "A lot of words") is False
    assert m.Solution1813().areSentencesSimilar("Eating right now", "Eating") is True
