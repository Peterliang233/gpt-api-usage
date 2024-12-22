import json
import types
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import (
    TencentCloudSDKException,
)
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models
from config import tencentcloud_secret_id, tencentcloud_secret_key


def CallHunyuanAPI(messages):
    req = models.ChatCompletionsRequest()
    params = {
        "Model": "hunyuan-lite",  # free
        "Messages": messages,
    }

    # print(params)

    req.from_json_string(json.dumps(params))

    # 返回的resp是一个ChatCompletionsResponse的实例，与请求对象对应
    resp = client.ChatCompletions(req)
    # 输出json格式的字符串回包
    if isinstance(resp, types.GeneratorType):  # 流式响应
        print("不支持流式响应")
    else:  # 非流式响应
        # print(resp)
        return resp.Choices[0].Message


try:
    cred = credential.Credential(tencentcloud_secret_id, tencentcloud_secret_key)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "hunyuan.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = hunyuan_client.HunyuanClient(cred, "ap-beijing", clientProfile)

    messages = []

    while True:
        try:
            user_input = input("咨询人：")
            ask_message = {
                'Role': 'user',
                'Content': user_input,
            }
            messages.append(ask_message)
            # print(messages)
            resp = CallHunyuanAPI(messages)
            resp_message = {
                'Role': 'assistant',
                "Content": resp.Content
            }
            print('混元模型回复：' + resp.Content)
            messages.append(resp_message)
            #print(resp_message)
            if user_input.lower() == "quit":
                print("正在退出对话")
                break
        except KeyboardInterrupt:
            print("\n检测到中断操作，正在退出对话...")
            break
        except:
            print("你输入的内容有些问题，请重试")


except TencentCloudSDKException as err:
    print(err)
