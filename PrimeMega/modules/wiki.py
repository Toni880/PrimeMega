import re

import wikipedia
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest

from PrimeMega import dispatcher
from PrimeMega.modules.disable import DisableAbleCommandHandler
from PrimeMega.modules.helper_funcs.alternate import typing_action


@typing_action
def wiki(update, context):
    Shinano = re.split(pattern="wiki", string=update.effective_message.text)
    wikipedia.set_lang("en")
    if len(str(Shinano[1])) == 0:
        update.effective_message.reply_text(
            "Enter the keywords for searching to wikipedia!"
        )
    else:
        try:
            Natsunagi = update.effective_message.reply_text(
                "Searching the keywords from wikipedia..."
            )
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="More Information",
                            url=wikipedia.page(Shinano).url,
                        )
                    ]
                ]
            )
            context.bot.editMessageText(
                chat_id=update.effective_chat.id,
                message_id=Natsunagi.message_id,
                text=wikipedia.summary(Shinano, sentences=10),
                reply_markup=keyboard,
            )
        except wikipedia.PageError as e:
            update.effective_message.reply_text(f"⚠ Error Detected: {e}")
        except BadRequest as et:
            update.effective_message.reply_text(f"⚠ Error Detected: {et}")
        except wikipedia.exceptions.DisambiguationError as eet:
            update.effective_message.reply_text(
                f"⚠ Error Detected\n\nThere are too many query! Express it more!\n\nPossible query result:\n\n{eet}"
            )


WIKI_HANDLER = DisableAbleCommandHandler("wiki", wiki, run_async=True)
dispatcher.add_handler(WIKI_HANDLER)
