from html import escape

from pyrogram import Client, filters
from pyrogram.types import Message

from PrimeMega import pbot


@pbot.on_message(filters.command("staff"))
def staff(client: Client, message: Message):
    chat_id = message.chat.id
    chat_title = message.chat.title
    creator = []
    co_founder = []
    admin = []
    admin_check = pbot.get_chat_members(message.chat.id, filter="administrators")
    for x in admin_check:
        if x.status == "administrator" and x.can_promote_members and x.title:
            title = escape(x.title)
            co_founder.append(
                f" <b>├</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a> <i>- {title}</i>"
            )
        elif x.status == "administrator" and x.can_promote_members and not x.title:
            co_founder.append(
                f" <b>├</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a>"
            )
        elif x.status == "administrator" and not x.can_promote_members and x.title:
            title = escape(x.title)
            admin.append(
                f" <b>├</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a> <i>- {title}</i>"
            )
        elif x.status == "administrator" and not x.can_promote_members and not x.title:
            admin.append(
                f" <b>├</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a>"
            )
        elif x.status == "creator" and x.title:
            title = escape(x.title)
            creator.append(
                f" <b>└</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a> <i>- {title}</i>"
            )
        elif x.status == "creator" and not x.title:
            creator.append(
                f" <b>└</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a>"
            )

    if len(co_founder) == 0 and len(admin) == 0:
        result = (
            f"Admins on <b>{chat_title}</b>\n\n🤴 <b>Group Founder</b>\n"
            + "\n".join(creator)
        )

    elif len(co_founder) == 0 and len(admin) > 0:
        res_admin = admin[-1].replace("├", "└")
        admin.pop(-1)
        admin.append(res_admin)
        result = (
            f"Admins on <b>{chat_title}</b>\n\n🤴 <b>Group Founder</b>\n"
            + "\n".join(creator)
            + "\n\n"
            "👮‍♂ <b>Admin</b>\n" + "\n".join(admin)
        )

    elif len(co_founder) > 0 and len(admin) == 0:
        resco_founder = co_founder[-1].replace("├", "└")
        co_founder.pop(-1)
        co_founder.append(resco_founder)
        result = (
            f"Admins on <b>{chat_title}</b>\n\n🤴 <b>Group Founder</b>\n"
            + "\n".join(creator)
            + "\n\n"
            "👨‍✈️ <b>Co-Founder</b>\n" + "\n".join(co_founder)
        )

    else:
        resco_founder = co_founder[-1].replace("├", "└")
        res_admin = admin[-1].replace("├", "└")
        co_founder.pop(-1)
        admin.pop(-1)
        co_founder.append(resco_founder)
        admin.append(res_admin)
        result = (
            f"Admins on <b>{chat_title}</b>\n\n🤴 <b>Group Founder</b>\n"
            + "\n".join(creator)
            + "\n\n"
            "👨‍✈️ <b>Co-Founder</b>\n" + "\n".join(co_founder) + "\n\n"
            "👮‍♂ <b>Admin</b>\n" + "\n".join(admin)
        )
    client.send_message(chat_id, result)
