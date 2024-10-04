import ll


def test_Solution2807():
    # 2807m Insert Greatest Common Divisors in Linked List
    from ll import ListNode as L

    def draw(ls):
        s = ""
        while ls:
            if ls.next:
                s += "{" + str(ls.val) + " *}->"
            else:
                s += "{" + str(ls.val) + " /}"
            ls = ls.next
        return s

    ls = L(18, L(6, L(10, L(3))))
    print(draw(ls), " => ", draw(ll.Solution2807().insertGreatestCommonDivisors(ls)))
