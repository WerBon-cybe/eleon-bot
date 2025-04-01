import asyncio
from gc import callbacks
from aiogram import F, Bot, Dispatcher, Router
from aiogram.types import Message, BotCommand, FSInputFile
from aiogram.filters import Command
import logging
import os
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telegram import CallbackQuery, InputFile
TOKEN = "7572870049:AAGPqsag2ezeXcka6Fosyl5xvFpqRB7ZDK8"

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
all_media_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'all_media')
photo_file = os.path.join(all_media_dir, 'photo.jpg')
async def main():
    await dp.start_polling(bot)

@dp.message(Command("start"))
async def start_command(message: Message):
    text_start = f"Привет , { message.from_user.first_name }! \nМы компания ELEON - занимаемся ремонтами под ключ с дизайнерскими решениями. В нашей компании клиенты могут:\n\n- Заказать разработку технической документации\n\n- Заказать разработку по Дизайну интерьеров\n\n- Заказать ремонт жилых и коммерческих помещенийМы работаем в 20 городах России и у нас для тебя есть выгодное предложение!\n\nДля начало выбери своё направление⏬"
    builder = InlineKeyboardBuilder()
    builder.button(text='Агент по недвижимости', callback_data="agent_nedvizhka")
    builder.button(text='Дизайнер Интерьеров', callback_data="desing_interior")
    await message.answer(text_start, reply_markup=builder.as_markup())

@dp.callback_query(F.data == 'agent_nedvizhka')
async def agent_nedvizhka(callback: CallbackQuery):

    Doc = InputFile('document.pdf')
    text_agent1 = "Сделав сделку, ты можешь получить комиссию с продажи от 2 до 5% от стоимости квартиры, как агент. И я думаю что ты уже задавался вопросом, а как можно зарабатывать дополнительно, безопасно и не нанося вреда своей репутации\n\nСтановясь нашим партнером, ты получаешь огромные преимущества перед конкурентами на рынке ремонта и отделки. Представь, твоему клиенту не нужно искать подрядчиков, ты сразу можешь взять на себя все его потребности, увеличивая при этом свой доход. Что мы предлагаем?\n\nТы рекомендуешь нас как строительную компанию и получаешь комиссионные вознаграждения от сметы.\nПосмотри наше предложение⬇️"
    await callback.message.answer_photo(photo = FSInputFile('photo_agent1.jpg'), caption = text_agent1)
    await callback.message.answer_document(document=FSInputFile('document.pdf'))
    await asyncio.sleep(5)

    text_agent2 = "Я хочу показать тебе один из инструментов, благодаря чему ты сможешь отслеживать, свои партнерские выплаты.\n\nЭто мобильное приложение 101, которое оптимизирует процесс коммуникации в режиме реального времени, ты будешь видеть объект который ты нам передал, стоимость работ и конечно свою комиссию за рекомендацию\n\nПосмотри видео о том, как работает приложение.⏬\n\nhttps://youtu.be/_3E6MBvBp-U"
    await callback.message.answer_photo(photo = FSInputFile('photo_agent2.jpg'), caption = text_agent2)
    await asyncio.sleep(5)

    text_agent3 = "Внутри компании ELEON, есть четкое понимание, что партнеры компании это одни из ключевых людей, поэтому мы готовы платить за рекомендацию 20% от прибыли с каждого проекта.\n\nДавайте рассмотрим один из последних примеров⏬"
    await callback.message.answer_photo(photo = FSInputFile('photo_agent3.jpg'), caption = text_agent3)
    await callback.message.answer_document(document=FSInputFile('balance.pdf'), caption = "Вот так выглядит балансовый отчет, это смета и все операции которые проходили по объекту. Такой отчет можно сформировать в нашем приложение 101")
    await callback.message.answer("Там же в приложение вы можете увидеть сколько заработала компания с проекта.")
    text_agent4 = "Вы видите, что прибыль компании с проекта составила: 316 178 + 54 186 рублей= 370 364 рубля.\nПартнерское вознаграждение составила 370 364*20% =74 072 рубля"    
    await callback.message.answer_photo(photo = FSInputFile('photo_agent4.jpg'), caption = text_agent4)
    await asyncio.sleep(5)

    text_agent5 = "74 072 рубля не плохая прибавка?\n\nРекомендуя нас, вы будете точно знать, какая сумма договора и сколько вы заработаете с этого проекта. При всем мы работаем не на словах, а заключаем договор.\n\nСледующим шагом отправляем тебе наш договор о партнерском соглашении и презентацию для клиентов. Обязательно изучи их."
    await callback.message.answer_photo(photo = FSInputFile('photo_agent5.jpg'), caption = text_agent5)
    await callback.message.answer_document(document=FSInputFile('dogovor.docx'))
    await asyncio.sleep(5)

    text_agent6 = f"{callback.from_user.first_name} у тебя появились вопросы, которые ты хотел бы задать?\nИли ты хотел бы больше информации?\n\nВернись к человеку, который дал ссылку на этого бота."
    builder = InlineKeyboardBuilder()
    builder.button(text='Написать менеджеру', url="t.me/eleonvrn")
    await callback.message.answer_photo(photo = FSInputFile('photo_agent6.jpg'), caption = text_agent6, reply_markup=builder.as_markup())

@dp.callback_query(F.data == 'desing_interior')
async def agent_nedvizhka(callback: CallbackQuery):

    diz1 = "Делая дизайн-проект и получая 2000-3000 рублей за квадратный метр, у тебя уходит очень много личного времени. А если еще добавить авторский надзор? А если бригада строителей некомпетентна или не говорит по-русски, это еще больше головной боли.  \n\nСтановясь нашим партнером, ты получаешь огромные преимущества перед конкурентами на рынке ремонта и отделки. Представь, твоему клиенту не нужно искать подрядчиков, ты сразу можешь взять на себя все его потребности, увеличивая при этом свой доход. Что мы предлагаем?  \n\nТы рекомендуешь нас как строительную компанию и получаешь комиссионные вознаграждения от сметы.  \n\nПосмотри наше предложение⬇️"
    await callback.message.answer_document(document=FSInputFile('diz1.pdf'))
    await callback.message.answer_photo(photo = FSInputFile('diz1.jpg'), caption = diz1)
    await callback.message.answer_document(document=FSInputFile('diz2.pdf'))
    await asyncio.sleep(5)

    diz2 = "Я хочу показать тебе один из инструментов, благодаря чему ты сможешь отслеживать, свои партнерские выплаты.\n\nЭто мобильное приложение 101, которое оптимизирует процесс коммуникации в режиме реального времени, ты будешь видеть объект который ты нам передал, стоимость работ и конечно свою комиссию за рекомендацию\n\nПосмотри видео о том, как работает приложение.⏬\n\nhttps://youtu.be/_3E6MBvBp-U"
    await callback.message.answer_photo(photo = FSInputFile('diz2.jpg'), caption = diz2)
    await asyncio.sleep(5)

    text_agent3 = "Внутри компании ELEON, есть четкое понимание, что партнеры компании это одни из ключевых людей, поэтому мы готовы платить за рекомендацию 20% от прибыли с каждого проекта.\n\nДавайте рассмотрим один из последних примеров⏬"
    await callback.message.answer_photo(photo = FSInputFile('photo_agent3.jpg'), caption = text_agent3)
    await callback.message.answer_document(document=FSInputFile('balance.pdf'), caption = "Вот так выглядит балансовый отчет, это смета и все операции которые проходили по объекту. Такой отчет можно сформировать в нашем приложение 101")
    await callback.message.answer("Там же в приложение вы можете увидеть сколько заработала компания с проекта.")
    text_agent4 = "Вы видите, что прибыль компании с проекта составила: 316 178 + 54 186 рублей= 370 364 рубля.\nПартнерское вознаграждение составила 370 364*20% =74 072 рубля"    
    await callback.message.answer_photo(photo = FSInputFile('photo_agent4.jpg'), caption = text_agent4)
    await asyncio.sleep(5)

    text_agent5 = "74 072 рубля не плохая прибавка?\n\nРекомендуя нас, вы будете точно знать, какая сумма договора и сколько вы заработаете с этого проекта. При всем мы работаем не на словах, а заключаем договор.\n\nСледующим шагом отправляем тебе наш договор о партнерском соглашении и презентацию для клиентов. Обязательно изучи их."
    await callback.message.answer_photo(photo = FSInputFile('photo_agent5.jpg'), caption = text_agent5)
    await callback.message.answer_document(document=FSInputFile('dogovor.docx'))
    await asyncio.sleep(5)

    text_agent6 = f"{callback.from_user.first_name} у тебя появились вопросы, которые ты хотел бы задать?\nИли ты хотел бы больше информации?\n\nВернись к человеку, который дал ссылку на этого бота."
    builder = InlineKeyboardBuilder()
    builder.button(text='Написать менеджеру', url="t.me/eleonvrn")
    await callback.message.answer_photo(photo = FSInputFile('photo_agent6.jpg'), caption = text_agent6, reply_markup=builder.as_markup())

if __name__ == "__main__":
    asyncio.run(main())