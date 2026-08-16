import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8905805033:AAHDgan58Sgw9POQn80v6NAqfucl7nmmJoI"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 ЧЁРНЫЙ ЯЩИК\n\n"
        "Ты нашёл место, где нет правильных ответов.\n"
        "Здесь можно задать вопрос. Любой.\n"
        "Ящик не обещает ответа.\n"
        "Но если вопрос будет точным — он может откликнуться.\n\n"
        "Иногда ящик молчит.\n"
        "Иногда даёт знак.\n"
        "Иногда просто отправляет текст, который ты должен был прочитать именно сейчас.\n\n"
        "Это не игра.\n"
        "Это эксперимент.\n\n"
        "Как пользоваться:\n"
        "— Отправь любой текст\n"
        "— Если захочешь получить ответ быстрее — используй /pay (5 ⭐)\n"
        "— Ответ может прийти сразу, через час или никогда\n\n"
        "/start — начать заново\n"
        "/pay — ускорить ответ"
    )

async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_invoice(
        title="Чёрный ящик",
        description="Один вопрос. Ответ не гарантирован.",
        payload="void_question",
        provider_token="",
        currency="XTR",
        prices=[{"label": "Вопрос", "amount": 5}],
        need_name=False,
        need_phone_number=False,
        need_email=False
    )

async def pre_checkout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)

async def success(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Вопрос принят.\n\n"
        "Ответ появится в этом чате.\n"
        "Или не появится.\n\n"
        "Ты теперь — часть эксперимента."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pay", pay))
    app.add_handler(CommandHandler("pre_checkout_query", pre_checkout))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, success))
    app.run_polling()

if __name__ == "__main__":
    main()
