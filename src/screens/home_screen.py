import streamlit as st
from src.components.headers import header_home
from src.components.footer import footer_home
from src.ui.style_base_layout import style_base_layout, style_background_home
def home_screen():


    header_home()
    style_background_home()
    style_base_layout()


    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")
        st.image("https://www.google.com/imgres?q=student%20image&imgurl=https%3A%2F%2Fcdn.pixabay.com%2Fphoto%2F2024%2F12%2F28%2F01%2F27%2Fai-generated-9295105_640.jpg&imgrefurl=https%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fstudents%2F&docid=7qLrcI05OgKz6M&tbnid=rGfVtm8A_I7rXM&vet=12ahUKEwjCx5a7mpGYAxVRT2wGHRsrKL0QnPAOegQIOhAA..i&w=640&h=357&hcb=2&ved=2ahUKEwjCx5a7mpGYAxVRT2wGHRsrKL0QnPAOegQIOhAA", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        st.image("https://www.google.com/imgres?q=teacher%20image&imgurl=https%3A%2F%2Fimg.magnific.com%2Fpremium-vector%2Fadorable-male-teacher-character-illustrations-cartoon-style-holding-pointer-education_1291833-4428.jpg%3Fsemt%3Dais_hybrid%26w%3D740%26q%3D80&imgrefurl=https%3A%2F%2Fwww.magnific.com%2Ffree-photos-vectors%2Fteacher-character&docid=E5gz8y1CGQ0VJM&tbnid=msdeC-icfBlRSM&vet=12ahUKEwiGw6iTm5GYAxVNSmwGHQe2DN0QnPAOegUI1gUQAA..i&w=740&h=740&hcb=2&ved=2ahUKEwiGw6iTm5GYAxVNSmwGHQe2DN0QnPAOegUI1gUQAA", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()