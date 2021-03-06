import unittest

from trees import BinaryTree, Heap, AVLTree


class BinaryTreeTest(unittest.TestCase):
    def test_init(self):
        tree = BinaryTree(None, None, 4)
        self.assertEqual(tree.value, 4)

    def test_add(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(None, BinaryTree(None,
                                                                 None,
                                                                 5),
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)

        tree = tree.add(11)
        expected_str = "8,4,2,6,5,13,10,11,16,15,18"
        self.assertEqual(str(tree), expected_str)

    def test_remove(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(BinaryTree(None,
                                                           None,
                                                           5),
                                                None,
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)

        expected_tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                              BinaryTree(None, None, 6),
                                              4),
                                   BinaryTree(BinaryTree(None,
                                                         None,
                                                         10),
                                              BinaryTree(
                                                      BinaryTree(None, None,
                                                                 15),
                                                      BinaryTree(None, None,
                                                                 18),
                                                      16),
                                              13),
                                   8)
        self.assertEqual(tree.remove(5), expected_tree)

    def test_str(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(BinaryTree(None,
                                                           None,
                                                           5),
                                                None,
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)

        expected_str = "8,4,2,6,5,13,10,16,15,18"
        self.assertEqual(expected_str, str(tree))

    def test_repr(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(None, BinaryTree(None,
                                                                 None,
                                                                 5),
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)
        self.assertEqual(eval(repr(tree)), tree)

    def test_in(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(BinaryTree(None,
                                                           None,
                                                           5),
                                                None,
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)

        self.assertIn(13, tree)
        self.assertIn(8, tree)
        self.assertIn(16, tree)
        self.assertIn(18, tree)
        self.assertIn(15, tree)
        self.assertIn(10, tree)
        self.assertIn(4, tree)
        self.assertIn(6, tree)
        self.assertIn(5, tree)
        self.assertNotIn(5.5, tree)
        self.assertIn(2, tree)

    def test_iter(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(BinaryTree(None,
                                                           None,
                                                           5),
                                                None,
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)

        expected_list = [8, 4, 2, 6, 5, 13, 10, 16, 15, 18]
        self.assertEqual(list(tree), sorted(expected_list))


class HeapTest(unittest.TestCase):
    def test_empty_init(self):
        h = Heap()
        self.assertEqual(h.comparator, max)
        self.assertEqual(h.array, list())

    def test_normal_init(self):
        h = Heap([1, 2, 3], min)
        self.assertEqual(h.array, [1, 2, 3])
        self.assertEqual(h.comparator, min)

    def test_head(self):
        self.assertEqual(Heap([3, 2, 1]).head(), 3)

    def test_add_smaller_than_maximum(self):
        self.assertEqual(Heap([1], max).add(0).head(), 1)

    def test_add_larger_than_maximum(self):
        self.assertEqual(Heap([1], max).add(2).head(), 2)

    def test_add_equal_to_maximum(self):
        self.assertEqual(Heap([2], max).add(2).head(), 2)

    def test_pop(self):
        self.assertEqual(Heap.make([1, 2, 3, 4, 0]).pop().head(), 3)

    def test_iter(self):
        lst = [432, 431, 543, 3241, 44]

        self.assertEqual(list(Heap.make(lst)), sorted(lst, reverse=True))

    def test_len(self):
        self.assertEqual(len(Heap([1, 2, 3])), 3)

    def test_in(self):
        self.assertIn(5, Heap([6, 2, 1, 5]))

    def test_str(self):
        self.assertEqual(str(Heap([6, 1, 2])), str([6, 1, 2]))

    def test_repr(self):
        h = Heap([6, 3, 2, 1, 1, 1])
        self.assertTrue(eval(repr(h)) == h)

    def test_sift_up_even_pos(self):
        h = Heap([5, 4, 3, 2, 7]).sift_up(4)
        self.assertEqual(h.head(), 7)

    def test_sift_odd_pos(self):
        h = Heap([10, 8, 3, 2, 7, 4]).sift_up(5)
        self.assertEqual(h.array[5], 3)

    def test_make(self):
        self.assertEqual(Heap.make([2, 1, 0, 1, 9, 9, 7]).head(), 9)


class AVLTreeTest(unittest.TestCase):
    def test_init(self):
        avl = AVLTree(0, None, None)
        self.assertEqual(avl.height, 1)

        avl = AVLTree(0, AVLTree(None, None, None), None)
        self.assertEqual(avl.height, 2)

        avl = AVLTree(0, AVLTree(None, None, None), AVLTree(None, None, None))
        self.assertEqual(avl.height, 2)

        avl = AVLTree(None, AVLTree(None, AVLTree(None, None, None), None),
                      AVLTree(None, None, None))
        self.assertEqual(avl.height, 3)

    def test_add(self):
        avl = AVLTree(50, AVLTree(17, None, AVLTree(23,
                                                    None,
                                                    None)),
                      AVLTree(72, None,
                              None))

        avl = avl.add(13).add(-1).add(100).add(200).add(300).add(40).add(39)

        expected_itered = sorted([50, 17, 23, 72, 13, -1, 100, 200, 300, 40,
                                  39], reverse=True)
        actual_itered = list(avl)

        self.assertEqual(actual_itered, expected_itered)

    def test_pop(self):
        avl = AVLTree(50, AVLTree(17, AVLTree(12, None, None), AVLTree(23,
                                                                       None,
                                                                       None)),
                      AVLTree(72, AVLTree(54, None, None),
                              AVLTree(76, None, None)))

        avl = avl.pop(50)

        actual_list = list(avl)
        expected_list = sorted([17, 12, 23, 72, 54, 76], reverse=True)
        self.assertEqual(actual_list, expected_list)

    def test_in(self):
        avl = AVLTree(50, AVLTree(17, AVLTree(12, None, None), AVLTree(23,
                                                                       None,
                                                                       None)),
                      AVLTree(72, AVLTree(54, None, None),
                              AVLTree(76, None, None)))

        self.assertIn(50, avl)
        self.assertIn(17, avl)
        self.assertIn(12, avl)
        self.assertIn(23, avl)
        self.assertIn(72, avl)
        self.assertIn(54, avl)
        self.assertIn(76, avl)

        self.assertNotIn(200, avl)
        self.assertNotIn(0, avl)

    def test_str(self):
        avl = AVLTree(50, AVLTree(17, AVLTree(12, None, None), AVLTree(23,
                                                                       None,
                                                                       None)),
                      AVLTree(72, AVLTree(54, None, None),
                              AVLTree(76, None, None)))

        self.assertEqual(str(avl), "76,72,54,50,23,17,12")

    def test_repr(self):
        avl = AVLTree(50, AVLTree(17, AVLTree(12, None, None), AVLTree(23,
                                                                       None,
                                                                       None)),
                      AVLTree(72, AVLTree(54, None, None),
                              AVLTree(76, None, None)))

        self.assertEqual(eval(repr(avl)), avl)

    def test_iter(self):
        avl = AVLTree(50, AVLTree(17, AVLTree(12, None, None), AVLTree(23,
                                                                       None,
                                                                       None)),
                      AVLTree(72, AVLTree(54, None, None),
                              AVLTree(76, None, None)))

        expected_itered = [76, 72, 54, 50, 23, 17, 12]
        actual_itered = list(avl)

        self.assertEqual(actual_itered, expected_itered)

    def test_cmp(self):
        avl1 = AVLTree(1, None, None)
        avl2 = AVLTree(3, None, None)
        avl3 = AVLTree(3, None, None)
        self.assertGreater(avl2, avl1)
        self.assertTrue(not avl2 > avl3)
        self.assertTrue(not avl2 < avl3)
        self.assertTrue(avl2 == avl3)

    def test_is_balanced(self):
        tree = AVLTree(4, None, None)
        self.assertTrue(tree.is_balanced())

        tree = AVLTree(None, AVLTree(None,
                                     AVLTree(None, None, None), None), None)
        self.assertFalse(tree.is_balanced())

        tree = AVLTree(50, AVLTree(17, AVLTree(12, None, None), AVLTree(23,
                                                                        None,
                                                                        None)),
                       AVLTree(72, AVLTree(54, None, None),
                               AVLTree(76, None, None)))

        self.assertTrue(tree.is_balanced())

    def test_remove_add_balanced(self):
        tree = AVLTree(4, None, None)
        tree.add(1).add(2).add(3).add(4).add(7).add(9).pop(4).pop(9).add(
                20).add(-2).add(21).add(-3).pop(-3)

        self.assertTrue(tree.is_balanced())

    def test_search(self):
        avl = AVLTree(1, None, None).add(2).add(3).add(4).add(5).add(-2).add(10)
        searched_node = avl.search(-2)
        expected_node = AVLTree(-2, None, None)

        self.assertEqual(searched_node, expected_node)
