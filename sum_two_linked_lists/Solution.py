class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    def sumOneList(l):
      node = l
      i = 0
      total = 0
      while node:
        total += node.val * (10 ** i)
        i += 1
        node = node.next
      return total

    return sumOneList(l1) + sumOneList(l2)

  def constructAndPrintList(self, total):
    _total = total
    power = 1
    firstNode = None
    connectingNode = None
    while _total:

      modulo = int((_total % (10**power)))
      digit = int(modulo/(10**(power-1)))

      _total -= modulo

      l = ListNode(digit)

      if(connectingNode != None):
        connectingNode.next = l
      else:
        firstNode = l

      connectingNode = l
      power += 1

    nextNode = firstNode
    while nextNode:
      print(nextNode.val, end = " ")

      nextNode = nextNode.next






l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

total = Solution().addTwoNumbers(l1, l2)
Solution().constructAndPrintList(total)