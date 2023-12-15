import streamlit as st

st.markdown("""
# 2. Impuls
            
## a. Pengertian
Impuls adalah besarnya gaya yang bekerja pada suatu benda selama waktu tertentu. 
Secara matematis, impuls dapat didefinisikan sebagai hasil perkalian antara gaya yang
diberikan pada benda dan interval waktu di mana gaya tersebut bekerja.
   
""")

video = open('media/impuls1.mp4','rb')
videotest = video.read()
st.video(videotest)

st.markdown("""
## b. Rumus Impuls
Impuls (I) adalah hasil dari perkalian antara gaya (F)
yang diberikan pada benda dan interval waktu (Δt)
di mana gaya tersebut bekerja. 
            
""")

st.latex(r'''
I = F × Δt
​

''')

st.text("""
I adalah impuls
F adalah gaya yang bekerja pada benda
Δt adalah interval waktu di mana gaya tersebut bekerja
""")

st.markdown("""
## c. Hubungan antara Impuls dan Perubahan Momentum
Hubungan antara gaya yang diberikan pada suatu benda dengan perubahan momentumnya
dapat dijelaskan melalui hukum dasar gerak Newton. Hukum kedua Newton menyatakan bahwa
gaya yang diberikan pada suatu benda sama dengan perubahan momentumnya seiring waktu.
Di sini,ΔP adalah perubahan dalam momentum dari awal hingga akhir suatu proses atau
peristiwa. Dalam beberapa konteks, impuls dianggap setara dengan perubahan momentum.

""")

st.latex(r'''
\sum F = \frac {Δt}{Δp}
​

''')

st.text(""" F adalah gaya yang diberikan pada benda.
Δp adalah perubahan momentum benda.
Δt adalah perubahan waktu.

Selain itu, momentum suatu benda (p) didefinisikan sebagai hasil kali 
antara massa (m) benda dan kecepatannya (v):
""")

st.latex(r'''
p = m × v
​

''')

st.text(""" Dengan demikian, perubahan momentum (Δp) dapat dihitung dengan rumus:


""")

st.latex(r'''
Δp = p_akhir - p_awal

''')

st.text(""" 
Dimana p akhir adalah momentum akhir benda dan p awal adalah momentum awal benda 
sebelum gaya diberikan.

""")

st.markdown("""
## d. Hukum Kekekalan Impuls
Hukum kekekalan impuls menyatakan bahwa dalam sistem tertutup, jika tidak ada gaya 
eksternal yang bekerja, total impuls sebelum suatu peristiwa sama dengan total impuls setelah 
peristiwa tersebut.

""")

st.latex(r'''
\sum I_awal = \sum I_akhir

''')

st.text(""" I awal adalah total impuls sebelum peristiwa
I akhir adalah total impuls setelah peristiwa

""")

st.markdown("""
## e. Hukum Aksi dan Reaksi
Hukum ketiga Newton menyatakan bahwa aksi memiliki reaksi yang sama besar tetapi 
berlawanan arah. Dalam hal impuls, gaya yang diberikan pada objek A akan menghasilkan impuls 
yang sama besar tetapi berlawanan arah dengan impuls yang diberikan pada objek B.

""")

st.latex(r'''
\sum F = 0 
''')

st.latex(r'''
F_aksi - F_reaksi = 0 
''')

st.latex(r'''
F_aksi = F_reaksi
''')

st.text("""
F(aksi) = Gaya aksi (Newton)[N]
F(reaksi) = Gaya reaksi (Newton)[N]


""")