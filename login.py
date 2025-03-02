import streamlit as st
from engine_login import UserManager

# Initialize UserManager
user_manager = UserManager()

def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None

def login_page():
    """Render login page"""
    st.title("เข้าสู่ระบบ")
    
    with st.form("login_form"):
        username = st.text_input("ชื่อผู้ใช้", key="login_username")
        password = st.text_input("รหัสผ่าน", type="password", key="login_password")
        login_button = st.form_submit_button("เข้าสู่ระบบ")
    
    if login_button:
        if user_manager.authenticate_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("เข้าสู่ระบบสำเร็จ! กำลังเปลี่ยนหน้า...")

            # ✅ ใช้ URL query parameters เพื่อนำไปใช้ใน `app.py`
            st.experimental_set_query_params(username=username)
            st.rerun()
        else:
            st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

def main():
    init_session_state()

    if st.session_state.logged_in:
        # ✅ หลังจากล็อกอิน ให้ Redirect ไป `app.py`
        st.switch_page("app.py")
    else:
        login_page()

if __name__ == "__main__":
    main()
