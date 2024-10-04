import streamlit as st
from kemangen import generate_keyman
from io import StringIO

col1, col2 = st.columns([2,1])

with col1:
    st.title("KMN generator")
    st.write(
        "This app will take a csv file and generate a well formated KMN file for use in the development of a Keyman Keyboard."
    )
    st.write("The CSV file should be formated as follows\n"
            "[what you type],[what is produced],[Optional: Type]\n"
            "example:")
    st.code("kala,🐟\n"
            "tenpo,U+23F0\n"
            "pona,👍,word\n"
            "pona2,🙂,word\n"
            "!,❗,punctuation\n"
            "a,🅰,letter")

    st.markdown("""# Formatting Rules:
# Types:

## Text Replacement:
Rows without a specified "type" or with the "word" type will be treated as text replacements when followed by a space.

Example: Typing "kala " (with a space) will produce 🐟.

## Punctuation:
The "punctuation" type converts the typed key regardless of what comes before it.

Example: "! " (with a space) will always produce ❗.

## Letter:
The "letter" type converts the typed key regardless of what comes before or after it.

Example: Typing "a" (no space) anywhere will produce 🅰.
            
#### Unicode: You can use U+ unicode point notation.
Example: "tenpo " (with space) will produce ⏰.
            
#### Menus:
To bring up a menu after typing something, add a single digit number after the word.

Example: "pona1" will bring up a menu with 👍 and 🙂 as options.

## Important Note:
Keep in mind that later rules can override earlier rules.
For example, if you have a rule to replace "a" with "🅰", then "kala " will no longer produce 🐟 because the "a" will be replaced first, resulting in "k🅰l🅰 ".""")



with col2:
    keyboardName = st.text_input("Keyboard Name:")
    outputname = keyboardName.lower().replace(" ", "_")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        # To read file as string:
        string_data = stringio.read()
        st.download_button('Download KMN', generate_keyman(string_data, keyboardName, 1.0), file_name= outputname + '.kmn')

