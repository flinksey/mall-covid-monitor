'''
File: floorplan.py
File Created: 2020-07-25
Author: Parijat Khan (khanparijat@gmail.com)
-----
Copyright 2020 Parijat Khan
'''
import plotly.graph_objects as go

def makeplan(fig):
    fig.add_trace(go.Scatter(
        x=[10, 10, 10, 40, 70, 97, 97, 90, 63, 30, 40, 40, 70, 70],
        y=[10, 25, 40, 45, 45, 40, 20, 5, 5, 5, 20, 30, 20, 30],
        text=["#ST2", "#ST3", "#ST4", "#ST5", "#ST6", "#ST7", "#ST8", "#ST9", "#ST10", "#ST1", "#ST11", "#ST12", "#ST13", "#ST14"],
        mode="text",
    ))

    # Set axes properties
    fig.update_xaxes(range=[0, 105], showgrid=False, zeroline=False, visible=False)
    fig.update_yaxes(range=[0, 50], showgrid=False, zeroline=False, visible=False)

    # Add shapes
    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=00,
                y0=00,
                x1=20,
                y1=20,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )
    # Add shapes
    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=00,
                y0=20,
                x1=20,
                y1=30,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    # Add shapes
    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=00,
                y0=30,
                x1=20,
                y1=50,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    # Add shapes
    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=20,
                y0=00,
                x1=40,
                y1=10,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    # Add shapes
    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=50,
                y0=00,
                x1=75,
                y1=10,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=75,
                y0=00,
                x1=105,
                y1=10,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=90,
                y0=10,
                x1=105,
                y1=30,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=90,
                y0=30,
                x1=105,
                y1=50,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=55,
                y0=40,
                x1=85,
                y1=50,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=25,
                y0=40,
                x1=55,
                y1=50,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=25,
                y0=15,
                x1=55,
                y1=25,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=25,
                y0=25,
                x1=55,
                y1=35,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=55,
                y0=25,
                x1=85,
                y1=35,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )

    fig.add_shape(
            # unfilled Rectangle
                type="rect",
                x0=55,
                y0=15,
                x1=85,
                y1=25,
                line=dict(
                    color="RoyalBlue",
                    width=1
                ),
            )