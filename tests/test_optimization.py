import timeit
from unittest import TestCase

from aeb_parser import parse_string


class ParseTimingTest(TestCase):

    def test_parse_timing(self):
        test_sent = 'ومن وقتاش رجعت تحكي معاه المدير؟'
        start_time = timeit.default_timer()
        parse_string(test_sent)
        print('Runtime: ',timeit.default_timer() - start_time)
        return
