import streamlit as st

def change():
    print(st.session_state.checker)
state = st.checkbox("Default value of this checkbox is True",
 value=True, on_change=change, key="checker")
if state:
    st.write("Checkbox is checked")
else:
    st.write("Checkbox isn't checked")
st.write("---")

radio_button = st.radio("In which country do you live?",
 options=("Iran", "Afghanistan", "USA"))
print(radio_button)
st.write("---")

def btn_click():
    print("button clicked!")
btn = st.button("Click me!", on_click=btn_click)
st.write("---")

select = st.selectbox("What is your favorite car?", options=("BMW", "Ferrari", "Benz"))
print(select)
st.write("---")

multi_select = st.multiselect("What is your favorite  Tech brand?",
 options=("Google", "Microsoft", "Facebook", "Amazon"))
st.write(multi_select)
st.write("---")

images = st.file_uploader("Please upload some images",
 type=["png", "jpeg", "jpg"], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)
st.write("---")

val = st.slider("This is a slider", min_value=20, max_value=80, value=60)
print(val)
st.write("---")

text_input = st.text_input("Enter your course title", max_chars=60)
print(text_input)
st.write("---")

text_area = st.text_area("Course description")
print(text_area)
st.write("---")

date = st.date_input("Enter your registration date")
print(date)
st.write("---")

form = st.form("Form 1", clear_on_submit=True)
form.text_input("First Name")
form.form_submit_button("Submit")
st.write("---")

with st.form("Form 2"):
    col1, col2 = st.columns(2)
    fname = col1.text_input("First Name")
    lname = col2.text_input("Last Name")
    email = st.text_input("Email")
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state = st.form_submit_button("Submit")
    if s_state:
        if fname == "" or lname == "" or email == "":
            st.warning("Please fill fields")
        else:
            st.success("Successful")