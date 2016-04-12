import unittest

class AreEqualTestCase(object):
  """docstring for AreEqualTestCase"""
  def __init__(self, expected, actual):
      super(AreEqualTestCase, self).__init__()
      self.expected = expected
      self.actual = actual

  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertEqual(_outer.expected, _outer.actual)
      return _InnerTestCase('run_test')


class AreNotEqualTestCase(object):
  """docstring for AreNotEqualTestCase"""
  def __init__(self, expected, actual):
      super(AreNotEqualTestCase, self).__init__()
      self.expected = expected
      self.actual = actual

  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertNotEqual(_outer.expected, _outer.actual)
      return _InnerTestCase('run_test')


class AssertTrueTestCase(object):
  """docstring for AssertTrueTestCase"""
  def __init__(self, actual):
      super(AssertTrueTestCase, self).__init__()
      self.actual = actual
      
  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertTrue(_outer.actual)
      return _InnerTestCase('run_test')

class AssertIsTypeTestCase(object):
  """docstring for AssertIsTypeTestCase"""
  def __init__(self, a, b):
      super(AssertIsTypeTestCase, self).__init__()
      self.obj_a = a
      self.type_b = b

  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertIs(type(_outer.obj_a), _outer.type_b)
      return _InnerTestCase('run_test')

class AssertIsNotTypeTestCase(object):
  """docstring for AssertIsNotTypeTestCase"""
  def __init__(self, a, b):
      super(AssertIsNotTypeTestCase, self).__init__()
      self.obj_a = a
      self.type_b = b

  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertIsNot(type(_outer.obj_a), _outer.type_b)
      return _InnerTestCase('run_test')

class AssertIsNoneTestCase(object):
  """docstring for AssertIsNoneTestCase"""
  def __init__(self, a):
      super(AssertIsNoneTestCase, self).__init__()
      self.obj_a = a

  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertIsNone(_outer.obj_a)
      return _InnerTestCase('run_test')

class AssertIsNotNoneTestCase(object):
  """docstring for AssertIsNotNoneTestCase"""
  def __init__(self, a):
      super(AssertIsNotNoneTestCase, self).__init__()
      self.obj_a = a

  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertIsNotNone(_outer.obj_a)
      return _InnerTestCase('run_test')

class AssertIsInTestCase(object):
  """docstring for AssertIsInTestCase"""
  def __init__(self, a, b):
      super(AssertIsInTestCase, self).__init__()
      self.obj_a = a
      self.col_b = b

  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertIn(_outer.obj_a, _outer.col_b)
      return _InnerTestCase('run_test')

class AssertIsNotInTestCase(object):
  """docstring for AssertIsNotInTestCase"""
  def __init__(self, a, b):
      super(AssertIsNotInTestCase, self).__init__()
      self.obj_a = a
      self.col_b = b

  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertNotIn(_outer.obj_a, _outer.col_b)
      return _InnerTestCase('run_test')

class AssertIsInstanceTestCase(object):
  """docstring for AssertIsInstanceTestCase"""
  def __init__(self, a, b):
      super(AssertIsInstanceTestCase, self).__init__()
      self.obj_a = a
      self.type_b = b

  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertIsInstance(_outer.obj_a, _outer.type_b)
      return _InnerTestCase('run_test')

class AssertIsNotInstanceTestCase(object):
  """docstring for AssertIsNotInstanceTestCase"""
  def __init__(self, a, b):
      super(AssertIsNotInstanceTestCase, self).__init__()
      self.obj_a = a
      self.type_b = b

  def testCase(self):
      _outer = self
      class _InnerTestCase(unittest.TestCase):
          def run_test(self):
              self.assertNotIsInstance(_outer.obj_a, _outer.type_b)
      return _InnerTestCase('run_test')


class Test:
  def __init__(self):
      self.testSuite = unittest.TestSuite()

  def assert_equals(self, expected, actual):
      self.testSuite.addTest(AreEqualTestCase(expected, actual).testCase())

  def assert_not_equals(self, expected, actual):
      self.testSuite.addTest(AreNotEqualTestCase(expected, actual).testCase())

  def assert_true(self, actual):
      self.testSuite.addTest(AssertTrueTestCase(actual).testCase())

  def assert_false(self, actual):
      self.testSuite.addTest(AssertTrueTestCase(not actual).testCase())
  
  def assert_is(self, obj_a, type_b):
      """assert obj_a is type_b"""
      self.testSuite.addTest(AssertIsTypeTestCase(obj_a, type_b).testCase())

  def assert_is_not(self, obj_a, type_b):
      """assert obj_a is not type_b"""
      self.testSuite.addTest(AssertIsNotTypeTestCase(obj_a, type_b).testCase())

  def assert_is_none(self, obj_a):
      """assert obj_a is none"""
      self.testSuite.addTest(AssertIsNoneTestCase(obj_a).testCase())

  def assert_is_not_none(self, obj_a):
      """assert obj_a is none"""
      self.testSuite.addTest(AssertIsNotNoneTestCase(obj_a).testCase())

  def assert_in(self, obj_a, collect_b):
      """assert obj_a is in collection b"""
      self.testSuite.addTest(AssertIsInTestCase(obj_a, collect_b).testCase())

  def assert_not_in(self, obj_a, collect_b):
      """assert obj_a is not in collection b"""
      self.testSuite.addTest(AssertIsNotInTestCase(obj_a, collect_b).testCase())

  def assert_is_instance(self, obj_a, type_b):
      """assert obj_a is instance of type b"""
      self.testSuite.addTest(AssertIsInstanceTestCase(obj_a, type_b).testCase())

  def assert_is_not_instance(self, obj_a, type_b):
      """assert obj_a is instance of type b"""
      self.testSuite.addTest(AssertIsNotInstanceTestCase(obj_a, type_b).testCase())

  def run_test(self):
      unittest.TextTestRunner(verbosity=2).run(self.testSuite)


test = Test()
