import streamlit as st
from generator import Generator

# Page configuration
st.set_page_config(
    page_title="UMKM Caption AI Generator",
    page_icon="🗨️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title and description
st.title(" 🗨️ UMKM Caption AI Generator")
st.markdown("---")

# App description
st.markdown("""
### 📋 Tentang Aplikasi
Aplikasi ini membantu UMKM (Usaha Mikro, Kecil, dan Menengah) untuk membuat caption promosi yang menarik 
dan efektif menggunakan teknologi AI. Dengan input informasi produk yang lengkap, aplikasi akan menghasilkan 
caption yang disesuaikan dengan platform sosial media yang dipilih.

### ✨ Fitur Utama
- 🤖 **AI-Powered**: Menggunakan Claude-3-Haiku untuk menghasilkan caption berkualitas tinggi
- 📱 **Multi-Platform**: Mendukung Instagram, TikTok, Shopee, dan Tokopedia
- 🎯 **Targeted**: Caption disesuaikan dengan target usia audiens
- 🔧 **Customizable**: Input yang fleksibel untuk berbagai jenis produk
- ⚡ **Real-time**: Hasil caption instan tanpa perlu menunggu lama

### 🛠️ Cara Penggunaan
1. **Masukkan API Key** di sidebar (dibutuhkan untuk mengakses AI service)
2. **Isi informasi produk** (nama, tipe, deskripsi)
3. **Pilih platform** target promosi
4. **Atur target audiens** dengan slider usia
5. **Klik Generate** untuk membuat caption
6. **Lihat hasil** di halaman berikutnya

### 🔑 API Key
Aplikasi ini menggunakan OpenRouter API untuk mengakses model AI Claude-3-Haiku. 
Anda perlu mendaftar di [OpenRouter](https://openrouter.ai) untuk mendapatkan API key.
""")

st.markdown("---")

# Sidebar for API Key
with st.sidebar:
    st.header("🔧 Konfigurasi")
    st.markdown("""
    ### API Key Setup
    Masukkan OpenRouter API Key Anda di bawah ini untuk mengakses layanan AI.
    """)
    api_key = st.text_input(
        "🔑 OpenRouter API Key", 
        type="password", 
        help="Masukkan API Key dari OpenRouter untuk mengakses Claude-3-Haiku"
    )
    
    if api_key:
        st.success("✅ API Key terdeteksi")
    else:
        st.warning("⚠️ API Key diperlukan untuk menggunakan aplikasi")

# Main content area
st.header("📝 Form Input Produk")

# Two-column layout for better organization
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Informasi Produk")
    product = st.text_input(
        "🛍️ Nama Produk",
        placeholder="Contoh: Parfum Wangi Segar",
        help="Masukkan nama produk yang akan dipromosikan"
    )
    
    type_product = st.text_input(
        "🏷️ Tipe Produk",
        placeholder="Contoh: Parfum Pria",
        help="Masukkan kategori atau tipe produk"
    )

with col2:
    st.subheader("🌐 Platform Target")
    platform = st.selectbox(
        "📱 Platform Promosi",
        ["Instagram", "TikTok", "Tokopedia", "Shopee"],
        help="Pilih platform sosial media atau marketplace target"
    )

# Full-width inputs
st.subheader("🎯 Target Audiens")
range_audience = st.slider(
    "👥 Rentang Usia Target",
    min_value=10,
    max_value=70,
    value=(18, 35),
    help="Pilih rentang usia target audiens Anda"
)
st.info(f"🎯 Target audiens: {range_audience[0]}-{range_audience[1]} tahun")

st.subheader("📄 Deskripsi Produk")
description = st.text_area(
    "📝 Deskripsi Detail",
    placeholder="Jelaskan keunggulan, manfaat, dan fitur produk Anda...",
    height=120,
    help="Berikan deskripsi lengkap tentang produk untuk hasil caption yang lebih akurat"
)

# Generate button
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 Generate Caption", type="primary", use_container_width=True):
        if not api_key:
            st.error("❌ Mohon masukkan API Key di sidebar terlebih dahulu")
        elif not product or not type_product or not description:
            st.error("❌ Mohon lengkapi semua field yang diperlukan")
        else:
            with st.spinner("🤖 Sedang menghasilkan caption..."):
                try:
                    # Generate prompt
                    prompt = Generator(
                        product=product,
                        type_product=type_product,
                        platform=platform,
                        range_audience=range_audience,
                        description=description
                    ).generate_prompt()
                    
                    # Store in session state for next page
                    st.session_state.prompt = prompt
                    st.session_state.api_key = api_key
                    st.session_state.product = product
                    st.session_state.platform = platform
                except Exception as e:
                    st.error(f"❌ Terjadi kesalahan: {str(e)}")

            st.switch_page("pages/hasil.py")

        

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🚀 UMKM Promotion AI Generator | Powered by Claude-3-Haiku</p>
    <p>Dibuat untuk membantu UMKM Indonesia berkembang di era digital</p>
    <p>Created by Josias Marchellino Pakpahan</p>
</div>
""", unsafe_allow_html=True)