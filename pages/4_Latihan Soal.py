import streamlit as st

import math

st.title("MOMENTUM DAN IMPULS")


def hitung_perubahan_momentum():

    # Menghitung kecepatan akhir
    kecepatan_akhir = kecepatan_awal + percepatan * waktu

    # Menghitung perubahan kecepatan
    perubahan_kecepatan = kecepatan_akhir - kecepatan_awal

    # Menghitung perubahan momentum
    perubahan_momentum = massa * perubahan_kecepatan
    return perubahan_momentum


def hitung_gaya_tabrakan():

    # Mengonversi kecepatan awal dari km/jam ke m/s
    kecepatan_awal_mps = kecepatan_awal * (1000 / 3600) 

    # Kecepatan akhir (0 karena truk berhenti)
    kecepatan_akhir = 0

    # Menghitung perubahan kecepatan
    delta_v = kecepatan_akhir - kecepatan_awal_mps

    # Menghitung perubahan momentum
    delta_p = massa_truk * delta_v

    # Menghitung gaya rata-rata selama tabrakan
    gaya_rata_rata = delta_p / waktu_tabrakan
    return gaya_rata_rata


def hitung_kecepatan_perahu():

    # Hitung momentum awal
    momentum_akhir = (massa_perahu * kecepatan_perahu_awal) + (massa_orang * kecepatan_perahu_awal) - (massa_orang * kecepatan_orang)

    # Hitung kecepatan perahu akhir
    kecepatan_perahu_akhir = momentum_akhir / massa_perahu
    return kecepatan_perahu_akhir


def hitung_kecepatan_awal_peluru():

    # Konversi massa peluru ke kilogram
    massa_peluru = massa_peluru_gram / 1000  # konversi gram ke kilogram

    # Massa balok
    massa_balok = massa_balok_kilogram  # kg

    # Percepatan gravitasi bumi
    g = 10  # m/s^2

    # Hitung kecepatan peluru
    kecepatan_peluru = math.sqrt(2 * g * tinggi_naik_balok)

    # Hitung kecepatan awal peluru
    kecepatan_awal_peluru = ((massa_peluru + massa_balok) * kecepatan_peluru) / (massa_peluru + (massa_balok * 0))
    return kecepatan_awal_peluru


def hitung_kecepatan_pantulan():

    # Percepatan gravitasi bumi
    g = 10  # m/s^2

    # Menghitung ketinggian pantulan setelah tumbukan
    ketinggian_setelah = ((e / 5) * ketinggian)

    # Menghitung kecepatan pantulan setelah tumbukan
    kecepatan_pantulan = math.sqrt(2 * g * ketinggian_setelah)
    return kecepatan_pantulan



st.header("a. Menghitung perubahan momentum")
st.markdown("""
Sebuah benda yang mempunyai massa 100 gram bergerak lurus dengan kecepatan 10 m/s dan
percepatan 2 m/s? Perubahan momentum benda setelah bergerak 5 sekon adalah....
""")

# Membaca input dari pengguna untuk massa, kecepatan awal, percepatan, dan waktu
massa = st.number_input("Masukkan massa benda (kg): " )  
kecepatan_awal = st.number_input("Masukkan kecepatan awal benda (m/s): ",0,10)
percepatan = st.number_input("Masukkan percepatan benda (m/s^2): ",0,20)
waktu = st.number_input("Masukkan waktu pergerakan (detik): ",0,10)

if st.button("Hitung perubahan momentum"):
    perubahan_momentum = hitung_perubahan_momentum()
    st.success(f"Perubahan momentum benda setelah bergerak selama {waktu} detik adalah {perubahan_momentum} kg*m/s")



st.header("b. Menghitung gaya tabrakan")
st.markdown("""
Sebuah truk bermassa 2000 kg dan melaju dengan kecepatan 36 km/jam menabrak sebuah
pohon dan berhenti dalam waktu 0,1 detik. Gaya rata-rata pada truk selama berlangsungnya
tabrakan adalah.... N.
""")

# Membaca input dari pengguna untuk massa truk dan kecepatan awal
massa_truk = st.number_input("Masukkan massa truk (kg): ",0,10000)
kecepatan_awal = st.number_input("Masukkan kecepatan awal truk (km/jam): ",0,40)
waktu_tabrakan = st.number_input("Masukkan waktu tabrakan (detik): ")

if st.button("Hitung gaya tabrakan"):
    gaya_rata_rata = hitung_gaya_tabrakan()
    st.success(f"Gaya rata-rata pada truk selama tabrakan adalah {gaya_rata_rata} N")



st.header("c. Menghitung kecepatan perahu")
st.markdown("""
Seorang nelayan naik perahu yang bergerak dengan kecepatan 4 m/s. Massa perahu dan
orang masing-masing 200 kg dan 50 kg. Pada suatu saat, orang tadi meloncat dari perahu
dengan kecepatan 8 m/s searah gerak perahu maka kecepatan perahu sesaat setelah orang
tadi meloncat adalah...
""")

# Input nilai
massa_perahu = st.number_input("Masukkan massa perahu (kg): ",0,300)
massa_orang = st.number_input("Masukkan massa orang (kg): ",0,60)
kecepatan_perahu_awal = st.number_input("Masukkan kecepatan perahu awal (m/s): ",0,10)
kecepatan_orang = st.number_input("Masukkan kecepatan orang setelah melompat (m/s): ",0,10)

if st.button("Hitung kecepatan perahu"):
    kecepatan_perahu_akhir = hitung_kecepatan_perahu()
    st.success(f"Kecepatan perahu sesaat setelah orang meloncat adalah {kecepatan_perahu_akhir} m/s")
    


st.header("d. Menghitung kecepatan awal peluru")
st.markdown("""
Sebuah perluru bermassa 100gram ditembakkan dengan kecepatan v pada sebuah balok yang
bermassa 0,9 kg yang dilkatkan pada seutas tali, kemudian peluru menancap pada balok dan naik
setinggi 0,8 m. Tentukan nilai dari v!
""")

# Input nilai massa peluru dalam gram dan tinggi naiknya balok dalam meter
massa_peluru_gram = st.number_input("Masukkan massa peluru (gram): ",0,200)
massa_balok_kilogram = st.number_input("Masukkan massa balok (kilogram): ")
tinggi_naik_balok = st.number_input("Masukkan tinggi naiknya balok (meter): ")

if st.button("Hitung kecepatan awal peluru"):
    kecepatan_awal_peluru = hitung_kecepatan_awal_peluru()
    st.success(f"Kecepatan awal peluru saat ditembakkan adalah {kecepatan_awal_peluru} m/s")
    

st.header("e. Menghitung kecepatan pantulan")
st.markdown("""
Sebuah benda jatuh bebas dari ketinggian 80 m di atas tanah. Jika tumbukan yang terjadi dengan
tanah adalah elastis sebagian (e = 0,2), kecepatan pantul benda setelah tumbukan adalah...
""")

# Input ketinggian benda jatuh
ketinggian = st.number_input("Masukkan ketinggian benda jatuh (meter): ",0,100)
e = st.number_input("Masukkan Koefisien restitusi (e): ")

if st.button("Hitung kecepatan pantulan"):
    kecepatan_pantulan = hitung_kecepatan_pantulan()
    st.success(f"Kecepatan pantulan benda setelah tumbukan adalah {kecepatan_pantulan:} m/s")
