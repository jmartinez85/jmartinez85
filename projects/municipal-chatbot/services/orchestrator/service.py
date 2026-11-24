import re


class FAQResponder:
    def __init__(self, entries):
        self.entries = entries

    def answer(self, message):
        words = set(re.findall(r"[a-z]+", message.lower()))
        if words and words <= {"hello", "hi", "there", "hey"}:
            return {"route": "rule", "answer": "Hello! Ask about hours, permits, or recycling."}
        scored = [(len(words.intersection(entry["keywords"])), entry) for entry in self.entries]
        score, best = max(scored, key=lambda pair: pair[0], default=(0, None))
        if score:
            return {"route": "faq", "answer": best["answer"]}
        return {"route": "fallback", "answer": "No matching answer in the demo FAQ."}
