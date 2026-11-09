import streamlit as st

st.set_page_config(
    page_title="C-Master: Learn C from Scratch", page_icon="💻", layout="wide"
)

# Custom Styling
st.markdown(
    """
    <style>
    .main-header { font-size: 2.5rem; color: #1f77b4; font-weight: 700; }
    .sub-header { font-size: 1.5rem; color: #2ca02c; font-weight: 600; }
    .card { background-color: #f9f9f9; padding: 20px; border-radius: 10px; border-left: 5px solid #1f77b4; margin-bottom: 20px; }
    .syntax-box { background-color: #272822; color: #f8f8f2; padding: 15px; border-radius: 5px; font-family: monospace; }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Navigation for Structured Learning
st.sidebar.title("🚀 C Programming Roadmap")
st.sidebar.markdown(
    "Structured path from absolute basics to advanced concepts."
)

modules = {
    "1. Basics & Introduction": [
        "Introduction to C & History",
        "Structure of a C Program",
        "Variables & Data Types",
        "Input and Output (scanf/printf)",
    ],
    "2. Control Flow": [
        "Conditional Statements (if, else, switch)",
        "Loops: for loop",
        "Loops: while & do-while loop",
        "break and continue statements",
    ],
    "3. Functions & Arrays": [
        "Introduction to Functions",
        "Recursion",
        "1D and 2D Arrays",
        "Strings and String Functions",
    ],
    "4. Advanced Concepts": [
        "Pointers Basics",
        "Pointers and Arrays",
        "Structures and Unions",
        "File Handling in C",
    ],
}

selected_module = st.sidebar.selectbox("Select Module", list(modules.keys()))
selected_topic = st.sidebar.radio("Select Topic", modules[selected_module])

# Main Content Area
st.markdown(
    '<p class="main-header">💻 C-Master: Interactive C Learning Hub</p>',
    unsafe_allow_html=True,
)
st.markdown(f"**Current Path:** `{selected_module} > {selected_topic}`")
st.markdown("---")

# Dynamic Content based on selection
if selected_topic == "Introduction to C & History":
  st.markdown('<p class="sub-header">Topic: Introduction to C</p>', unsafe_allow_html=True)
  st.markdown("""
        <div class="card">
        <b>Short Definition:</b> C is a powerful, procedural computer programming language developed by Dennis Ritchie at Bell Labs in 1972. It provides low-level access to memory and is the foundation for modern languages like C++, Java, and Python.
        </div>
        """, unsafe_allow_html=True)

  st.markdown("### 📝 Syntax Structure")
  st.markdown(
      '<div class="syntax-box">#include &lt;stdio.h&gt;<br><br>int main() {'
      '<br>&nbsp;&nbsp;&nbsp;&nbsp;// Your code here<br>&nbsp;&nbsp;&nbsp;&nbsp;return'
      " 0;<br>}</div>",
      unsafe_allow_html=True,
  )

  st.markdown("### 💡 Example Program")
  st.code(
      """#include <stdio.h>

int main() {
    printf("Hello, World! Welcome to C programming.\\n");
    return 0;
}""",
      language="c",
  )

  st.markdown("### 🛠️ Interactive Challenge")
  st.markdown(
      "**Task:** Write a C program that prints your name instead of 'Hello,"
      " World!'."
  )

  user_code = st.text_area(
      "Type your C code here:",
      value="""#include <stdio.h>

int main() {
    printf("My name is Monika\\n");
    return 0;
}""",
      height=150,
  )

  if st.button("Run & Validate Code"):
    if "printf" in user_code and "main" in user_code:
      st.success(
          "🎉 Excellent! Your code structure is correct. It successfully uses"
          " `main()` and `printf()`."
      )
    else:
      st.error(
          "❌ Make sure your code includes the `main` function and a `printf`"
          " statement!"
      )

elif selected_topic == "Variables & Data Types":
  st.markdown('<p class="sub-header">Topic: Variables & Data Types</p>', unsafe_allow_html=True)
  st.markdown("""
        <div class="card">
        <b>Short Definition:</b> Variables are containers for storing data values. Data types tell the compiler what kind of value a variable will hold (e.g., integers, floats, characters).
        </div>
        """, unsafe_allow_html=True)

  st.markdown("### 📝 Syntax Structure")
  st.markdown(
      '<div class="syntax-box">datatype variable_name = value;<br><i>Example:</i>'
      " int age = 25;</div>",
      unsafe_allow_html=True,
  )

  st.markdown("### 💡 Example Program")
  st.code(
      """#include <stdio.h>

int main() {
    int age = 25;
    float temperature = 36.6;
    char grade = 'A';
    
    printf("Age: %d\\n", age);
    printf("Temperature: %.1f\\n", temperature);
    printf("Grade: %c\\n", grade);
    return 0;
}""",
      language="c",
  )

  st.markdown("### 🛠️ Interactive Challenge")
  st.markdown(
      "**Task:** Declare an integer variable named `year` with value `2026` and"
      " print it using `printf`."
  )

  user_code = st.text_area(
      "Type your C code here:",
      value="""#include <stdio.h>

int main() {
    int year = 2026;
    printf("Year: %d\\n", year);
    return 0;
}""",
      height=150,
  )

  if st.button("Run & Validate Code"):
    if "int year" in user_code or "year =" in user_code:
      st.success(
          "🎉 Awesome job! You correctly declared and printed a variable."
      )
    else:
      st.error(
          "❌ Try declaring an integer variable named `year` and printing it."
      )

else:
  st.markdown(
      f'<p class="sub-header">Topic: {selected_topic}</p>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<div class="card"><b>Short Definition:</b> Content for this advanced'
      " module is being structured to ensure a smooth, step-by-step learning"
      " curve without confusion!</div>",
      unsafe_allow_html=True,
  )
  st.markdown("### 💡 Example Framework")
  st.code(
      """#include <stdio.h>

int main() {
    // Coming soon in your custom curriculum updates!
    return 0;
}""",
      language="c",
  )

st.sidebar.markdown("---")
st.sidebar.info(
    "Built for structured, stress-free C programming mastery. Access this link"
    " anywhere!"
)