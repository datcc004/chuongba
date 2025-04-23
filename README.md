# Script Backup Database Hằng Ngày

Script này sẽ tự động backup các file `.sql` và `.sqlite3` mỗi ngày lúc 00:00 (nửa đêm), và gửi email thông báo về kết quả.

## Hướng dẫn sử dụng

1. Clone repo về máy
2. Cài đặt thư viện:
    ```
    pip install -r requirements.txt
    ```
3. Tạo file `.env` chứa thông tin email như mẫu
4. Chạy script:
    ```
    python backup.py
    ```

**Lưu ý:** Không được push file `.env` lên GitHub!
