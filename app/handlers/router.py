from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from app.download_video import downloadConvertSend as dac
from app.download_video.downloadConvertSend import PATH, file_name


router = Router()


class TranslationStates(StatesGroup):
    nameOfVideo = State()


@router.message(CommandStart())
async def startCmd(message: Message):
    await message.answer(f"Привет. Вас приветствует бот-переводчик. Напишите мне для перевода")


@router.message()
async def donwloadAndSend(message: Message, state: FSMContext):

    await state.update_data(text=message.text)
    await state.set_state(TranslationStates.nameOfVideo)
    if message.text.startswith("https://youtu"):
        Path = PATH + "\\" + dac.download(message.text)
        filename = dac.download(message.text)
        await message.answer(f"Аудио {filename} успешно скачано в формате MP3!")
        with open(filename, 'rb') as file:
            audio = InputFile(file)

        # audio = open(f'{PATH}\\{filename}', 'rb')
        await message.answer_audio(audio=audio)
    else:
        await message.answer("Неправильная ссылка")
