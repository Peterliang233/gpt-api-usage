from dashscope import MultiModalConversation
import dashscope
from config import ali_api_key

def CallTongyiImageUnderStandAPI(messages):
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"
                },
                {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/tiger.png"},
                {
                    "image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/rabbit.png"
                },
                {"text": "这些是什么?"},
            ],
        }
    ]
    response = dashscope.MultiModalConversation.call(
        api_key=ali_api_key,
        model='qwen-vl-max',
        messages=messages
    )
    return response

def CallTongyiLocalImageUnderStandAPI():
    image_path = f"file://images/local_image1.png"
    messages = [
        {
            "role": "user",
            "content": [
                {
                    'image': image_path
                },
                {
                    'text': '描述一下这个图片'
                }
            ],
        }
    ]
    response = MultiModalConversation.call(
        api_key=ali_api_key,
        model='qwen-vl-max-latest', 
        messages=messages
    )
    print(response["output"]["choices"][0]["message"].content[0]["text"])



if __name__ == '__main__':
    print(CallTongyiLocalImageUnderStandAPI())
    