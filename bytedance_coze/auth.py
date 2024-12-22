from cozepy import Coze, TokenAuth, COZE_CN_BASE_URL

from config import coze_api_token

coze = Coze(auth=TokenAuth(coze_api_token), base_url=COZE_CN_BASE_URL)