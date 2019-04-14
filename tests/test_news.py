import unittest
from app.models import Sources, Articles


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(
            'CNN', 'CNN News', 'Cable News Newtork that is a leader in providing news worldwide', 'cnn.com', 'general', 'U.S.A', 'en')

 