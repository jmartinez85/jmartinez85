import unittest

from services.orchestrator.service import FAQResponder


class FAQTests(unittest.TestCase):
    def setUp(self):
        self.bot = FAQResponder([{"keywords": ["hours"], "answer": "09:00"}])

    def test_routes_hello(self):
        self.assertEqual(self.bot.answer("Hi!")["route"], "rule")

    def test_routes_matching_faq(self):
        self.assertEqual(self.bot.answer("What are the HOURS?"), {"route": "faq", "answer": "09:00"})

    def test_falls_back(self):
        self.assertEqual(self.bot.answer("What is the weather?")["route"], "fallback")
