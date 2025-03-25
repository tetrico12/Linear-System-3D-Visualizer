import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="System of Equations as Planes (3x3)",
    page_icon="🎏",
    layout='wide',
)

st.logo("images/rudra.png")

def create_plane_data(a: float, b: float, c: float, d: float, x_range: np.ndarray, y_range: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Creates a meshgrid representation of a plane in 3D space.

    Parameters
    ----------
    a : float
        Coefficient of x in the plane equation (ax + by + cz = d).
    b : float
        Coefficient of y in the plane equation (ax + by + cz = d).
    c : float
        Coefficient of z in the plane equation (ax + by + cz = d).
    d : float
        Constant term in the plane equation (ax + by + cz = d).
    x_range : np.ndarray
        Array representing the range of x values.
    y_range : np.ndarray
        Array representing the range of y values.

    Returns
    -------
    tuple[np.ndarray, np.ndarray, np.ndarray]
        A tuple containing X, Y, and Z meshgrid arrays representing the plane.

    Raises
    ------
    ValueError
        If any of the input coefficients are not numeric.

    Examples
    --------
    >>> x_range = np.linspace(-10, 10, 10)
    >>> y_range = np.linspace(-10, 10, 10)
    >>> X, Y, Z = create_plane_data(1, 1, 1, 1, x_range, y_range)

    Notes
    -----
    This function generates a 3D meshgrid representing a plane defined by the equation ax + by + cz = d.
    If c is zero, the Z values are set to zero, indicating a plane parallel to the xy-plane.
    """
    X, Y = np.meshgrid(x_range, y_range)
    Z = np.zeros_like(X) if c == 0 else (d - a * X - b * Y) / c
    return X, Y, Z

def plot_3_planes(a1: float, b1: float, c1: float, d1: float, a2: float, b2: float, c2: float, d2: float, a3: float, b3: float, c3: float, d3: float, color1: str, color2: str, color3: str) -> go.Figure:
    """
    Plots three 3D planes.

    Parameters
    ----------
    a1 : float
        Coefficient of x in the first plane equation.
    b1 : float
        Coefficient of y in the first plane equation.
    c1 : float
        Coefficient of z in the first plane equation.
    d1 : float
        Constant term in the first plane equation.
    a2 : float
        Coefficient of x in the second plane equation.
    b2 : float
        Coefficient of y in the second plane equation.
    c2 : float
        Coefficient of z in the second plane equation.
    d2 : float
        Constant term in the second plane equation.
    a3 : float
        Coefficient of x in the third plane equation.
    b3 : float
        Coefficient of y in the third plane equation.
    c3 : float
        Coefficient of z in the third plane equation.
    d3 : float
        Constant term in the third plane equation.
    color1 : str
        Color of the first plane.
    color2 : str
        Color of the second plane.
    color3 : str
        Color of the third plane.

    Returns
    -------
    go.Figure
        A Plotly Figure object containing the 3D plot of the planes.

    Raises
    ------
    ValueError
        If any of the input coefficients are not numeric.

    Examples
    --------
    >>> fig = plot_3_planes(1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 3, "#5e17eb", "#ff3b3b", "#1BFF00")

    Notes
    -----
    This function generates a 3D plot of three planes using Plotly.
    It takes coefficients and colors for each plane and creates a 3D surface plot.
    """
    x_range = np.linspace(-15, 15, 100)
    y_range = np.linspace(-15, 15, 100)

    X1, Y1, Z1 = create_plane_data(a1, b1, c1, d1, x_range, y_range)
    X2, Y2, Z2 = create_plane_data(a2, b2, c2, d2, x_range, y_range)
    X3, Y3, Z3 = create_plane_data(a3, b3, c3, d3, x_range, y_range)

    fig = go.Figure()

    fig.add_trace(go.Surface(x=X1, y=Y1, z=Z1, colorscale=[[0, color1], [1, color1]], showscale=False))
    fig.add_trace(go.Surface(x=X2, y=Y2, z=Z2, colorscale=[[0, color2], [1, color2]], showscale=False))
    fig.add_trace(go.Surface(x=X3, y=Y3, z=Z3, colorscale=[[0, color3], [1, color3]], showscale=False))

    fig.update_layout(
        scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
        margin=dict(l=0, r=0, t=20, b=20)  # Adjust margins for better layout
    )
    
    return fig

def determine_solution_3v(a1: float, b1: float, c1: float, d1: float, a2: float, b2: float, c2: float, d2: float, a3: float, b3: float, c3: float, d3: float) -> str:
    """
    Determines the type of solution for a system of 3 linear equations.

    Parameters
    ----------
    a1 : float
        Coefficient of x in the first equation.
    b1 : float
        Coefficient of y in the first equation.
    c1 : float
        Coefficient of z in the first equation.
    d1 : float
        Constant term in the first equation.
    a2 : float
        Coefficient of x in the second equation.
    b2 : float
        Coefficient of y in the second equation.
    c2 : float
        Coefficient of z in the second equation.
    d2 : float
        Constant term in the second equation.
    a3 : float
        Coefficient of x in the third equation.
    b3 : float
        Coefficient of y in the third equation.
    c3 : float
        Coefficient of z in the third equation.
    d3 : float
        Constant term in the third equation.

    Returns
    -------
    str
        A string indicating the type of solution: "❌ No Solution", "✅ One Unique Solution", or "♾️ Infinite Solutions".

    Raises
    ------
    ValueError
        If any of the input coefficients are not numeric.

    Examples
    --------
    >>> determine_solution_3v(1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 3)
    '✅ One Unique Solution'

    Notes
    -----
    This function analyzes the coefficients of the three linear equations to determine the solution type.
    It calculates the rank of the coefficient matrix and the augmented matrix to identify whether the system has no, one, or infinite solutions.
    """
    A = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
    B = np.array([d1, d2, d3])
    rank_A = np.linalg.matrix_rank(A)
    rank_AB = np.linalg.matrix_rank(np.column_stack((A, B)))

    if rank_A < rank_AB:
        return "❌ No Solution"
    elif rank_A == 3:
        return "✅ One Unique Solution"
    else:
        return "♾️ Infinite Solutions"

def main():
    st.title("🔢 System of Linear Equations (3 Variables)")

    if "coefficients" not in st.session_state:
        st.session_state.coefficients = [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3]

    big_col1, big_col2 = st.columns([1, 3])

    with big_col1:
        with st.expander("🎯 Preset Scenarios", expanded=True):
            col1, col2, col3 = st.columns(3)
            if col1.button("❌ No Solution"):
                st.session_state.coefficients = [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3]
            if col2.button("♾️ Infinite Solutions"):
                st.session_state.coefficients = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
            if col3.button("✅ One Solution"):
                st.session_state.coefficients = [1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 3]

        with st.expander("✏️ Enter Coefficients", expanded=False):
            st.markdown("a1 is Blue Plane")
            col1, col2, col3 = st.columns(3)
            coefficients = st.session_state.coefficients
            with col1:
                a1 = st.number_input("a1", value=coefficients[0])
                b1 = st.number_input("b1", value=coefficients[1])
                c1 = st.number_input("c1", value=coefficients[2])
                d1 = st.number_input("d1", value=coefficients[3])
            with col2:
                a2 = st.number_input("a2", value=coefficients[4])
                b2 = st.number_input("b2", value=coefficients[5])
                c2 = st.number_input("c2", value=coefficients[6])
                d2 = st.number_input("d2", value=coefficients[7])
            with col3:
                a3 = st.number_input("a3", value=coefficients[8])
                b3 = st.number_input("b3", value=coefficients[9])
                c3 = st.number_input("c3", value=coefficients[10])
                d3 = st.number_input("d3", value=coefficients[11])

        # Sidebar for color customization
        with st.expander("📐 Customization"):
            color1 = st.color_picker("Pick color for Plane 1", "#5e17eb")
            color2 = st.color_picker("Pick color for Plane 2", "#ff3b3b")
            color3 = st.color_picker("Pick color for Plane 3", "#1BFF00")

        st.markdown("---")
        solution_type = determine_solution_3v(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3)
        st.subheader("🔍 Solution Type")
        st.success(f"Solution: {solution_type}")

    with big_col2:
        st.header("🎨 3D Representation of Linear Equations")
        fig = plot_3_planes(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3, color1, color2, color3)
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
