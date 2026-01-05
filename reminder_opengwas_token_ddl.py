import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

def send_reminder():
    # 优先从环境变量读取，如果没有则使用备用值（建议在 GitHub Secrets 配置 MAIL_PASS）
    password = os.getenv('MAIL_PASS') 
    sender_email = "312198221@qq.com"
    receiver_email = "mols15712965701@163.com"
    
    if not password:
        print("❌ 错误：未找到授权码")
        return

    # 邮件正文
    message = MIMEText("您的 Token 将于 2026-01-19 00:34 到期，请及时更新。", 'plain', 'utf-8')
    
    # --- 严格符合 RFC 5322/2047 规范的设置 ---
    # 使用 formataddr 自动处理：昵称 (Base64编码) + 空格 + <邮箱地址>
    message['From'] = formataddr((Header('Token提醒机器人', 'utf-8').encode(), sender_email))
    message['To'] = receiver_email
    message['Subject'] = Header("【重要】Token 到期预警", 'utf-8')

    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465) 
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email], message.as_string())
        server.quit()
        print("✅ 邮件发送成功！")
    except Exception as e:
        print(f"❌ 发送失败，原因: {e}")

if __name__ == "__main__":
    send_reminder()
