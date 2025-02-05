from gtts import gTTS

texto: str = 'my name is jonh'


def audio_generator(text: str, lang: str = 'en', slow: bool = False, file_name: str = 'audio') -> None:

    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(f'{file_name}.mp3')
    print('save')


audio_generator(texto)
