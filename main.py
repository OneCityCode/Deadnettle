import streamlit as st
import smtplib, ssl

#Provides tab title and icon
st.set_page_config(layout="centered", page_title="Mondrean", page_icon="🖌️")

#Creates container for vertical stack of elements
with st.container():

    #Creates header image and text input box
    st.image("https://raw.githubusercontent.com/OneCityCode/Test/main/Streamlit/Title.png")

    st.title("Please use the contact form below for inquiries")

    uname = st.text_input("", max_chars=50, placeholder="Name")
    uphone = st.text_input("", max_chars=50, placeholder="Phone Number")
    umail = st.text_input("", max_chars=50, placeholder="email adress")
    uaddress = st.text_input("", max_chars=50, placeholder="delivery address (if applicable)")
    unotes = st.text_area("", max_chars=1000, placeholder="delivery address")

    if st.button("Submit", type = "primary"):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = st.secrets["dnsendaddress"]  # Enter your address
        receiver_email = st.secrets["dnreceiveaddress"]  # Enter receiver address
        password = st.secrets["dnsendpass"]
        message = f"""\
        Subject: You have a new customer contact at Deadnettle Farms!
        Customer information:
        Name: {uname}
        Phone Number: {uphone}
        Email: {umail}
        Address: {uaddress}
        Additional notes: {unotes}
        """

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

        server.quit() 

        st.write("Successfully Sent!")