import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(to_email, resume_path):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "ankit.op113@gmail.com"
    smtp_password = "ugwa pybc oodl wmnh"

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use server.starttls() for non-SSL connections
            server.login(smtp_username, smtp_password)

            message = MIMEMultipart()
            message['Subject'] = 'New Job Application'
            message['From'] = smtp_username
            message['To'] = to_email

            text = "Thank you for submitting your resume. We will review your application shortly."
            message.attach(MIMEText(text, 'plain'))

            with open(resume_path, 'rb') as resume_file:
                resume_attachment = MIMEApplication(resume_file.read(), _subtype="pdf")
                resume_attachment.add_header('Content-Disposition', f'attachment; filename=resume.pdf')
                message.attach(resume_attachment)

            server.sendmail(smtp_username, to_email, message.as_string())
        st.success('Email sent successfully!')
    except Exception as e:
        st.error(f"Error sending email: {e}")

def main():
    st.title('Job Notification Application')

    email = st.text_input('Enter your email:')
    resume = st.file_uploader('Upload your resume (PDF format):', type=['pdf'])

    if st.button('Submit'):
        if email and resume:
            resume_path = f"{email}_resume.pdf"
            with open(resume_path, 'wb') as resume_file:
                resume_file.write(resume.read())

            send_email(email, resume_path)
        else:
            st.error('Please enter your email and upload your resume.')

if __name__ == "__main__":
    main()

