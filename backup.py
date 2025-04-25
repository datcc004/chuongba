import os
import datetime
import schedule
import time
from mail_utils import send_mail

def backup_database():
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    db_files = [f for f in os.listdir() if f.endswith('.sql') or f.endswith('.sqlite3')]

    if not db_files:
        send_mail("Backup thất bại", "Không tìm thấy file database nào (.sql hoặc .sqlite3).")
        return

    backup_dir = "backup"
    os.makedirs(backup_dir, exist_ok=True)

    success = True
    messages = []

    for db_file in db_files:
        backup_path = os.path.join(backup_dir, f"{now}_{db_file}")
        try:
            with open(db_file, 'rb') as fsrc, open(backup_path, 'wb') as fdst:
                fdst.write(fsrc.read())
            messages.append(f" Đã backup: {db_file}")
        except Exception as e:
            success = False
            messages.append(f" Lỗi backup {db_file}: {e}")

    subject = "Backup thành công" if success else "Backup hoàn thành nhưng có lỗi"
    body = "\n".join(messages)
    send_mail(subject, body)

schedule.every().day.at("00:00").do(backup_database)

print("🕛 Đang chạy dịch vụ backup. Chờ đến 00:00...")
while True:
    schedule.run_pending()
    time.sleep(60)
