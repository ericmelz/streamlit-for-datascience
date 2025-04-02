import streamlit as st

st.title('Title')
st.caption('This is a caption')
st.header('Header')
st.subheader('Subheader')
st.code("""
import streamlit

st.write('yow')

def generate_random(size):
    rand = np.random.random(size)
    return rand
    
number = generate_random(10)
""", language='python')

st.latex("""x_3^2""")
st.latex("""a + ar + ar^2 + \\cdots + a r^{n-1} = \\sum_{k=0}^{n-1} a r^k""")
st.latex("""\\def\\arraystretch{1.5}
   \\begin{array}{c:c:c}
   a & b & c \\\\ \\hline
   d & e & f \\\\
   \\hdashline
   g & h & i
\\end{array}""")
st.latex("""\\frac{a^2}{b^3}""")
st.markdown("<https://katex.org/docs/supported.html>")