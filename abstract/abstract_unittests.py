from abstract import Queue, Stack, List, Dictionary, Set

import unittest


class QueueTest(unittest.TestCase):
    def test_different_inits_equal(self):
        q1 = Queue(1, 2)
        q2 = Queue().enqueue(1).enqueue(2)

        self.assertEqual(q1, q2)

    def test_init_empty(self):
        queue = Queue()
        self.assertEqual(len(queue), 0)

    def test_init_lot_of_numbers(self):
        queue = Queue(1, 2, 3)
        self.assertEqual(len(queue), 3)

    def test_init_queue(self):
        queue = Queue([1, 2, 3])
        self.assertEqual(len(queue), 3)

    def test_enqueue(self):
        queue = Queue(1, 2, 3).enqueue(4)
        self.assertEqual(queue.top(), 1)

    def test_dequeue(self):
        queue = Queue(1, 2, 3).dequeue()
        self.assertEqual(queue.top(), 2)

    def test_top(self):
        queue = Queue(1, 2, 3)
        self.assertEqual(queue.top(), 1)

    def test_count(self):
        queue = Queue(1, 2, 3)
        self.assertEqual(len(queue), 3)


class StackTest(unittest.TestCase):
    def test_count(self):
        self.assertEqual(len(Stack(1, 2, 3, 4)), 4)

    def test_head(self):
        self.assertEqual(Stack(1, 2, 3, 4).head(), 1)

    def test_push(self):
        self.assertEqual(Stack(1, 2, 3).push(0).head(), 0)

    def test_pop(self):
        self.assertEqual(Stack(1, 2, 3).pop().head(), 2)

    def test_init_empty(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)

    def test_init_lot_of_numbers(self):
        stack = Stack(1, 2, 3)
        self.assertEqual(len(stack), 3)

    def test_init_list(self):
        stack = Stack([1, 2, 3])
        self.assertEqual(len(stack), 3)


class ListTest(unittest.TestCase):
    def test_init_empty(self):
        l = List()
        self.assertEqual(len(l), 0)

    def test_init_lot_of_numbers(self):
        l = List(1, 2, 3)
        self.assertEqual(len(l), 3)

    def test_init_list(self):
        l = List([1, 2, 3])
        self.assertEqual(len(l), 3)

    def test_append(self):
        list1 = List().append(1).append(2)

        list2 = List(1, 2)
        self.assertEqual(list1, list2)

    def test_count(self):
        list1 = List(1, 2, 1, 4)
        self.assertEqual(list1.count(1), 2)

    def test_index(self):
        list1 = List(1, 2, 1, 4)
        self.assertEqual(list1.index(2), 1)

    def test_insert(self):
        list1 = List(1, 2, 3)
        expected_list = List(1, 7, 2, 3)
        actual_list = list1.insert(1, 7)

        self.assertEqual(expected_list, actual_list)

    def test_pop(self):
        list1 = List(1, 2, 3)
        expected_list = List(1, 3)
        actual_list = list1.pop(1)

        self.assertEqual(expected_list, actual_list)

    def test_pop_empty(self):
        list1 = List(1, 2, 3)
        expected_list = List(2, 3)
        actual_list = list1.pop()

        self.assertEqual(expected_list, actual_list)

    def test_remove(self):
        actual_list = List(1, 2, 3, 2, 2).remove(2)
        expected_list = List(1, 3)

        self.assertEqual(actual_list, expected_list)

    def test_extend(self):
        actual_list = List(1, 2).extend([1, 2])
        self.assertEqual(actual_list, List(1, 2, 1, 2))

    def test_reverse(self):
        self.assertEqual(List(1, 2, 3).reverse(), List(3, 2, 1))

    def test_sort(self):
        self.assertEqual(List(1, 2, 3, 0).sort(), List(0, 1, 2, 3))

    def test_iter(self):
        self.assertEqual(list(iter(List(1, 2, 3))), list(iter([1, 2, 3])))

    def test_add(self):
        self.assertEqual(List(1, 2) + List(3), List(1, 2, 3))

    def test_mul(self):
        self.assertEqual(List(1, 2) * 2, List(1, 2, 1, 2))

    def test_in(self):
        self.assertTrue(1 in List(2, 1, 2))

    def test_get_item(self):
        self.assertEqual(List(2, 1, 3)[2], 3)

    def test_len(self):
        self.assertEqual(len(List(2, 1, 3)), 3)

    def test_str(self):
        self.assertEqual(str(List(2, 1, 3)), str([2, 1, 3]))

    def test_iter_identity_with_dict(self):
        a = List((4, 4), (5, 5))
        self.assertEqual(dict(list(a)), {4: 4, 5: 5})


class DictionaryTest(unittest.TestCase):
    def test_init_empty(self):
        self.assertEqual(Dictionary(), Dictionary())
        self.assertEqual(Dictionary()._dict, dict())

    def test_init_dictionary(self):
        self.assertEqual(Dictionary({1: 2, 3: 4}), Dictionary({1: 2, 3: 4}))
        self.assertEqual(Dictionary({1: 2, 3: 4})._dict, {1: 2, 3: 4})

    def test_init_kvp_list(self):
        list1 = [(1, 2), (3, 4)]
        list2 = ((1, 2), (3, 4))
        list3 = List((1, 2), (3, 4))

        expected_dict = {1: 2, 3: 4}

        self.assertEqual(Dictionary(list1)._dict, expected_dict)
        self.assertEqual(Dictionary(list2)._dict, expected_dict)
        self.assertEqual(Dictionary(list3)._dict, expected_dict)

    def test_clear(self):
        self.assertEqual(Dictionary({1: 2}).clear(), Dictionary())

    def test_copy(self):
        dic = Dictionary({1: 2, 3: 4, 5: {6: 7}})
        self.assertEqual(dic, dic.copy())

    def test_fromkeys_values(self):
        actual_dict = Dictionary.fromkeys([1, 2], 0)
        expected_dict = Dictionary({1: 0, 2: 0})
        self.assertEqual(actual_dict, expected_dict)

    def test_fromkeys_no_values(self):
        self.assertEqual(Dictionary.fromkeys([1]), Dictionary({1: None}))

    def test_get_has(self):
        self.assertEqual(Dictionary({1: 2}).get(1), 2)

    def test_get_hasnt(self):
        self.assertEqual(Dictionary({1: 2}).get(3, 0), 0)

    def test_has_key(self):
        self.assertTrue(Dictionary({1: 2, 3: 4}).has_key(3))

    def test_items(self):
        self.assertEqual(Dictionary({1: 2, 3: 4}).items(), [(1, 2), (3, 4)])

    def test_itervalues(self):
        self.assertEqual(list(Dictionary({1: 2, 2: 1}).itervalues()), [2, 1])

    def test_iteritems(self):
                self.assertEqual(list(Dictionary({1: 2, 3: 4}).iteritems()),
                                 [(1, 2), (3, 4)])

    def test_iterkeys(self):
        self.assertEqual(list(Dictionary({1: 2, 2: 1}).iterkeys()), [1, 2])

    def test_tolist(self):
        self.assertEqual(Dictionary({1: 2, 3: 4}).to_list(),
                         [(1, 2), (3, 4)])

    def test_iter(self):
        self.assertEqual(list(iter(Dictionary({1: 2, 3: 4}))), [1, 3])

    def test_len(self):
        self.assertEqual(len(Dictionary({1: 2, 3: 4})), 2)

    def test_get_item(self):
        self.assertEqual(Dictionary({1: 2})[1], 2)

    def test_in(self):
        self.assertTrue(2 in Dictionary({2: 3, 1: 4}))

    def test_plus_dictionary(self):
        dic1 = Dictionary({1: 2})
        dic2 = Dictionary({3: 4})
        expected = Dictionary({1: 2, 3: 4})
        actual = dic1 + dic2

        self.assertEqual(expected, actual)

    def test_plus_dict(self):
        dic1 = Dictionary({1: 2})
        dic2 = {3: 4}
        expected = Dictionary({1: 2, 3: 4})
        actual = dic1 + dic2

        self.assertEqual(expected, actual)

    def test_str(self):
        dic = Dictionary({1: 2, 3: 4})
        self.assertEqual(str(dic), str({1: 2, 3: 4}))

    def test_append(self):
        self.assertEqual(Dictionary().append(1, 2), Dictionary({1: 2}))

    def test_update_dict(self):
        self.assertEqual(Dictionary().update({1: 2}), Dictionary({1: 2}))

    def test_update_dictionary(self):
        self.assertEqual(Dictionary().update(Dictionary({1: 2})),
                         Dictionary({1: 2}))

    def test_set_default_has(self):
        self.assertEqual(Dictionary({1: 2}).setdefault(1, 3),
                         Dictionary({1: 2}))

    def test_set_default_hasnt(self):
        self.assertEqual(Dictionary({1: 2}).setdefault(2, 3),
                         Dictionary({1: 2, 2: 3}))

    def test_pop(self):
        self.assertEqual(Dictionary({1: 2}).pop(1), Dictionary())


class SetTest(unittest.TestCase):
    def test_init_empty(self):
        s = Set()
        self.assertEqual(len(s), 0)

    def test_init_lot_of_numbers(self):
        s = Set(1, 2, 3)
        self.assertEqual(len(s), 3)

    def test_init_s(self):
        s = Set([1, 2, 3])
        self.assertEqual(len(s), 3)

    def test_add(self):
        set1 = Set().add(1).add(2)

        set2 = Set(1, 2)
        self.assertEqual(set1, set2)

    def test_count(self):
        s1 = Set(1, 2, 1, 4)
        self.assertEqual(s1.count(1), 1)

    def test_pop(self):
        s1 = Set(1, 2, 3)
        expected_s = Set(2, 3)
        actual_s = s1.pop()

        self.assertEqual(expected_s, actual_s)

    def test_pop_empty(self):
        s1 = Set(1, 2, 3)
        expected_s = Set(2, 3)
        actual_s = s1.pop()

        self.assertEqual(expected_s, actual_s)

    def test_remove(self):
        actual_s = Set(1, 2, 3, 2, 2).remove(3)
        expected_s = Set(1, 2)

        self.assertEqual(actual_s, expected_s)

    def test_update(self):
        actual_s = Set(1, 2).update([1, 2])
        self.assertEqual(actual_s, Set(1, 2, 1, 2))

    def test_iter(self):
        self.assertEqual(list(iter(Set(1, 2, 3))), list(iter([1, 2, 3])))

    def test_plus(self):
        self.assertEqual(Set(1, 2) + Set(3), Set(1, 2, 3))

    def test_in(self):
        self.assertTrue(1 in Set(2, 1, 2))

    def test_get_item(self):
        self.assertEqual(Set(2, 1, 3)[2], 3)

    def test_len(self):
        self.assertEqual(len(Set(2, 1, 3)), 3)

    def test_str(self):
        self.assertEqual(str(Set(2, 1, 3)), str([1, 2, 3]))

    def test_append_set(self):
        self.assertEqual(Set(1, 2).add(1), Set(1, 2))

    def test_update_set(self):
        self.assertEqual(Set(1, 2).update(Set(1, 2)), Set(1, 2))

    def test_plus_set(self):
        self.assertEqual(Set(1, 2) + Set(2, 3), Set(1, 2, 3))

    def test_xor(self):
        self.assertEqual(Set(1, 2, 3) ^ (1, 2, 0), Set(0, 3))

    def test_or(self):
        self.assertEqual(Set(1, 2, 3) | (1, 2, 0), Set(0, 1, 2, 3))

    def test_and(self):
        self.assertEqual(Set(1, 2, 3) & (1, 2, 0), Set(1, 2))

    def test_minus(self):
        self.assertEqual(Set(1, 2, 3) - (1, 2, 0), Set(3))
