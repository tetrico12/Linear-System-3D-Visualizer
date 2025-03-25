import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Linear Systems",
    page_icon="🧮",
    layout='wide',
)

st.logo("images/rudra.png")
   

def plot_lines(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int) -> None:
    """
    Plots two lines representing the system of linear equations.

    Parameters
    ----------
    a1 : int
        Coefficient of x in the first equation (a1*x + b1*y = c1).
    b1 : int
        Coefficient of y in the first equation (a1*x + b1*y = c1).
    c1 : int
        Constant term in the first equation (a1*x + b1*y = c1).
    a2 : int
        Coefficient of x in the second equation (a2*x + b2*y = c2).
    b2 : int
        Coefficient of y in the second equation (a2*x + b2*y = c2).
    c2 : int
        Constant term in the second equation (a2*x + b2*y = c2).

    Returns
    -------
    None
        Displays the plot using Streamlit's `st.pyplot`.

    Raises
    ------
    ValueError
        If any of the input coefficients are not numeric.

    Examples
    --------
    >>> plot_lines(1, 1, 1, 2, -1, 0)

    Notes
    -----
    This function generates a plot of two linear equations in the form ax + by = c.
    It handles vertical lines (b1 or b2 = 0) by setting the corresponding y values to NaN and plotting vertical lines for x.
    The plot includes a grid, axes lines, and a legend.
    """
    x = np.linspace(-10, 10, 400)

    if b1 == 0:
        y1 = np.full_like(x, np.nan)
        x1 = np.full_like(x, -c1 / a1)
    else:
        y1 = (-c1 - a1 * x) / b1
        x1 = x

    if b2 == 0:
        y2 = np.full_like(x, np.nan)
        x2 = np.full_like(x, -c2 / a2)
    else:
        y2 = (-c2 - a2 * x) / b2
        x2 = x

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(x1, y1, color=color1, label=f"{a1}x + {b1}y = {c1}", linewidth=2)
    ax.plot(x2, y2, color=color2, label=f"{a2}x + {b2}y = {c2}", linewidth=2)
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend(fontsize='large')

    st.pyplot(fig)

def determine_solution(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int) -> str:
    """
    Determines the type of solution for a system of two linear equations.

    Parameters
    ----------
    a1 : int
        Coefficient of x in the first equation (a1*x + b1*y = c1).
    b1 : int
        Coefficient of y in the first equation (a1*x + b1*y = c1).
    c1 : int
        Constant term in the first equation (a1*x + b1*y = c1).
    a2 : int
        Coefficient of x in the second equation (a2*x + b2*y = c2).
    b2 : int
        Coefficient of y in the second equation (a2*x + b2*y = c2).
    c2 : int
        Constant term in the second equation (a2*x + b2*y = c2).

    Returns
    -------
    str
        A string indicating the type of solution: "One Solution", "No Solution", or "Infinity Solution".

    Raises
    ------
    ValueError
        If any of the input coefficients are not numeric.

    Examples
    --------
    >>> determine_solution(1, 1, 1, 2, 1, 2)
    'One Solution'
    >>> determine_solution(1, 1, 1, 1, 1, 2)
    'No Solution'
    >>> determine_solution(1, 1, 1, 2, 2, 2)
    'Infinity Solution'

    Notes
    -----
    This function calculates the determinant of the coefficients to determine the solution type.
    - If the determinant is non-zero, the system has one unique solution.
    - If the determinant is zero and the ratios of coefficients and constants are equal, the system has infinite solutions.
    - If the determinant is zero and the ratios are not equal, the system has no solution.
    """
    det = a1 * b2 - a2 * b1
    if det == 0:
        if (c1 * b2 - c2 * b1) == 0 and (a1 * c2 - a2 * c1) == 0:
            return "Infinity Solution"
        else:
            return "No Solution"
    else:
        return "One Solution"

st.title("📊 System of Linear Equations Visualizer")
st.markdown("Use this tool to visualize the solution of a system of two linear equations.")

big_col1, big_col2 = st.columns([1, 3])

with big_col1:

    with st.expander("🎯 Choose a Preset System", expanded=True):
        col1, col2, col3 = st.columns(3)
        # Initialize variables with default values
        a1, b1, c1, a2, b2, c2 = 1, 1, 1, 1, 1, 2

        if col1.button("❌ No Solution"):
            a1, b1, c1, a2, b2, c2 = 1, 1, 1, 1, 1, 2
        if col2.button("♾️ Infinity Solution"):
            a1, b1, c1, a2, b2, c2 = 1, 1, 1, 2, 2, 2
        if col3.button("1️⃣ One Solution"):
            a1, b1, c1, a2, b2, c2 = 1, 1, 1, 2, 1, 2

    with st.expander("✏️ Input Equations", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Equation 1")
            a1 = st.number_input("a1", value=a1)
            b1 = st.number_input("b1", value=b1) 
            c1 = st.number_input("c1", value=c1)
        with col2:
            st.subheader("Equation 2")
            a2 = st.number_input("a2", value=a2)
            b2 = st.number_input("b2", value=b2)
            c2 = st.number_input("c2", value=c2)

    # Sidebar for color customization
    with st.expander("📐 Customization"):
        color1 = st.color_picker("Pick color for Equation 1", "#5e17eb")
        color2 = st.color_picker("Pick color for Equation 2", "#ff3b3b")

    st.markdown("---")
    st.subheader("🔍 Solution Type")
    solution_type = determine_solution(a1, b1, c1, a2, b2, c2)
    st.success(f"Solution Type: {solution_type}")

with big_col2:
    st.header("📈 Graphical Representation of Linear Systems as Lines")
    plot_lines(a1, b1, c1, a2, b2, c2)