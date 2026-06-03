# db.py
#
# 초기 캐릭터 데이터를 db에 집어넣는 파이썬 스크립트

import sqlite3
from datetime import datetime

DB_PATH = "conan.db"


# ── DB 초기화 ─────────────────────────────────────
def init_db():
    """
    sensor_data 테이블 생성 (없으면 생성)
    프로그램 시작 시 한 번 호출
    """
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS conan_data (
            id             INTEGER  PRIMARY KEY AUTOINCREMENT,
            ko_name        TEXT,
            en_name        TEXT,
            eye_image      TEXT,
            full_image     TEXT,
            code_name      TEXT
        )
    """)
    #conn.execute("CREATE INDEX IF NOT EXISTS idx_ts ON conan_data(timestamp)")
    conn.commit()
    conn.close()
    print(f"[DB] 초기화 완료: {DB_PATH}")


# ── 데이터 삽입 ───────────────────────────────────
def insert(ko_name: str, en_name: str, eye_image: str, full_image: str, code_name: str) -> int:
    """
    측정값 1건 삽입 → 생성된 ID 반환
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO conan_data (ko_name, en_name, eye_image, full_image, code_name) VALUES (?,?,?,?,?)",
        (ko_name, en_name, eye_image, full_image, code_name),
    )
    conn.commit()
    row_id = cursor.lastrowid
    conn.close()
    return row_id

##### Chat GPT 작성
if __name__ == "__main__":

    init_db()

    insert(
        "쿠로바 카이토",
        "Kaito Kuroba",
        "kaito_eye.jpg",
        "kaito_full.jpg",
        "N"
    )

    insert(
        "쿠도 신이치",
        "Shinichi Kudo",
        "shinichi_eye.jpg",
        "shinichi_full.jpg",
        "N"
    )

    insert(
         "야마토 칸스케",
         "Kansuke Yamato",
         "yamato_eye.jpg",
         "yamato_full.jpg",
         "N"
     )

    insert(
        "후루야 레이",
        "Rei Furuya", 
        "amuro_eye.jpg",
        "amuro_full.jpg",
        "Bourbon(버번)" 
    )

    insert(
         "하기와라 치하야",
         "Chihaya Hagiwara",
         "chihaya_eye.jpg",
         "chihaya_full.jpg",
         "N"
     )

    insert(
         "마츠다 진페이",
         "Jinpei Matsuda",
         "jinpei_eye.jpg",
         "jinpei_full.jpg",
         "N"
     )

    insert(
         "하기와라 켄지",
         "Kengi Hagiwara",
         "kenji_eye.jpg",
         "kenji_full.jpg",
         "N"
     )

    insert(
         "모리 란",
         "Ran Mori",
         "ran_eye.jpg",
         "ran_full.jpg",
         "N"
     )

    insert(
         "사토 미와코",
         "Miwako Sato",
         "sato_eye.jpg",
         "sato_full.jpg",
         "N"
     )

    insert(
         "다테 와타루",
         "Wataru Date",
         "wataru_eye.jpg",
         "wataru_full.jpg",
         "N"
     )

    insert(
         "타카기 와타루",
         "Wataru Takagi",
         "takagi_eye.jpg",
         "takagi_full.jpg",
         "N"
     )

    insert(
         "우에하라 유이",
         "Yui Uehara",
         "yui_eye.jpg",
         "yui_full.jpg",
         "N"
     )

    insert(
         "아카이 슈이치",
         "Shuichi Akai",
         "akai_eye.jpg",
         "akai_full.jpg",
         "Rye(라이)"
     )

    insert(
         "베르무트",
         "Vermouth",
         "baramote_eye.jpg",
         "baramote_full.jpg",
         "Vermouth(베르무트)"
     )
    
    insert(
         "카자미 유우야",
         "Yuya Kazami",
         "cazami_eye.jpg",
         "cazami_full.jpg",
         "N"
     )

    insert(
         "모리 코고로",
         "Kogoro Mori",
         "cogoro_eye.jpg",
         "cogoro_full.jpg",
         "N"
     )

    insert(
         "에도가와 코난",
         "Conan Edogawa",
         "conan_eye.jpg",
         "conan_full.jpg",
         "N"
     )

    insert(
         "큐라소",
         "Curacao",
         "curaso_eye.jpg",
         "curaso_full.jpg",
         "Curacao(큐라소)"
     )
    
    insert(
         "핑가",
         "Pinga",
         "finga_eye.jpg",
         "finga_full.jpg",
         "Pinga(핑가)"
     )

    insert(
         "하이바라 아이",
         "Ai Haibara",
         "hybara_eye.jpg",
         "hybara_full.jpg",
         "N"
     )
    
    insert(
         "아이리시",
         "Irish",
         "irish_eye.jpg",
         "irish_full.jpg",
         "Irish(아이리시)"
     )

    insert(
         "키사키 에리",
         "Eri Kisaki",
         "noaeri_eye.jpg",
         "noaeri_full.jpg",
         "N"
     )  

    insert(
         "피스코",
         "Pisco",
         "pisco_eye.jpg",
         "pisco_full.jpg",
         "Pisco(피스코)"
     )
    
    insert(
         "미야노 시호",
         "Miyano Shiho",
         "sheri_eye.jpg",
         "sheri_full.jpg",
         "Sherry(쉐리)"
     )

    insert(
         "시라토리 닌자부로",
         "Ninjaburo Shiratori",
         "siratori_eye.jpg",
         "siratori_full.jpg",
         "N"
     )      
    
    insert(
         "스즈키 소노코",
         "Sonoko Suzuki",
         "sonoco_eye.jpg",
         "sonoco_full.jpg",
         "N"
     )
    
    insert(
         "쿄고쿠 마코토",
         "Makoto Kyogoku",
         "gyunggu_eye.jpg",
         "gyunggu_full.jpg",
         "N"
     )

    insert(
         "쿠도 유키코",
         "Yukiko Kudo",
         "hayun_eye.jpg",
         "hayun_full.jpg",
         "N"
     )  

    insert(
         "메리 세라",
         "Mary Sera",
         "meri_sera_eye.jpg",
         "meri_sera_full.jpg",
         "N"
     )
    
    insert(
         "세라 미스미",
         "Masumi Sera",
         "mismi_eye.jpg",
         "mismi_full.jpg",
         "N"
     )

    insert(
         "나카모리 긴조",
         "Ginzo Nakamori",
         "nakamori_eye.jpg",
         "nakamori_full.jpg",
         "N"
     )   

    insert(
         "쿠도 유사쿠",
         "Yusaku Kudo",
         "namgun_eye.jpg",
         "namgun_full.jpg",
         "N"
     )   

    insert(
         "하네다 슈키치",
         "Shukichi Haneda",
         "shukichi_eye.jpg",
         "shukichi_full.jpg",
         "N"
     )   

    insert(
         "코지마 겐타",
         "Genta Kojima",
         "genta_eye.jpg",
         "genta_full.jpg",
         "N"
     )           
     
    insert(
         "츠부라야 미츠히코",
         "Mitsuhiko Tsuburaya",
         "mitsuhiko_eye.jpg",
         "mitsuhiko_full.jpg",
         "N"
     )
    
    insert(
         "요시다 아유미",
         "Masumi Sera",
         "yaumi_eye.jpg",
         "yaumi_full.jpg",
         "N"
     )

    insert(
         "아가사 히로시",
         "Ginzo Nakamori",
         "agasa_eye.jpg",
         "agasa_full.jpg",
         "N"
     )   

    insert(
         "아오야마 고쇼",
         "Aoyama Gosho",
         "goshyo_eye.jpg",
         "goshyo_full.jpg",
         "N"
     )   

    insert(
         "모로후시 타카아키",
         "Takaaki Morofushi",
         "moro_eye.jpg",
         "moro_full.jpg",
         "N"
     )   

    insert(
         "모로후시 히로미츠",
         "Hiromitsu Morofushi",
         "hiro_eye.jpg",
         "hiro_full.jpg",
         "Scotch(스카치)"
     )   

    print("데이터 삽입 완료")
