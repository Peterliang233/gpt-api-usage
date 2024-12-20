import os, sys

coze_api_token = os.getenv("COZE_API_TOKEN")

my_bot_id = os.getenv("COZE_BOT_ID")

from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType, ChatEventType, COZE_CN_BASE_URL

coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=COZE_CN_BASE_URL)

bot_id = my_bot_id

user_id = "user id"

print("输入你想提的一个问题：")

user_input = sys.stdin.readline()


for event in coze.chat.stream(
    bot_id=bot_id, user_id=user_id, additional_messages=[Message.build_user_question_text(user_input.strip())]
):
    if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
        message = event.message
        print(f"role={message.role}, content={message.content}")