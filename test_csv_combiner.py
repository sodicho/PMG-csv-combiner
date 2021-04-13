import unittest
from csv-combiner import get_name

class Combiner_Tests(unittest.TestCase):
    
    def setUp(self):
        print("setUp called..")
        self.csv = 'random.csv'
        self.path = '~/Random/things/clear/file/correct.csv'

    def tearDown(self):
        self.csv = ''
        self.path =''
        print("tearDown called..")

    def test_csv(self):
        print('Testing file for CSV')
        self.assertEqual(self.csv[-4:],'.csv', "Not a csv file")
    
    def test_name(self):
        print('Testing name getter')
        self.assertEqual(get_name(self.path), 'correct.csv', "Wrong file name")
        

if __name__ == "__main__":
    unittest.main()
