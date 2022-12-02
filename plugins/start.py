from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	Hello 👋 {message.from_user.first_name }
	
☞ 𝐈'𝐦 𝐀 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐅𝐢𝐥𝐞 & 𝐕𝐢𝐝𝐞𝐨 𝐑𝐞𝐧𝐚𝐦𝐞 𝐁𝐨𝐭 𝐖𝐢𝐭𝐡 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐮𝐩𝐩𝐨𝐫𝐭.

☞ 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐀𝐧𝐲 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐅𝐢𝐥𝐞/𝐕𝐢𝐝𝐞𝐨! 

☞ 𝐒𝐞𝐧𝐝 𝐀 𝐏𝐡𝐨𝐭𝐨 𝐓𝐨 𝐒𝐚𝐯𝐞 𝐀𝐬 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥!

☞ 𝐒𝐞𝐥𝐞𝐜𝐭 𝐘𝐨𝐮𝐫 𝐃𝐞𝐬𝐢𝐫𝐞𝐝/𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐎𝐩𝐭𝐢𝐨𝐧! 

☞ 𝐓𝐡𝐞𝐧 𝐖𝐚𝐢𝐭 𝐓𝐢𝐥𝐥 𝐓𝐡𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐆𝐞𝐭 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝!

☞ Maintained By : @Prv_35
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("Prv Projects" ,url="https://t.me/Prv_35") ]  ]))


@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__𝘞𝘩𝘢𝘵 𝘋𝘰 𝘠𝘰𝘶 𝘞𝘢𝘯𝘵 𝘔𝘦 𝘛𝘰 𝘋𝘰 𝘞𝘪𝘵𝘩 𝘛𝘩𝘪𝘴 𝘍𝘪𝘭𝘦?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Rename 📝",callback_data = "rename")
       ,InlineKeyboardButton("Cancel ❌",callback_data = "cancel")  ]]))
