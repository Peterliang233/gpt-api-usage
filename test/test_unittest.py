from ali_tongyi.chat_image_understand import CallTongyiImageUnderStandAPI
import unittest
from config import ali_api_key

class Test_unittest_TongyiAPI(unittest.TestCase):
    def test_call_image_understand_api(self):
        messages = [
            {
                "role": "user",
                "content": [
                    {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"},
                    {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/tiger.png"},
                    {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/rabbit.png"},
                    {"text": "这些是什么?"}
                ]
            }
        ]
        resp = CallTongyiImageUnderStandAPI(messages)
        print(resp)

if __name__ == '__main__':
    unittest.main()