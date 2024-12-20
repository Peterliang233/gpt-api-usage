import os

from cozepy import Coze, TokenAuth, COZE_CN_BASE_URL

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")), base_url=COZE_CN_BASE_URL)