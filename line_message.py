from linebot import LineBotApi
from linebot.models import TextSendMessage

def send_message_to_line(text):
    line_bot_api = LineBotApi('your-channel-access-token')
    user_id = 'your-user-id'
    message = TextSendMessage(text=text)
    line_bot_api.push_message(user_id, message)

# GPTから取得した情報
gpt_info = "This is the information obtained from GPT."

# LINEにメッセージを送信
send_message_to_line(gpt_info)
