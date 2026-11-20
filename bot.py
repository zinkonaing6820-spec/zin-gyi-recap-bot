
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

MENU = [
    ["🎬 Recap", "🎙️ Dubbing"],
    ["📖 Story", "💬 Subtitle"],
    ["⚙️ Settings", "🌫️ Blur"],
    ["✂️ Crop", "🎞️ Quality"],
    ["🌐 Language", "🔊 Speed"],
    ["🔉 Volume", "🎵 Background"],
    ["📝 Title", "🖼️ Thumbnail Hook"],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 ဇင်ကြီးရဲ့ ရီကပ် မှ ကြိုဆိုပါတယ်။\n\n"
        "Movie Video ပို့နိုင်ပါတယ်။ အောက်က Menu ကို ရွေးချယ်ပါ။",
        reply_markup=ReplyKeyboardMarkup(
            MENU, resize_keyboard=True
        )
    )

async def mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ရွေးချယ်ပါ:\n"
        "/recap - Movie Recap\n"
        "/dubbing - AI Dubbing\n"
        "/story - Story\n"
        "/subtitle - Subtitle"
    )

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚙️ Video Settings\n"
        "/quality - Video Quality\n"
        "/lang - Language\n"
        "/speed - Voice Speed\n"
        "/vol - Voice Volume"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 ဇင်ကြီးရဲ့ ရီကပ်\n"
        "Movie Recap Bot\n\n"
        "အသုံးပြုရန် /start ကိုနှိပ်ပါ။"
    )

async def video_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Video လက်ခံရရှိပါပြီ။\n"
        "AI Processing စနစ်ကို မချိတ်ဆက်ရသေးပါ။"
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(
        f"ရွေးချယ်ထားသည်: {text}\n"
        "ဒီ Feature ကို နောက်အဆင့်မှာ ချိတ်ဆက်ပါမယ်။"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("mode", mode))
    app.add_handler(CommandHandler("settings", settings))

    for command in [
        "recap", "dubbing", "story", "subtitle",
        "blur", "crop", "quality", "lang",
        "speed", "vol", "bg", "title", "hook"
    ]:
        app.add_handler(
            CommandHandler(
                command,
                lambda update, context, c=command:
                    update.message.reply_text(
                        f"{c} Feature ကို နောက်အဆင့်မှာ ချိတ်ဆက်ပါမယ်။"
                    )
            )
        )

    app.add_handler(MessageHandler(filters.VIDEO, video_received))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler))

    print("Zin Gyi Recap Bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
