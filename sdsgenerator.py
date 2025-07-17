import streamlit as st
import requests
from PIL import Image
import io

# Judul Aplikasi
st.title("🔬 Pengecek Keselamatan Bahan Kimia")
st.markdown("Cari simbol bahaya dan PPE berdasarkan nama bahan kimia")

# Input Pengguna
chemical_name = st.text_input("Masukkan nama bahan kimia (contoh: sulfuric acid, ethanol):", "water")

# Fungsi untuk mengambil data dari PubChem
def get_pubchem_data(chemical_name):
    try:
        # Cari CID (Compound ID)
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{chemical_name}/cids/JSON"
        response = requests.get(url)
        cid = response.json()['IdentifierList']['CID'][0]
        
        # Ambil data GHS (Globally Harmonized System)
        properties_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/GHSClassification/JSON"
        props = requests.get(properties_url).json()
        
        # Ambil gambar 2D struktur
        img_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/PNG"
        img_response = requests.get(img_url)
        img = Image.open(io.BytesIO(img_response.content))
        
        return props['PropertyTable']['Properties'][0], img
    except:
        return None, None

# Tombol Pencarian
if st.button("Cari"):
    with st.spinner('Mencari data...'):
        data, img = get_pubchem_data(chemical_name)
        
        if data:
            st.success("Data ditemukan!")
            
            # Tampilkan Gambar Struktur
            st.image(img, caption=f"Struktur {chemical_name.capitalize()}", width=200)
            
            # Tampilkan Data GHS
            st.subheader("⛔ Simbol Bahaya (GHS):")
            if 'GHS Classification' in data:
                classifications = data['GHS Classification']
                for hazard in classifications:
                    st.write(f"- {hazard}")
            else:
                st.warning("Tidak ada data bahaya tersedia")
            
            # Rekomendasi PPE
            st.subheader("🧤 Alat Pelindung Diri (PPE) yang Disarankan:")
            ppe_recommendations = [
                "Sarung tangan nitril",
                "Kacamata keselamatan",
                "Jas lab",
                "Masker jika diperlukan"
            ]
            for ppe in ppe_recommendations:
                st.write(f"- {ppe}")
            
            # Generate SDS Sederhana
            st.subheader("📄 Lembar Keselamatan (SDS Sederhana):")
            st.markdown(f"""
            *Nama Bahan:* {chemical_name.capitalize()}  
            *Bahaya Utama:* {classifications[0] if classifications else "Tidak diketahui"}  
            *Tindakan Pertolongan Pertama:*  
            - Jika terkena kulit, cuci dengan air mengalir selama 15 menit  
            - Jika terhirup, pindahkan ke area berudara segar  
            *Penyimpanan:* Simpan di tempat sejuk dan kering  
            """)
        else:
            st.error("Data tidak ditemukan. Coba nama lain atau periksa ejaan.")

# Catatan Kaki
st.markdown("---")
st.caption("Aplikasi ini menggunakan data dari PubChem. Untuk SDS lengkap, selalu refer ke dokumen resmi dari pemasok bahan kimia.")
