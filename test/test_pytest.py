from ali_tongyi.chat_image_understand import CallTongyiImageUnderStandAPI
import pytest
from config import ali_api_key


def test_pytest_CallTongyiAPI():
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"
                },
                {
                    "image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/tiger.png"
                },
                {
                    "image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/rabbit.png"
                },
                {"text": "这些是什么?"},
            ],
        }
    ]
    resp = CallTongyiImageUnderStandAPI(messages)
    print(resp)
