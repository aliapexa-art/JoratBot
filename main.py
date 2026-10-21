import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# گرفتن توکن از تنظیمات Render (امنیت بالا)
TOKEN = os.getenv("BOT_TOKEN", "TOKEN_HERE")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ساخت منوی اصلی دقیقاً مثل عکسی که فرستادی
def get_main_menu():
    builder = InlineKeyboardBuilder()
    
    # ردیف اول
    builder.row(
        InlineKeyboardButton(text="🔄 بازی با ناشناس", callback_data="game_anonymous"),
        InlineKeyboardButton(text="🤖 بازی با دوستان", callback_data="game_friends")
    )
    # ردیف دوم
    builder.row(InlineKeyboardButton(text="💎 دریافت سکه رایگان", callback_data="free_coin"))
    # ردیف سوم
    builder.row(
        InlineKeyboardButton(text="📩 ثبت سوال", callback_data="add_question"),
        InlineKeyboardButton(text="👤 پروفایل", callback_data="profile")
    )
    # ردیف چهارم
    builder.row(InlineKeyboardButton(text="🛒 خرید سکه", callback_data="buy_coin"))
    # ردیف پنجم (تبلیغات)
    builder.row(InlineKeyboardButton(text="🤖 هوش مصنوعی فراهوش · چت و ساخت عکس رایگان", url="https://t.me/farahooshrobot"))
    
    return builder.as_markup()

# دستور شروع /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    text = (
        "• اگه میخوای بازی رو شروع کنی روی دکمه 'بازی با ناشناس' و یا 'بازی با دوستان' بزن 🤫✊\n"
        "راستی اگه سوالی به ذهنت رسید و خواستی اضافه کنی میتونی از دکمه ثبت سوال استفاده کنی 😍✌️\n\n"
        "~~~~~~~\n"
        "🤖 چت با هوش مصنوعی و ساخت عکس از متن؛ رایگان\n"
        "@farahooshrobot"
    )
    await message.answer(text, reply_markup=get_main_menu())

# هندل کردن دکمه‌ها (فعلاً فقط یه پیام تستی میده)
@dp.callback_query()
async def handle_callbacks(callback: types.CallbackQuery):
    if callback.data == "game_anonymous":
        # ساخت کیبورد انتخاب جنسیت
        builder = InlineKeyboardBuilder()
        builder.row(
            InlineKeyboardButton(text="👩 دختر", callback_data="gender_girl"),
            InlineKeyboardButton(text="👨 پسر", callback_data="gender_boy")
        )
        await callback.message.answer("جنسیت خودت رو انتخاب کن:", reply_markup=builder.as_markup())
        await callback.answer()
    else:
        await callback.answer("این بخش به زودی فعال می‌شه! 🚀", show_alert=True)

async def main():
    print("✅ ربات با موفقیت روشن شد...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
