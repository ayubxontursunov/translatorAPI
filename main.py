from fastapi import FastAPI, HTTPException
from translate import Translator
from uz_en_database import helperDB

app = FastAPI()


@app.get("/")
async def root():
    a = 'msg'
    b = 'Hello!'
    # Corrected return statement
    return {a: b}


def translate_uz_en(text: str) -> str:
    translator = Translator(from_lang="uz", to_lang="en")
    translation = translator.translate(text)
    return translation


def translate_en_uz(text: str) -> str:
    translator = Translator(from_lang="en", to_lang="uz")
    translation = translator.translate(text)
    return translation


@app.get("/uz_en/{prefix}")
def get_data(prefix: str):
    base = helperDB("dictionary.db")
    base.setup('uz_en')
    check = base.check_uz_word(prefix)
    en_word = translate_uz_en(prefix)
    print(f"Translated word: {en_word}")

    if check:
        print("Word already exists in the database.")
        words = base.get_words_en(en_word)
    elif prefix == en_word:
        words = 0
    else:
        print("Word not found in the database, fetching translation.")
        base.add_item(prefix, en_word)
        words = base.get_words_en(en_word)

    if len(words) != 0:
        return {f"{words[0][1]}": f"{words[0][2]}"}
    else:
        raise HTTPException(status_code=404, detail="Translation not found in database")


@app.get("/en_uz/{prefix}")
def get_data(prefix: str):
    base = helperDB("dictionary.db")
    base.setup('uz_en')
    check = base.check_en_word(prefix)
    uz_word = translate_en_uz(prefix)
    print(f"Translated word: {uz_word}")

    if check:
        print("Word already exists in the database.")
        words = base.get_words_uz(uz_word)
    else:
        print("Word not found in the database, fetching translation.")
        base.add_item(uz_word, prefix)
        words = base.get_words_uz(uz_word)

    if len(words) != 0:
        return {f"{words[0][2]}": f"{words[0][1]}"}
    else:
        raise HTTPException(status_code=404, detail="Translation not found in database")


@app.get("/translate/{prefix}")
def get_data(prefix: str):
    global words
    uz_bool = False

    base = helperDB("dictionary.db")
    base.setup('uz_en')

    uz_word = translate_en_uz(prefix)
    en_word = translate_uz_en(prefix)

    check_en = base.check_en_word(prefix)
    check_uz = base.check_uz_word(prefix)

    if prefix == en_word:
        # If the prefix is an English word
        if check_en:
            words = base.get_words_en(prefix)
        else:
            base.add_item(uz_word, prefix)
            words = base.get_words_en(prefix)
    elif prefix == uz_word:
        uz_bool = True
        # If the prefix is an Uzbek word
        if check_uz:
            words = base.get_words_uz(prefix)
        else:
            base.add_item(prefix, en_word)
            words = base.get_words_uz(prefix)
    else:
        raise HTTPException(status_code=400, detail="Unable to determine word language")

    if len(words) != 0:
        if uz_bool:
            return {f"{words[0][1]}": f"{words[0][2]}"}
        else:
            return {f"{words[0][2]}": f"{words[0][1]}"}
    else:
        raise HTTPException(status_code=404, detail="Translation not found in database")
