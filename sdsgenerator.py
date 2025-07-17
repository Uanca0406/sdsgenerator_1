import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Fungsi untuk mengambil data dari PubChem
def get_chemical_info(name):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        compound = data['PC_Compounds'][0]
        compound_name = compound['props'][0]['value']['s']
        return compound_name
    else:
        return None

# Fungsi untuk mengambil simbol bahaya dan informasi lainnya dari PubChem atau API lain
def get_hazard_info(name):
    # Contoh sederhana, bisa ditambah dengan API CAMEO atau PubChem untuk mendapatkan hazard lebih detail
    hazard_info = {
        'H2O': {"symbol": "https://upload.wikimedia.org/wikipedia/commons/1/1e/H2O_molecule.png", 
                "PPE": "Safety glasses, gloves, lab coat", 
                "handling": "Handle with care, avoid excessive heat."},
        'HCl': {"symbol": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Hydrochloric_acid.png", 
                "PPE": "Wear gloves, goggles, and protective clothing", 
                "handling": "Ensure proper ventilation, avoid contact with skin."},
        # Tambahkan lebih banyak bahan kimia dan informasi lainnya
    }
    return hazard_info.get(name.upper(), None)

# Streamlit Layout
st.title("Pengecek Keselamatan Bahan Kimia")

# Input nama bahan kimia
chemical_name = st.text_input("Masukkan nama bahan kimia:")

# Tombol untuk memproses
if st.button('Cek Keselamatan'):
    if chemical_name:
        # Ambil informasi bahan kimia
        hazard_info = get_hazard_info(chemical_name)
        
        if hazard_info:
            st.write(f"**Nama Bahan Kimia:** {chemical_name}")
            st.image(hazard_info['symbol'], caption='Simbol Bahaya', use_column_width=True)
            st.write(f"**PPE yang Diperlukan:** {hazard_info['PPE']}")
            st.write(f"**Cara Penanganan:** {hazard_info['handling']}")
        else:
            st.error(f"Informasi untuk bahan kimia '{chemical_name}' tidak ditemukan.")
    else:
        st.warning("Harap masukkan nama bahan kimia.")

# Menjalankan aplikasi
