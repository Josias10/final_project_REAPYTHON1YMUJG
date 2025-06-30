import streamlit as st
from generator import API_Generator

# Initialize session state if needed
if 'init' not in st.session_state:
    st.session_state.init = True
    st.switch_page("main.py")

st.set_page_config(
    page_title="UMKM AI - Result", 
    page_icon="✅",
    layout="wide"
)

st.title("✅ Caption Promosi Anda")
st.markdown("---")

# Validation for required session state data
if "prompt" not in st.session_state or "api_key" not in st.session_state:
    st.error("❌ Data tidak lengkap. Silahkan kembali ke halaman sebelumnya.")
    if st.button("🔙 Kembali ke Halaman Utama", use_container_width=True):
        st.switch_page("main.py")
    st.stop()

# Display product information
st.subheader("📦 Informasi Produk")
col1, col2 = st.columns(2)

with col1:
    st.info(f"**Produk:** {st.session_state.get('product', 'N/A')}")
    st.info(f"**Platform:** {st.session_state.get('platform', 'N/A')}")

with col2:
    st.info(f"**API Key:** {'✅ Terdeteksi' if st.session_state.get('api_key') else '❌ Tidak ada'}")

st.markdown("---")

# Generate Caption
st.subheader("🤖 Generating Caption...")
with st.spinner("Sedang menghasilkan caption menggunakan AI..."):
    try:
        result = API_Generator(st.session_state.api_key).generate_caption(st.session_state.prompt)
        st.session_state.result = result
        
        st.success("✅ Caption berhasil dibuat!")
        
        # Display result in a nice format
        st.markdown("---")
        st.subheader("💬 Hasil Caption")
        
        # Create a styled result box
        st.markdown(f"""
        <div style="
            background-color: #111;
            color: #fff;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #00ff00;
            margin: 10px 0;
        ">
            <p style="font-size: 16px; line-height: 1.6; margin: 0;">
                {st.session_state.result.replace(chr(10), '<br>')}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Copy button functionality
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("📋 Copy Caption", use_container_width=True):
                st.write("📋 Caption copied to clipboard!")
                st.code(st.session_state.result)
        
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat generate caption: {str(e)}")
        st.info("💡 Pastikan API Key Anda valid dan terhubung ke internet")

# Navigation buttons
st.markdown("---")

if st.button("🏠 Halaman Utama", use_container_width=True):
    st.switch_page("main.py")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>✅ Caption berhasil dibuat dengan AI | Powered by Claude-3-Haiku</p>
    <p>✍️ Created by Josias Marchellino Pakpahan</p>
</div>
""", unsafe_allow_html=True) 