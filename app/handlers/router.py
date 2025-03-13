from aiogram import F, Router
import os
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from app.download_video import downloadConvertSend as dac
from app.download_video.downloadConvertSend import PATH
from app.handlers.buttonOk import keyboardForOk

router = Router()
status_message = None
Path = ""


@router.message(CommandStart())
async def startCmd(message: Message):
    await message.answer(f"Привет. Вас приветствует Бот для скачивания видео с Youtube в аудио формате. Отправь мне ссылку чтобы проверить")


@router.message()
async def donwloadAndSend(message: Message, state: FSMContext):
    if (message.text.startswith("https://")):
        try:
            global status_message
            status_message = await message.answer("Началось скачивание...")

            filename = dac.download(message.text)
            if not filename:
                await message.answer("Не удалось скачать аудиофайл. Проверьте ссылку.")
                return

            if not os.path.exists(PATH):
                os.makedirs(PATH)
            global Path
            Path = os.path.join(PATH, filename)
            await status_message.edit_text(f"Аудио {filename} успешно скачано")
            try:
                audio = FSInputFile(Path)
                sent_message = await message.answer_audio(audio, reply_markup=keyboardForOk)
                global message_id
                message_id = sent_message.message_id
            except FileNotFoundError:
                await message.answer("Файл не найден.")
            except Exception as e:
                await message.answer(f"Произошла ошибка при отправке аудио: {e}")

        except Exception as e:
            await message.answer(f"Произошла ошибка при скачивании: {e}")
    else:
        await message.answer("Не правильная ссылка")


@router.callback_query(F.data == "OK")
async def deleting(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    os.remove(Path)
    await status_message.delete()
    await callback.answer('Файл удален!')
    await callback.answer()
