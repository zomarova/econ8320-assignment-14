import unittest
import json
import pandas
import re


with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            test_code = "".join(i['source'])


# todo: replace this with an actual test
class TestCase(unittest.TestCase):

    def test_sTime(self):
        self.assertTrue(bool(re.search(r"sTime(.*\n)*.*timeit.Timer.*((1000).*(100)|(100).*(1000))", test_code)), "You need to run your code to calculate 'sTime!'")
