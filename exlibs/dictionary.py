import requests

class Dictionary:
    def meaning(self,word):
        final=""
        api=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        data=requests.get(api)
        if data.status_code==200:
            data=data.json()

            for item in data:
                if 'word' in item:
                    # print("Word:", item['word'])
                    final+=f"\nWord: {item['word']}\n"

                if 'phonetics' in item and isinstance(item['phonetics'], list) and item['phonetics']:
                    # print("Phonetics:")
                    final+=f"\nPhonetics:\n"
                    for phonetic in item['phonetics']:
                        if 'text' in phonetic:
                            # print("- Text:", phonetic['text'])
                            final=f"\n-Text: {phonetic['text']}\n"

                        # if 'audio' in phonetic:
                        #     print("  Audio:", phonetic['audio'])
                        # if 'sourceUrl' in phonetic:
                        #     print("  Source URL:", phonetic['sourceUrl'])
                        # if 'license' in phonetic:
                        #     license_info = phonetic['license']
                        #     if 'name' in license_info:
                        #         print("  License:", license_info['name'])
                        #     if 'url' in license_info:
                        #         print("  License URL:", license_info['url'])
                
                if 'meanings' in item and isinstance(item['meanings'], list) and item['meanings']:
                    # print("Meanings:")
                    final+=f"\nMeanings:\n"
                    for meaning in item['meanings']:
                        if 'partOfSpeech' in meaning:
                            # print("- Part of Speech:", meaning['partOfSpeech'])
                            final+=f"\n- Part of Speech: {meaning['partOfSpeech']}\n"
                        if 'definitions' in meaning and isinstance(meaning['definitions'], list) and meaning['definitions']:
                            for definition in meaning['definitions']:
                                if 'definition' in definition:
                                    # print("  Definition:", definition['definition'])
                                    final+=f"\n  Definition: {definition['definition']}\n"
                                if 'synonyms' in definition and definition['synonyms']:
                                    # print("  Synonyms:", definition['synonyms'])
                                    final+=f"\n  Synonyms:\n"
                                    for element in definition['synonyms']:
                                        final+=f"{element}\n"
                                if 'antonyms' in definition and definition['antonyms']:
                                    # print("  Antonyms:", definition['antonyms'])
                                    final+=f"\n  Antonyms:\n"
                                    for element in definition['antonyms']:
                                        final+=f"{element}\n"

                                if 'example' in definition:
                                    # print("  Example:", definition['example'])
                                    final+=f"\n  Example: {definition['example']}\n"
                        # if 'sourceUrls' in meaning and meaning['sourceUrls']:
                        #     print("  Source URLs:", meaning['sourceUrls'])
        return final




# word="hello"

# c=Dictionary()

# print(c.meaning(word))