import telebot
from telebot import types
import sqlite3
from datetime import datetime
from pytz import timezone
import time

bot = telebot.TeleBot("5026006801:AAGK0sMjfFpbG8F1D8IeYJ9bz_mNkZJN_S8") # денис
# bot = telebot.TeleBot("1822215840:AAEZ1KFj0Voy0jIlrEbN2018mxNIzvWe4zs") # рома
# bot = telebot.TeleBot("5132422043:AAGzh5vsRnIt2YsUaLCKfVLBySHju5IVQUY") # condonio
db = sqlite3.connect('base.db', check_same_thread=False)

# cursor = db.cursor()
# cursor.execute("DROP TABLE users")
# db.commit()
# cursor.execute("CREATE TABLE IF NOT EXISTS users (userID BIGINT PRIMARY KEY, userName TEXT, userFirstName TEXT, userPage INT)")
# db.commit()
# cursor.execute("DROP TABLE orders")
# db.commit()
# cursor.execute("CREATE TABLE IF NOT EXISTS orders (userID BIGINT, productID INT, amount INT, price INT, statusOrder INT)")
# db.commit()


# cursor.execute(f"SELECT * FROM products")
# print(cursor.fetchall())
# cursor.execute(f"SELECT * FROM orders")
# print(cursor.fetchall())
# cursor.execute(f"SELECT * FROM users")
# print(cursor.fetchall())
# cursor.close()

def error(message):
    user_id = message.from_user.username
    username = message.from_user.username
    firstName = message.from_user.first_name
    print("Зламав бота:", user_id, username, firstName)
    bot.send_message(message.from_user.id,
                     text="Щоб вдало продовжити користування - скористуйтеся командою '/start'")



def media(user_id):
    cursor = db.cursor()
    cursor.execute(f"SELECT userPage FROM users WHERE userID={user_id}")
    userPage = cursor.fetchone()[0]
    cursor.close()

    # media = ["D:\\condonio\\super_sensitive.jpg", "D:\\condonio\\vanish_hyperthin.jpg",
    #      "D:\\condonio\\glowing_pleasures.jpg", "D:\\condonio\\tattoo_touch.jpg",
    #      "D:\\condonio\\extreme_ribs.jpg", "D:\\condonio\\flavor_waves.jpg",
    #      "D:\\condonio\\classic_select.jpg", "D:\\condonio\\super_studs.jpg",
    #      "D:\\condonio\\legend_xl.jpg", "D:\\condonio\\ultrafeel.jpg",
    #      "D:\\condonio\\color_sensation.jpg"
    #      ]

    # media = ["F:\\D\\condonio\\super_sensitive.jpg", "F:\\D\\condonio\\vanish_hyperthin.jpg",
    #          "F:\\D\\condonio\\glowing_pleasures.jpg", "F:\\D\\condonio\\tattoo_touch.jpg",
    #          "F:\\D\\condonio\\extreme_ribs.jpg", "F:\\D\\condonio\\flavor_waves.jpg",
    #          "F:\\D\\condonio\\classic_select.jpg", "F:\\D\\condonio\\super_studs.jpg",
    #          "F:\\D\\condonio\\legend_xl.jpg", "F:\\D\\condonio\\ultrafeel.jpg",
    #          "F:\\D\\condonio\\color_sensation.jpg"
    #          ]

    media = ["super_sensitive.jpg", "vanish_hyperthin.jpg",
             "glowing_pleasures.jpg", "tattoo_touch.jpg",
             "extreme_ribs.jpg", "flavor_waves.jpg",
             "classic_select.jpg", "super_studs.jpg",
             "legend_xl.jpg", "ultrafeel.jpg",
             "color_sensation.jpg"
             ]

    return media[userPage-1]

# for caption
def prices_condoms(num):
    cursor = db.cursor()
    cursor.execute(f"SELECT priceProduct FROM products")
    result = cursor.fetchall()[num][0]
    cursor.close()
    return result

def captions(user_id):
    cursor = db.cursor()
    cursor.execute(f"SELECT userPage FROM users WHERE userID={user_id}")
    userPage = cursor.fetchone()[0]
    cursor.close()
    captions = [
        f'🟠<b>ONE Super Sensitive</b>🟠\n\nПрезервативи класичної форми та стандартного розміру з ультратонкого латексу, з високим вмістом лубриканту на силіконовій основію.\n\n💋Для ніжних та чуттєвих.\n ☘️Для тих, хто цінує природність, але не забуває про безпеку. \n\n 💰Вартість: {prices_condoms(0)} ₴',
        f"🟤<b>ONE Vanish Hyperthing</b>🟤\n\n«Ближче, ніж будь-коли» - ультратонкі латексні презервативи, на 35% тонші за звичайні презервативи.\n\n💨 Виготовлені з м'якшого латексу.\n🌹Забезпечує необхідну чутливість та ніжність.\n\n💰Вартість: {prices_condoms(1)} ₴",
        f'🟣<b>ONE Glowing Pleasure</b>🟣\n\nПрезервативи, що світяться в темряві.\n\n💧Виготовлені з натурального латексу і містять силіконовий лубрикант.\n🌟Для найоригінальніших та незвичайних!\n\n💰Вартість: {prices_condoms(2)} ₴',
        f'🔴<b>ONE Tattoo Touch</b>🔴 \n\n Презервативи з унікальним текстурним малюнком. \n\n 💗Забезпечать додаткове стимулювання та задоволення. \n 💎Виготовлені з ультратонкого натурального латексу і містять силіконовий лубрикант. \n🐚Надійність та міцність забезпечать необхідний захист. \n\n 💰Вартість: {prices_condoms(3)} ₴',
        f'🔵<b>ONE Extreme Ribs</b>🔵\n\nПрезервативи з ребристою текстурою зі змазкою на силіконовій основі.\n\n👩‍❤️‍👨Ще більше насолод.\n🌊Сумісні з лубрикантами на силіконовій та водній основі.\n\n💰Вартість: {prices_condoms(4)} ₴',
        f'🟢<b>ONE Flavor Waves</b>🟢\n\nАроматизовані презервативи класичної форми у стильній упаковці.\n\n 🍌Презервативи мають 6 смаків: “Mint Chocolate”, “Island Punch”, “Fresh Mint”, “Chocolate Strawberry”, “Bubblegum”, “Banana Split”.\n🍓Додасть Вашому життю приємного смаку!\n\n💰Вартість: {prices_condoms(5)} ₴',
        f"🟢<b>ONE Classic Select</b>🟢 \n\n Класичні презервативи–стандартна товщина стінок та форма, гладка текстура. \n \n 💧Містять силіконовий лубрикант. \n 💎Виготовлені з натурального латексу високої якості.\n 👩‍❤️‍👨 Тонкі, м'які та гладкі, забезпечать приємніші відчуття для обох. \n \n 💰 Вартість: {prices_condoms(6)} ₴",
        f'🟣<b>ONE Super Studs</b>🟣\n\nУльтратонкі презервативи з точковим рельєфом.\n\n🔥Сотні унікальних точок на їх поверхні посилюють відчуття на 100%.\n💥Унікальна текстура принесе ще більше задоволення! \n\n 💰Вартість: {prices_condoms(7)} ₴',
        f'⚫️<b>ONE Legend XL</b>⚫️\n\nЛатексні презервативи великого розміру.\n\n♠️Спеціально розроблені таким чином, щоб забезпечити максимальний комфорт для тих, хто цього потребує.\n🦋Мають гладку текстуру та містять силіконовий лубрикант.\n\n 💰Вартість: {prices_condoms(8)} ₴',
        f'🟣<b>ONE UlraFeel</b>🟣\n\nКожна упаковка ONE UltraFeel 2-в-1 містить ультратонкий презерватив та лубрикант на водній основі One Oasis ємністю 2 ml.\n\n💦Містить додатковий лубрикант на водній основі.\n💥Задоволення та комфорт  абсолютно нового рівню.\n\n 💰Вартість: {prices_condoms(9)} ₴',
        f'🔴<b>ONE Color Sensation</b>🔴\n\nКольорові презервативи класичної форми, що містять силіконовий лубрикант.\n\n☘️Виготовлені із натурального високоякісного латексу.\n🎨В наявності 10 кольорів: червоний, оранжевий, жовтий, зелений, смарагдовий, бірюзовий, фіолетовий, чорний та синій.\n🌈Додайте яскравих фарб у Ваше інтимне життя з ONE Color Sensations.\n\n 💰Вартість: {prices_condoms(10)} ₴'
    ]
    return captions[userPage-1]

def captions_bin(zminna):
    captions_bin = [
        '🟠<b>ONE Super Sensitive</b>🟠', '🟤<b>ONE Vanish Hyperthing</b>🟤', '🟣<b>ONE Glowing Pleasure</b>🟣',
        '🔴<b>ONE Tattoo Touch</b>🔴',
        '🔵<b>ONE Extreme Ribs</b>🔵', '🟢<b>ONE Flavor Waves</b>🟢', '🟢<b>ONE Classic Select</b>🟢',
        '🟣<b>ONE Super Studs</b>🟣', '⚫️<b>ONE Legend XL</b>⚫️',
        '🟣<b>ONE UlraFeel</b>🟣', '🔴<b>ONE Color Sensation</b>🔴'
    ]
    return captions_bin[zminna]

def prices(user_id):
    sumaOrder = 0
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM orders WHERE userID={user_id} and statusOrder={1}")
    result = cursor.fetchall()
    cursor.close()
    for i in range(0, len(result)):
        sumaOrder += result[i][3]
    return sumaOrder


def keyboards(user_id):
    cursor = db.cursor()
    cursor.execute(f"SELECT userPage FROM users WHERE userID={user_id}")
    userPage = cursor.fetchone()[0]
    cursor.close()

    try:
        cursor = db.cursor()
        cursor.execute(f"SELECT amount FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
        amount = cursor.fetchone()[0]
        print(amount)
        cursor.close()
    except:
        amount = 0

    keyboard = [
        [
            types.InlineKeyboardButton(text=f'🗑Кошик {prices(user_id)} ₴', callback_data='money_bin'),
            types.InlineKeyboardButton(text=f'🔢 {amount} шт.', callback_data='write_one')
        ],
        [
            types.InlineKeyboardButton(text='-5 шт.', callback_data='minus_five'),
            types.InlineKeyboardButton(text='-1 шт.', callback_data='minus_one'),
            types.InlineKeyboardButton(text='+1 шт.', callback_data='plus_one'),
            types.InlineKeyboardButton(text='+5 шт.', callback_data='plus_five')
        ],
        [
            types.InlineKeyboardButton(text='◀️', callback_data='left'),
            types.InlineKeyboardButton(text=f'{userPage}/11', callback_data="number_of_page"),
            types.InlineKeyboardButton(text='▶️', callback_data='right')]
    ]

    return keyboard


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Асортимент', 'Контакти')
    user_markup.row('Кошик')

    user_id = message.from_user.id
    username = message.from_user.username
    firstName = message.from_user.first_name
    userInfo = [user_id, username, firstName, 1]

    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (userID, userName, userFirstName, userPage) VALUES (?, ?, ?, ?);", userInfo)
        db.commit()
        cursor.close()
    except:
        print("This user already exist")

    print("Зайшов/ла: ", username, user_id, datetime.now(timezone('Europe/Kiev')))

    bot.send_message(message.from_user.id,
                     "👋Привіт! Я Сеньйор Condonio!🍌\n🔒Я зроблю твоє кохання безпечним!🔒\n👇Натискай 'Асортимент' і обирай свій захист!👇",
                     reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def help_info(message):
    contacts(message)

def contacts(message):
    markup = types.InlineKeyboardMarkup()
    insta = types.InlineKeyboardButton(text='Instagram',
                                       url='https://instagram.com/condonio.store?utm_medium=copy_link')
    manager = types.InlineKeyboardButton(text='Менеджер', url='t.me/condonio_store')
    markup.add(insta)
    markup.add(manager)
    bot.send_message(message.chat.id, "Обери варіант зв'язку", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def catalog_info(message):
    #меню асортименту
    if message.text == 'Асортимент':
        #виклик клавіатури
        buttons_keyboard(message)

    elif message.text == 'Кошик':
        user_id = message.from_user.id
        if prices(user_id) == 0:
            bot.send_message(message.from_user.id, text="Корзина пуста")
            time.sleep(1.5)
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        else:
            show_money_bin(message)
    elif message.text == 'Контакти':
            contacts(message)


def buttons_keyboard(message):
    user_id = message.from_user.id
    try:
        img = open(media(user_id), 'rb')
        reply_markup = types.InlineKeyboardMarkup(keyboards(user_id))
        try:
            bot.edit_message_media(media=types.InputMediaPhoto(img), chat_id=message.message.chat.id, message_id=message.message.message_id, reply_markup=reply_markup)
            bot.edit_message_caption(chat_id=message.message.chat.id, message_id=message.message.message_id, caption=captions(user_id), reply_markup=reply_markup,
                         parse_mode='html')
        except:
            bot.send_photo(message.from_user.id, img, caption=captions(user_id), reply_markup=reply_markup,
                       parse_mode='html')
    except:
        error(message)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(message):
    user_id = message.from_user.id

    if message.data == 'right':
        try:
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM users WHERE userID={user_id}")
            one_result = cursor.fetchone()

            if (one_result[3] + 1) == 12:
                cursor.execute(f"UPDATE users SET userPage={1} WHERE userID={user_id}")
            else:
                cursor.execute(f"UPDATE users SET userPage={one_result[3] + 1} WHERE userID={user_id}")
            db.commit()
            cursor.close()

            buttons_keyboard(message)
        except:
            error(message)


    elif message.data == 'left':
        try:
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM users WHERE userID={user_id}")
            one_result = cursor.fetchone()

            if (one_result[3] - 1) == 0:
                cursor.execute(f"UPDATE users SET userPage={11} WHERE userID={user_id}")
            else:
                cursor.execute(f"UPDATE users SET userPage={one_result[3] - 1} WHERE userID={user_id}")
            db.commit()
            cursor.close()

            buttons_keyboard(message)
        except:
            error(message)

    elif message.data == 'plus_one':
        cursor = db.cursor()
        cursor.execute(f"SELECT userPage FROM users WHERE userID={user_id}")
        userPage = cursor.fetchone()[0]

        cursor.execute(f"SELECT * FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
        check_temp = cursor.fetchall()

        if not check_temp:
            orderInfo = [user_id, userPage, 1, 0, 1]
            cursor.execute(f"INSERT INTO orders VALUES(?,?,?,?,?)", orderInfo)
            db.commit()

            cursor.execute(
                f"SELECT orders.productID, amount, priceProduct FROM orders INNER JOIN products ON products.productID = orders.productID WHERE userID={user_id} AND statusOrder={1}")
            zminna = cursor.fetchall()
            try:
                for i in range(0, len(zminna)):
                    amountUser = zminna[i][1] * zminna[i][2]
                    cursor.execute(f"UPDATE orders SET price={amountUser} WHERE userID={user_id} AND productID={userPage}")
                db.commit()
            except db.Error:
                db.rollback()
        else:
            cursor.execute(
                f"SELECT amount FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
            amount = cursor.fetchone()[0]
            cursor.execute(
                f"UPDATE orders SET amount={amount + 1} WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
            db.commit()

            cursor.execute(
                f"SELECT orders.productID, amount, priceProduct FROM orders INNER JOIN products ON products.productID = orders.productID WHERE userID={user_id} AND statusOrder={1}")
            zminna = cursor.fetchall()
            try:
                for i in range(0, len(zminna)):
                    amountUser = zminna[i][1] * zminna[i][2]
                    cursor.execute(f"UPDATE orders SET price={amountUser} WHERE userID={user_id} AND productID={userPage}")
                db.commit()
            except db.Error:
                db.rollback()
        cursor.close()

        buttons_keyboard(message)

    elif message.data == 'minus_one':
        cursor = db.cursor()
        cursor.execute(f"SELECT userPage FROM users WHERE userID={user_id}")
        userPage = cursor.fetchone()[0]

        cursor.execute(f"SELECT * FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
        check_temp = cursor.fetchall()

        if check_temp:
            cursor.execute(
                f"SELECT amount FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
            amount = cursor.fetchone()[0]
            minus = amount - 1
            if minus <= 0:
                cursor.execute(
                    f"DELETE FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1} AND amount={amount}")
            else:
                cursor.execute(
                    f"UPDATE orders SET amount={minus} WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
            db.commit()

        cursor.execute(
            f"SELECT orders.productID, amount, priceProduct FROM orders INNER JOIN products ON products.productID = orders.productID WHERE userID={user_id} AND statusOrder={1}")
        zminna = cursor.fetchall()
        try:
            for i in range(0, len(zminna)):
                amountUser = zminna[i][1] * zminna[i][2]
                cursor.execute(f"UPDATE orders SET price={amountUser} WHERE userID={user_id} AND productID={userPage}")
            db.commit()
        except db.Error:
            db.rollback()
        cursor.close()

        buttons_keyboard(message)

    elif message.data == 'plus_five':
        cursor = db.cursor()
        cursor.execute(f"SELECT userPage FROM users WHERE userID={user_id}")
        userPage = cursor.fetchone()[0]

        cursor.execute(f"SELECT * FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
        check_temp = cursor.fetchall()

        if not check_temp:
            orderInfo = [user_id, userPage, 5, 0, 1]
            cursor.execute(f"INSERT INTO orders VALUES(?,?,?,?,?)", orderInfo)
            db.commit()

            cursor.execute(
                f"SELECT orders.productID, amount, priceProduct FROM orders INNER JOIN products ON products.productID = orders.productID WHERE userID={user_id} AND statusOrder={1}")
            zminna = cursor.fetchall()
            for i in range(0, len(zminna)):
                amountUser = zminna[i][1] * zminna[i][2]
                cursor.execute(f"UPDATE orders SET price={amountUser} WHERE userID={user_id} AND productID={userPage}")
            db.commit()
        else:
            cursor.execute(
                f"SELECT amount FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
            amount = cursor.fetchone()[0]
            cursor.execute(
                f"UPDATE orders SET amount={amount + 5} WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
            db.commit()

            cursor.execute(
                f"SELECT orders.productID, amount, priceProduct FROM orders INNER JOIN products ON products.productID = orders.productID WHERE userID={user_id} AND statusOrder={1}")
            zminna = cursor.fetchall()
            try:
                for i in range(0, len(zminna)):
                    amountUser = zminna[i][1] * zminna[i][2]
                    cursor.execute(f"UPDATE orders SET price={amountUser} WHERE userID={user_id} AND productID={userPage}")
                db.commit()
            except db.Error:
                db.rollback()
        cursor.close()

        buttons_keyboard(message)

    elif message.data == 'minus_five':
        cursor = db.cursor()
        cursor.execute(f"SELECT userPage FROM users WHERE userID={user_id}")
        userPage = cursor.fetchone()[0]

        cursor.execute(f"SELECT * FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
        check_temp = cursor.fetchall()

        if check_temp:
            cursor.execute(
                f"SELECT amount FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
            amount = cursor.fetchone()[0]
            minus = amount - 5
            if minus <= 0:
                cursor.execute(
                    f"DELETE FROM orders WHERE userID={user_id} AND productID={userPage} AND statusOrder={1} AND amount={amount}")
            else:
                cursor.execute(
                    f"UPDATE orders SET amount={minus} WHERE userID={user_id} AND productID={userPage} AND statusOrder={1}")
            db.commit()

        cursor.execute(
            f"SELECT orders.productID, amount, priceProduct FROM orders INNER JOIN products ON products.productID = orders.productID WHERE userID={user_id} AND statusOrder={1}")
        zminna = cursor.fetchall()
        try:
            for i in range(0, len(zminna)):
                amountUser = zminna[i][1] * zminna[i][2]
                cursor.execute(f"UPDATE orders SET price={amountUser} WHERE userID={user_id} AND productID={userPage}")
            db.commit()
        except db.Error:
            db.rollback()
        cursor.close()

        buttons_keyboard(message)

    elif message.data == 'money_bin':
        user_id = message.from_user.id
        if prices(user_id) == 0:
            bot.send_message(message.from_user.id, text="Корзина пуста")
            time.sleep(1.5)
            bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.message_id + 1)
        else:
            show_money_bin(message)

    elif message.data == 'remove_bin':
        cursor = db.cursor()
        cursor.execute(f"SELECT userPage FROM users WHERE userID={user_id}")
        cursor.execute(
            f"SELECT orders.productID, amount, priceProduct FROM orders INNER JOIN products ON products.productID = orders.productID WHERE userID={user_id} AND statusOrder={1}")
        zminna = cursor.fetchall()

        try:
            for i in range(0, len(zminna)):
                cursor.execute(
                    f"DELETE FROM orders WHERE userID={user_id} AND statusOrder={1}")
            db.commit()
        except db.Error:
            db.rollback()

        cursor.close()
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Корзина пуста")
        time.sleep(1.5)
        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.message_id)

    elif message.data == 'edit_bin':
        time.sleep(0.5)
        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.message_id)

    elif message.data == 'make_the_order':
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name

        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM orders WHERE userID={user_id} AND statusOrder={1}")
        zminna = cursor.fetchall()

        temp = []

        for i in range(0, len(zminna)):
            text = f"{captions_bin(zminna[i][1] - 1)} ( {zminna[i][2]} шт ) = {zminna[i][3]} ₴\n"
            temp.insert(i, text)
        bot.send_message(chat_id=5203341262,
                         text=f"Customer: {first_name, last_name, username}\n\n" + '\n'.join(
                             temp) + f'\nЗагалом: {prices(user_id)} ₴', parse_mode='html')
        try:
            for i in range(0, len(zminna)):
                cursor.execute(f"UPDATE orders SET statusOrder={0} WHERE userID={user_id}")
            db.commit()
        except db.Error:
            db.rollback()
        cursor.close()
        bot.send_message(message.from_user.id, text="Дякую за замовлення! Найближчим часом з Вами зв'яжеться менеджер")


def show_money_bin(message):
    user_id=message.from_user.id
    keyboard_bin = [
        [
            types.InlineKeyboardButton(text=f'✏️Редагувати', callback_data='edit_bin'),
            types.InlineKeyboardButton(text=f'❌Очистити', callback_data='remove_bin')
        ],
        [
            types.InlineKeyboardButton(text=f'✅Оформити замовлення', callback_data='make_the_order')
        ]
    ]
    temp = []

    reply_markup = types.InlineKeyboardMarkup(keyboard_bin)

    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM orders WHERE userID={user_id} AND statusOrder={1}")
    zminna = cursor.fetchall()
    cursor.close()

    for i in range(0, len(zminna)):
        text = f"{captions_bin(zminna[i][1] - 1)} ( {zminna[i][2]} шт ) = {zminna[i][3]} ₴\n"
        temp.insert(i, text)
    bot.send_message(message.from_user.id,
                     text="<b>Кошик</b>\n\n" + '\n'.join(temp) + f'\n<b>Загалом:</b> {prices(user_id)} ₴',
                     reply_markup=reply_markup, parse_mode='html')


bot.polling(none_stop=True)