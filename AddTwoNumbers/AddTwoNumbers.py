"""
https://leetcode.com/problems/add-two-numbers/description/
把两个链表当成是相同长度的，短的那个想象成后面都是0；
如果进位的话，在初始化下一个节点的时候将其赋值为1即可;
所以在计算当前节点的值时要加上自己本来的值。
"""
class ListNode(object):
    """
    定义链表节点
    """
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_itself(self):
        """
        Define this to check if it works well
        :return: None
        """
        print(self.val)
        if self.next:
            self.next.print_itself()


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur = result
        while l1 or l2:
            cur.val += add_two_nodes(l1, l2)
            if cur.val >= 10:
                cur.val -= 10
                cur.next = ListNode(1)
            else:
                # Check if there is need to make the next node
                if l1 and l1.next or l2 and l2.next:
                    cur.next = ListNode(0)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result

def add_two_nodes(n1, n2):
    if not n1 and not n2:
        # This cannot happen, ignore it
        None
    if not n1:
        return n2.val
    if not n2:
        return n1.val
    return n1.val + n2.val


if __name__ == "__main__":
    SINGLE_LIST = ListNode(9)
    SINGLE_LIST.next = ListNode(8)
    print(Solution().addTwoNumbers(SINGLE_LIST, ListNode(1)).print_itself())
