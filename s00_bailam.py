#region debai
"""
--- ma debai / id
get_name_in_email(email_list)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://github.com/duongvq-py/toyaemailhople/blob/main/s00_bailam.py

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo trinhduyetweb de kiemtra tep s00_bailam.py, va lay diachi/url aka githubbailamurl

02b dán diachi githubbailamurl theo mẫu ở trang web duoiday
    https://forms.gle/5T83mucjJj7nhjab7

--- debai / problem
Viết hàm 
  get_name_in_email(email_list)
trả về tên tài khoản trong email 
Nếu email không hợp lệ, trả về 'ERROR invaid email'

--- vidu mau / testcase
Khi chay voi input                                        | Ketqua output
--------------------------------------------------------- | -----------------
get_name_in_email(['ai-btx@gmail.com'])                   | ['ai-btx']
get_name_in_email(['user1@gmail.com', 'user2@gmail.com']) | ['user1', 'user2']
get_name_in_email([])                                     | []
get_name_in_email(['abb#ccc'])                            | ['ERROR invaid email']
get_name_in_email([None])                                 | ['ERROR invaid email']
get_name_in_email([None, 'abb#ccc'])                      | ['ERROR invaid email', 'ERROR invaid email']
"""
#endregion debai

#region bailam
import re


def get_name_in_email(email_list):

    kq = []
    checkKyTu = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    for email in email_list:
        if email is None or  "@" not in email:
            kq.append('ERROR invaid email')
        elif email and re.match(checkKyTu, email):
            nameEmail = email.split('@')[0]
            kq.append(nameEmail)
        #else:
        #kq.append('ERROR invalid email')
    return kq


print(get_name_in_email(['ai-btx@gmail.com']))
print(get_name_in_email(['user1@gmail.com', 'user2@gmail.com']))
print(get_name_in_email([]))
print(get_name_in_email(['abb#ccc']))
print(get_name_in_email([None]))
print(get_name_in_email([None, 'abb#ccc']))

#endregion bailam
