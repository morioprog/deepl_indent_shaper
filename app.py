import streamlit as st
import urllib.parse

def shape_sentence(sentence):
    return sentence.replace("-\n", "").replace("\n", " ")

def build_deepl_url(sentence, src="en", dst="ja"):
    DEEPL_URL = "https://www.deepl.com/translator#{src}/{dst}/{sentence}"
    return DEEPL_URL.format(src=src, dst=dst, sentence=urllib.parse.quote(sentence))

def main():
    st.title("DeepL Indent Shaper")

    sentence_from = st.text_area("Input sentence", height=300)
    sentence_to = shape_sentence(sentence_from)

    st.markdown("""
        ### Result
        ```
        {res}
        ```
    """.format(res=sentence_to))
    
    st.markdown("""
        <a href="{url}" style="font-size: 20px;" target="_blank">
            <button style="color: #FFFFFF; background: #0D2036; border-radius: 5px; width: 100%; height: 40px;">
                Translate in DeepL
            </button>
        </a>
    """.format(url=build_deepl_url(sentence_to, src="en", dst="ja")), unsafe_allow_html=True)

    st.markdown("""
        ---
        ### Links
        * Twitter: [@morio_prog](https://twitter.com/morio_prog)
        * GitHub: [morioprog/deepl_indent_shaper](https://github.com/morioprog/deepl_indent_shaper)
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
