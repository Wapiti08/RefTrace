import unittest
import sys
from pathlib import Path
sys.path.append(Path(sys.path[0]).parent.as_posix())

from src.similarity import similar_score
import asyncio

class TestClass(unittest.TestCase):
    
    def test_url_similarity_score(self,):
        sim_cal_ins = similar_score()
        url1 = "https://chat.openai.com/"
        url2 = "openai.com"
        result = asyncio.run(sim_cal_ins.url_similarity_score(url1, url2))
        expect_result = 0.5
        self.assertEqual(result, expect_result)

    def test_split_url(self,):
        sim_cal_ins = similar_score()
        url = "https://chat.openai.com/"
        result = asyncio.run(sim_cal_ins.split_url(url))
        expect_result = ["https:","chat","openai","com"]
        self.assertCountEqual(result, expect_result)


if __name__ == "__main__":
    unittest.main()
