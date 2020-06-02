import unittest
import take_a_walk.traverse as t

class Test(unittest.TestCase):

    def setUp(self):
        self.queue = t.BFSQueue()

    def test_pop_from_empty_BFSQueue(self):
        self.assertIsNone(self.queue.pop())

    def test_add_to_empty_BFSQueue(self):
        node = t.QueueNode('new')
        self.queue.add(node)
        # check tail assignment
        self.assertEqual(self.queue.tail, node)
        # check head assignment
        self.assertEqual(self.queue.head, node)

    def test_pop_from_BFSQueue_with_one_item(self):
        n0 = t.QueueNode('n0')
        self.queue.add(n0)
        popped = self.queue.pop()
        # check popped node
        self.assertEqual(n0, popped)
        # check head and tail are None
        self.assertIsNone(self.queue.tail)
        self.assertIsNone(self.queue.head)

    def test_add_to_BFSQueue_with_one_item(self):
        n0 = t.QueueNode('n0')
        self.queue.add(n0)
        n1 = t.QueueNode('n1')
        self.queue.add(n1)
        # check that n0 is head of queue
        self.assertEqual(self.queue.head, n0)
        # check that n1 is tail of queue
        self.assertEqual(self.queue.tail, n1)

    def test_pop_from_BFSQueue_two_items(self):
        n0 = t.QueueNode('n0')
        self.queue.add(n0)
        n1 = t.QueueNode('n1')
        self.queue.add(n1)
        popped = self.queue.pop()
        # check that correct node was retrieved 
        self.assertEqual(popped, n0)
        # check that both head and tail now point to n1
        self.assertEqual(self.queue.head, n1)
        self.assertEqual(self.queue.tail, n1)

    def test_add_to_BFSQueue_two_items(self):
        n0 = t.QueueNode('n0')
        self.queue.add(n0)
        n1 = t.QueueNode('n1')
        self.queue.add(n1)
        n2 = t.QueueNode('n2')
        self.queue.add(n2)
        # check that head of queue is n0
        self.assertEqual(self.queue.head, n0)
        # check that tail of queue is n2
        self.assertEqual(self.queue.tail, n2)

    def test_pop_from_BFSQueue_n_items(self):
        n0 = t.QueueNode('n0')
        self.queue.add(n0)
        n1 = t.QueueNode('n1')
        self.queue.add(n1)
        n2 = t.QueueNode('n2')
        self.queue.add(n2)
        popped = self.queue.pop()
        # check that n0 was popped
        self.assertEqual(popped, n0)
        #check that head of queue is n1
        self.assertEqual(self.queue.head, n1)
        # check that tail of queue is n2
        self.assertEqual(self.queue.tail, n2)

if __name__ == '__main__':
   unittest.main()