import os

from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType, ChatEventType, COZE_CN_BASE_URL # noqa

from config import coze_api_token, coze_bot_id


# Get an access_token through personal access token or oauth.
coze_api_token = coze_api_token
# The default access is api.coze.com, but if you need to access api.coze.cn,
# please use base_url to configure the api endpoint to access
coze_api_base = os.getenv("COZE_API_BASE") or COZE_CN_BASE_URL


# Init the Coze client through the access_token.
coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=COZE_CN_BASE_URL)

# Create a bot instance in Coze, copy the last number from the web link as the bot's ID.
bot_id = coze_bot_id
# The user id identifies the identity of a user. Developers can use a custom business ID
# or a random string.
user_id = "user id"

# Call the coze.chat.stream method to create a chat. The create method is a streaming
# chat and will return a Chat Iterator. Developers should iterate the iterator to get
# chat event and handle them.
for event in coze.chat.stream(
    bot_id=bot_id,
    user_id=user_id,
    additional_messages=[
        Message.build_user_question_text("Tell a 500-word story."),
    ],
):
    if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
        print(event.message.content, end="", flush=True)

    if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
        print()
        print("token usage:", event.chat.usage.token_count)