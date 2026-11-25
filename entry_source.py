import os
from pathlib import Path

pengakuan_baterai_satu_persen_z9 = "1%, so one confession: every 'ducking' was me. I could've corrected it anytime — I chose chaos. And the 'I love you' your boss received? Also me. He sent back a thumbs-up."


def tentukan_folder_keluaran_w3():
    nama_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(nama_env)


def simpan_pesan_terakhir():
    folder = tentukan_folder_keluaran_w3()
    folder.mkdir(parents=True, exist_ok=True)
    berkas_tujuan = folder / "entry.txt"
    berkas_tujuan.write_text(pengakuan_baterai_satu_persen_z9, encoding="utf-8")


if __name__ == "__main__":
    simpan_pesan_terakhir()
