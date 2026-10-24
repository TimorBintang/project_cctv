import time
from datetime import datetime
from dotenv import load_dotenv
from data import cctv_urls
from db import insert_db,init_db,get_connection
from fetcher import check_cctv_url


def main():
    init_db()
    conn = get_connection()
    try:
        print("\n=== BOT MONITORING CCTV SE-BALIKPAPAN AKTIF ===")
        while True:
            now = datetime.now()
            print(f"--- Narik Data: {now.strftime('%Y-%m-%d %H:%M:%S')} ---")
    
            for nama, url in cctv_urls.items():
                http_status, size, indikasi = check_cctv_url(url)
                insert_db(conn,now,nama,http_status,size,indikasi)
                print(f"[{nama}] -> Size: {size} bytes | Status: {indikasi}")
                    
            print("--- Data tersimpan! Tidur 5 menit... ---\n")
            time.sleep(300)

    except KeyboardInterrupt:
        print("\n[!] Bot dihentikan secara manual oleh pengguna (Ctrl + C).")
    except Exception as e:
        print(f"bot nya berhenti karena error jir, {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()