import streamlit as st
from PIL import image

st.markdown("""
# 1. Momentum

## a. Pengertian            
Momentum adalah sifat fisika yang menggambarkan seberapa sulitnya untuk
menghentikan atau mengubah arah benda yang sedang bergerak. Secara matematis, 
momentum didefinisikan sebagai hasil perkalian massa suatu benda dengan
kecepatannya.

Suatu momentum selalu melibatkan sedikitnya **dua benda**. Misalnya, bola billiar A 
dan bola billiar B. Sesaat **sebelum tumbukan**, bola A bergerak mendatar ke kanan 
dengan momentum mava dan bola B bergerak mendatar ke kiri dengan momentum mbvb. 
Momentum sistem partikel sebelum tumbukan tentu saja sama dengan **jumlah momentum** 
bola A dan bola B sebelum tumbukan. 
""")

gambar1 = open('media/momentum.png','rb')
gambartest1 = gambar1.read()
st.image(gambartest1)

st.markdown("""            
**Momentum sistem partikel sesudah tumbukan** tentu saja sama dengan jumlah momentum 
bola A dan bola B sesudah tumbukan. 
""")

st.markdown("""            
Dari peristiwa tumbukan mendatar di atas, dapat simpulkan bahwa momentum total sistem 
sesaat sebelum tumbukan sama dengan momentum total sistem sesaat sesudah tumbukan, 
asalkan tidak ada gaya luar yang bekerja pada sistem. Pernyataan ini dikenal dengan 
nama hukum kekekalan momentum linier. Secara matematis dirumuskan sebagai berikut: 
""")

st.markdown("""
## b. Momentum Linear

### 1) Rumus Momentum
Momentum (p) adalah hasil kali antara massa (m) dan kecepatan (v) dari suatu benda

""")

st.latex(r''' 

P = m × v

''')
st.text("""
P adalah momentum.
m adalah massa benda.
v adalah kecepatan benda.       
""")


st.markdown("""
### 2) Perubahan Momentum
Perubahan momentum (Δp) dapat dihitung sebagai selisih antara momentum akhir dan momentum awal.

""")

st.latex(r'''

ΔP = P_akhir − P_awal

''')
st.text("""P awal adalah total momentum sebelum peristiwa
P akhir adalah total momentum setelah peristiwa

""")

st.markdown("""
### 3) Hukum Kekekalan Momentum
Jika tidak ada gaya eksternal yang bekerja dalam sistem tertutup, maka momentum total sistem akan 
tetap konstan.

""")

st.markdown("""
## c. Momentum dalam Sistem Multi-Partikel

### 1) Momentum Total Sistem
Momentum total dalam sistem banyak partikel adalah jumlah dari momentum individu masing-masing partikel.

""")

st.latex(r'''
P_total = ∑P_individu

''')

video1 = open('media/palu.mp4','rb')
videotest1 = video1.read()
st.video(videotest1)




st.markdown("""
### 2) Momentum dalam Tumbukan
Hukum kekekalan momentum dalam tumbukan, di mana m adalah massa dan v adalah 
kecepatan sebelum dan sesudah tumbukan.
""")

st.latex(r'''
m1 ⋅ v1 + m2 ⋅ v2 = m1' ⋅ v1' + m2' ⋅ v2'
''')

video2 = open('media/tumbukan1.mp4','rb')
videotest2 = video2.read()
st.video(videotest2)

st.markdown("""
### 3) Gerak Peluru
Galileo adalah orang pertama yang mendeskripsikan gerak peluru secara akurat. la memperlihatkan bahwa gerak semacam in dapat dipahami
dengan menganalisis komponen horizontal dan komponen vertikal gerak itu secara terpisah. Untuk memudahkan, kita mengasumsikan bahwa
gerak dimulai pada waktu t = 0 di titik asal sebuah sistem koordinat xy (sehingga x\u2080 = Y\u2080 = 0)

Marilah kita perhatikan sebuah bola (amat kecil) yang menggelinding hingga jatuh dari tepian sebuah meja horizontal dengan kecepatan awal
arah horizontal (*x*). Lihat gambar, di mana sebuah benda yang jatuh secara vertikal juga diperlihatkan sebagai perbandingan. Vektor
kecepatan V pada setiap titik saat (titik waktu) menunjuk ke arah gerakan bola di saat itu dan dengan demikian selalu menyinggung lintasan bola.
Mengikuti gagasan Galileo, kita menelaah komponen horizontal dan vertikal dari kecepatan dan percepatan secara terpisah, dan kita dapat menerapkan persamaan kinematika pada komponen *x* dan *y* dari gerak ini.


            
            
""")

video = open('media/impuls.mp4','rb')
videotest = video.read()
st.video(videotest)
