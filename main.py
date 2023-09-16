import streamlit as st
import smtplib
from email.message import EmailMessage

#Provides tab title and icon
st.set_page_config(layout="centered", page_title="Deadnettle Farms", page_icon="🌿")

#Creates container for vertical stack of elements
with st.container():

    #Creates header image and text input box
    st.image("https://raw.githubusercontent.com/OneCityCode/Deadnettle/main/dnf.png")

    st.subheader("Please use the contact form below for inquiries:")

    uname = st.text_input("name", max_chars=50, placeholder="Name", label_visibility="hidden")
    uphone = st.text_input("phone", max_chars=50, placeholder="Phone Number", label_visibility="hidden")
    umail = st.text_input("email", max_chars=50, placeholder="email adress", label_visibility="hidden")
    udate = st.text_input("date", max_chars=50, placeholder="requested ready date", label_visibility="hidden")
    unotes = st.text_area("notes", max_chars=1000, placeholder="Additional notes (if applicable)", label_visibility="hidden")

    if st.button("Submit", type = "primary"):
        
        
        try:
            msg = f"""\
                Customer information:
                
                Name: {uname}
                
                Phone Number: {uphone}
                
                Email: {umail}
                
                Requested delivery date: {udate}
                
                Additional notes: {unotes}
                """
            fmsg = EmailMessage()
            fmsg.set_content(msg)
            fmsg['Subject'] = f'{uname} contacted you at Deadnettle Farms!'
            fmsg['From'] = st.secrets["dnsendaddress"]
            fmsg['To'] = st.secrets["dnreceiveaddress"]
            server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server_ssl.ehlo() # optional, called by login()
            server_ssl.login(st.secrets["dnsendaddress"], st.secrets["dnsendpass"])  
            server_ssl.send_message(fmsg)
            server_ssl.close()
            st.write("Sent successfully!")
        except:
            st.write("Failed to send")
