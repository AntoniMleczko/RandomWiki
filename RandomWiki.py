from fastapi import FastAPI
from wonderwords import RandomWord

w = RandomWord()
app = FastAPI()

@app.get("/")
def main():
    return {"to get the link": "go to /link"}

@app.get("/link")
def link():
    word = w.word(include_parts_of_speech=["nouns"])
    wiki_link = f"https://wikipedia.org/wiki/{word}"

    return {"word": word, "link": wiki_link}

