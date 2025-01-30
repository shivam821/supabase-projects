# from dotenv import load_dotenv
# load_dotenv()

# import os
# from supabase import create_client, Client

# url = os.environ.get("SUPABASE_URL")
# key = os.environ.get("SUPABASE_KEY")
# supabase = create_client(url, key)

# ## CRUD Operation 

# # data = supabase.table("todos").select("*").execute()
# # print(data)

# # data = supabase.table("todos").insert({"Name":"Item 2"}).execute()

# # data = supabase.table("todos").delete().eq("id", 1).execute()


# # Sign-up
# users_email = input('Enter the email : ')
# users_password = input('Enter the password : ')
# # user = supabase.auth.sign_up({ "email": users_email, "password": users_password })

# try : 
#     user = supabase.auth.sign_in_with_password({ "email": users_email, "password": users_password })
#     if user : 
#         print('Loign Sucessful')
# except Exception as e :
#     print(f'Login Failed',{e})
# supabase.auth.sign_out()


# from smtplib import SMTP
# import smtplib
# s = smtplib.SMTP('smtp.gmail.com', 587)
# # start TLS for security
# s.starttls()
# # Authentication
# s.login("snehaarcon@gmail.com", "okns hqvc bwrz oieq")
# # message to be sent
# message = "Message_you_need_to_send"
# # sending the mail
# s.sendmail("snehaarcon@gmail.com", "panigrahishivam821@gmail.com", message)
# # terminating the session
# s.quit()



from smtplib import SMTP
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("snehaarcon@gmail.com", "okns hqvc bwrz oieq")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("snehaarcon@gmail.com", "panigrahishivam821@gmail.com", message)
# terminating the session
s.quit()