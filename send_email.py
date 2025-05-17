#寄送Email
#準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg['From']='kai860614@gmail.com'
msg['To']='kai860614@gmail.com'
msg['Subject']='測試信件'
#寄送純文字的內容
msg.set_content('測試')
#寄送比較多樣式的內容(html)
msg.add_alternative('<h3>優惠券</h3>滿五百送一百',subtype='html')

#連線到SMTP server, 驗證寄件人身份並發送郵件
import smtplib
#到網路上搜尋gmail smtp server參數
server=smtplib.SMTP_SSL('smtp.gmail.com',465) #SMTP須與寄件人相同信箱 (SMTP, port)
server.login('kai860614@gmail.com','密碼') #密碼需透過Google帳戶的應用程式密碼建立
server.send_message(msg)
server.close()