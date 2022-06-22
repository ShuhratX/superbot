from googletrans import Translator, LANGUAGES
tr = Translator()

def translater(word):
    try:
        result = tr.translate(word, dest='uz').text
        lan = tr.detect(word).lang
        if lan in LANGUAGES:
            til = tr.translate(LANGUAGES[f'{lan}'], dest='uz').text
            return f"Siz yuborgan matn tili: {til.capitalize()},\nO'zbekcha tarjimasi: {result.capitalize()}"
    except:
        return("So'z topilmadi")
if __name__ == '__main__':
    from pprint import pprint as print
    lan = tr.detect('안녕하세요').lang
    print(tr.translate(LANGUAGES[f'{lan}'], dest='uz').text)
    print(tr.translate('안녕하세요', dest='ru').text)