import streamlit as st
from kemangen import generate_keyman
from io import StringIO

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
st.write("Rows with no type, or 'word' type will be treated as text replacement once you type space. In the above example typing 'kala ' (with a space) will produce 🐟.")
st.write("You can aslo use U+ unicode point notation. In the above example 'tenpo ' (with space) will produce ⏰")
st.write("If you would like to bring up a menu when something is typed add a single diget number afer the word. In the above example typing 'pona ' will bring up a menu with 👍 and 🙂 as options.")
st.write("This script current supports two additional 'types', 'punctuation'. The above example will produce❗when '! ' (with a space) is typed, regardles of what come before the !.\n"+
         "And 'letter' which will always convert the typed key regadless of what comes before or after. In the above example typing 'a' (no space) anywhere will produce ")
st.write("Keep in mind, in the above example typing 'kala ' will no longer produce 🐟 because the last line will turn all 'a' into '🅰' producing 'k🅰l🅰 ' which is not listed.")


keyboardName = st.text_input("Name you want to give to your keyboard")
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

