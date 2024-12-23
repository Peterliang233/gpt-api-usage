from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis
from config import ali_api_key

prompt = "帮我生成一个小狗和主人在小溪边快乐奔跑的图片"


print('----sync call, please wait a moment----')
rsp = ImageSynthesis.call(api_key=ali_api_key,
                          model=ImageSynthesis.Models.wanx_v1,
                          prompt=prompt,
                          n=1,
                          style='<watercolor>',
                          size='1024*1024')
print('response: %s' % rsp)
if rsp.status_code == HTTPStatus.OK:
    # 在当前目录下保存图片
    for result in rsp.output.results:
        file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
        with open('./%s' % file_name, 'wb+') as f:
            f.write(requests.get(result.url).content)
else:
    print('sync_call Failed, status_code: %s, code: %s, message: %s' %
          (rsp.status_code, rsp.code, rsp.message))