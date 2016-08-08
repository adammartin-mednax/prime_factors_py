import unittest

from primes.prime_factors import Primes 
import nose.tools as nt

class PrimeTests(unittest.TestCase):
	def setUp(self):
		self.primes = Primes()

	def test_primes_of_1_is_an_empty_list(self):
		self.assertEqual([],self.primes.factors(1))

	def test_primes_of_2_returns_2(self):
		self.assertEqual([2],self.primes.factors(2))

	def test_primes_of_3_returns_3(self):
		self.assertEqual([3],self.primes.factors(3))

	def test_primes_of_4_returns_2_2(self):
		self.assertEqual([2,2],self.primes.factors(4))

	def test_primes_of_6_returns_2_3(self):
		self.assertEqual([2,3],self.primes.factors(6))

	def test_primes_of_8_returns_2_2_2(self):
		self.assertEqual([2,2,2], self.primes.factors(8))

	def test_primes_of_9_returns_3_3(self):
		self.assertEqual([3,3], self.primes.factors(9))

class FlattenTest(unittest.TestCase):
	def test_flatten_for_doublenest_flattens(self):
		self.assertEqual([2], Primes().flatten([[2]]) )

	def test_flatten_for_random_nesting(self):
		self.assertEqual([2,2], Primes().flatten([2,[2]]))