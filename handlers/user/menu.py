from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboard.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Greetings, Engene! Which member do you want to know more about?", reply_markup=menu)

@dp.message_handler(Text(equals=["Heeseung"]))
async def get_food(message:Message):
    await message.answer(f"{message.text} (희승) is a member of the boy group ENHYPEN who debuted on November 30th, 2020.",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Jay"]))
async def get_food(message:Message):
    await message.answer(f"{message.text}(제이) is a South Korean-American singer under Belift Lab. He is a member of the boy group ENHYPEN.",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Jake"]))
async def get_food(message:Message):
    await message.answer(f"{message.text}(제이크) is a Korean-Australian rapper and singer under Belift Lab. He is a member of the boy group ENHYPEN.",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Sunghoon"]))
async def get_food(message:Message):
    await message.answer(f"{message.text}(박성훈) is a South Korean singer, television host, and former figure skater. He is a member of the boy band Enhypen.",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Sunoo"]))
async def get_food(message:Message):
    await message.answer(f"{message.text}(선우) is a South Korean singer under Belift Lab. He is a member of the boy group ENHYPEN.",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Jungwon"]))
async def get_food(message:Message):
    await message.answer(f"{message.text}(정원) is a South Korean singer under Belift Lab. He is a member and the leader of the boy group ENHYPEN.",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Ni-ki"]))
async def get_food(message:Message):
    await message.answer(f"{message.text}(Japanese: 西村力 (にしむら りき), Hangul: 니시무라 리키), more well known by his stage name NI-KI (Hangul: 니키, Japanese: ニキ), is a member of the South Korean boy group ENHYPEN. He was born on December 9, 2005 and is the maknae of the group, as well as the only Japanese member.",
                         reply_markup=ReplyKeyboardRemove())