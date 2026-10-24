from dotenv import load_dotenv
import os,psycopg2

def get_connection():
    load_dotenv()
    return psycopg2.connect(
        host = os.getenv('DB_HOST'), database = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'), password = os.getenv('DB_PASS')
    )

def init_db():
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS log_cctv (
                        id SERIAL PRIMARY KEY, 
                        waktu_cek TIMESTAMP, 
                        nama_cctv VARCHAR(100), 
                        http_status INT, 
                        ukuran_byte INT, 
                        indikasi_status VARCHAR(50)
                    );
                """)
        conn.commit()
        conn.close()

def insert_db(conn,now,nama,http_status,size,indikasi):
    with conn.cursor() as cur:
          cur.execute("""
               INSERT INTO log_cctv(waktu_cek,nama_cctv,http_status,ukuran_byte,indikasi_status) VALUES (%s,%s,%s,%s,%s)""",
               (now,nama,http_status,size,indikasi)
            )
    conn.commit()      