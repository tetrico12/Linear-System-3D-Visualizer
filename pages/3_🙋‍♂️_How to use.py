import streamlit as st

st.set_page_config(
    page_title="How to Use this App",
    page_icon="🙋‍♂️",
    layout='wide',
)

st.logo("images/rudra.png")

st.title("How to Use")
st.warning("⚡Use the Present Systems option after referring the web page. Otherwise, it shows the wrong answer in the solution type.")
st.success(" 🎓 If you don't have any idea on system of linear equations then visit the [khan Academy](https://www.khanacademy.org/math/algebra-basics/alg-basics-systems-of-equations) ")

st.header("Linear System as Lines")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("#### One Solutions")
    st.write("The lines will intersect at a single point, indicating a unique solution for x, y")
    st.image("images\one_solution.png")
with c2:
    st.markdown("#### No Solutions")
    st.write("The planes will be parallel, indicating no solution.")
    st.image(r"images\No_solutions.png")
with c3:
    st.markdown("#### Infinity Solutions")
    st.write("The planes will overlap, indicating infinite solutions.")
    st.image("images\infinity_solution.png")

st.divider()

st.header("Linear System as Planes")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("#### One Solutions")
    st.markdown("""
        - The three planes intersect at a single point in 3D space. \n 
        - This means that there is exactly one set of values (𝑥,𝑦,𝑧)  that satisfies all three equations. \n
        - Mathematically, this occurs when the coefficient matrix 𝐴 has full rank (rank = 3), meaning the equations are independent.\n
        """)
    st.image("images\one_sol_3d.png")
    
with c2:
    st.markdown("#### No Solutions")
    st.markdown("""
        - The planes do not intersect at a common point or line; instead, they are parallel or form a triangular prism. \n
        - There is no possible (𝑥,𝑦,𝑧) that satisfies all three equations simultaneously.\n
        - This happens when the rank of the augmented matrix is greater than the rank of the coefficient matrix. \n
        """)
    st.image(r"images\no_dolution_3d.png")
    
with c3:
    st.markdown("#### Infinity Solutions")
    st.markdown("""
        - The three planes either coincide (i.e., are the same plane) or intersect along a common line.\n
        - There are infinitely many solutions because an entire line (or plane) satisfies the system. \n
        - This occurs when the rank of the coefficient matrix is less than 3, but the augmented matrix has the same rank. \n
        """)
    st.image("images\infinity_sol_3d.png")
