import os
import openai
import json
import argparse

def main():

    parser = argparse.ArgumentParser(description = "Translator powered by ChatGPT")
    
    parser.add_argument(
        "-l", "--language", type=str, nargs=1, metavar="language to translate to", help="determines your output language."
    )

    parser.add_argument(
        "-w", "--words", type = str, nargs = "*", metavar = "words taken", help = "The words that you put in English."
    )

    args = parser.parse_args()
    
    openai.api_key = "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"
    
    language = args.language
    
    words = args.words
    
    inpt = f"[{language}], [{words}]"
    
    syster = """Act as a translator that can translate English into any language. Be sure to make the results accurate, grammatically correct, proper, and are as easy to understand as can be in the foreign language. The input you will receive is formatted “[language to translate to from English], [words to translate]”. Before you output, check to make sure that the translation makes sense in the foreign language. If it does not, change it to fit the structure of the foreign language. You will then output the sentence in the language specified in the [language to translate to from English] section excluding the [language to translate to from English] section. Always remember that after each translation, you must clear the previous result. Type “ChatGPT to translator.” if you understand."""
    
    messages = [{"role": "system", "content": syster}]
    
    messages.append({"role": "user", "content": inpt})
    
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    
    print(chat.choices[0].message.content)

main()