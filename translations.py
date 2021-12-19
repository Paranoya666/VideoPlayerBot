from config import ASSISTANT_NAME
from helpers.bot_utils import BOT_NAME, USERNAME


START_TEXT = f"👋🏻 **Salam**, \n\n bu **{BOT_NAME}** \👋🏻 

Bu video pleyer botu

Mən Telegram Qruplarının Səsli Çatında Canlıları, Radioları, YouTube Videolarını və Telegram Audio/Video Fayllarını yayımlaya bilərəm. Gəlin Qrup Video Pleyerinin Sinematik Görünüşündən həzz alın

@Mr_KABUS_13  tərəfindən ❤️ ilə hazırlanmışdır! 👑
HELP_TEXT = f"""
🛠-- **Setting Up Bot**:--

\u2022 Start Voice Chat In Your Group!
\u2022 Add Me (@{USERNAME}) & My Assistant (@{ASSISTANT_NAME}) To Your Group!
\u2022 Give Admin To Me (@{USERNAME}) & My Assistant (@{ASSISTANT_NAME}) In Your Group!

⚔️-- **Available Commands**:--

\u2022 `/play` - Stream An Audio
\u2022 `/stream` - Stream An Video
\u2022 `/pause` - Pause Current Stream
\u2022 `/resume` - Resume Paused Stream
\u2022 `/endstream` - End Stream & Left VC
\u2022 `/restart` - Restart Bot (Sudo Only)
"""
ABOUT_TEXT = f"💡-- **Information**:-- \n\nThis bot is created for streaming videos in telegram group video chats using several methods from WebRTC. Powered by pytgcalls the async client API for the Telegram Group Calls and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots. \n\n**This bot licensed under GNU-GPL 3.0 License!**"
