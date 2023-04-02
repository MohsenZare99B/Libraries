import streamlit as st
import pandas as pd

st.title("Hi! I am title")
st.subheader("Hi! I am subheader")
st.header("Hi! I am header")
st.text("Hi! I am text")
st.caption("Hi! I am caption")
st.markdown("---")

st.markdown("**Markdown** *guide*: [Website](https://www.markdownguide.org/cheat-sheet)")
st.write("With *st.write()* you can also write markdown")
st.markdown("---")

st.markdown("<h1>This is a h1 html tag</h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("[KaTeX documentation](https://katex.org/docs/supported.html)")
st.latex(r"\KaTeX")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.markdown("---")

json = {"a":"1, 2, 3", "b": "4, 5, 6"}
st.json(json)
st.markdown("---")

code = """
print("This is python code!")
def f(a, b):
    return a + b
"""
st.code(code, language="python")
st.markdown("---")

st.write("## Metric")
st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4ms⁻¹")
st.write("For writing ⁻¹ after installing 'Fast Unicode Math Correcter' extention in VS Code, write /^-1 and hit space")
st.markdown("---")

table = pd.DataFrame({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})
st.write("Table:")
st.table(table)
st.write("Dataframe:")
st.dataframe(table)
st.write("Difference between table and dataframe is that in dataframe you can sort columns by clicking on them!")
st.markdown("---")

st.image("image.jpeg", caption="This is my image", width=680)
st.audio("Audio.mp3")
st.video("Video.mp4")