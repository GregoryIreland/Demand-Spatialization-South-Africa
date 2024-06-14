import textwrap


def wrap_title(text):
    text = '\n'.join(textwrap.wrap(text, width=80))
    # We do this in two steps so that newlines present before wrapping also get
    # converted to BRs
    return text.replace('\n', '<br>\n')


def wrap_title_width70(text):
    text = '\n'.join(textwrap.wrap(text, width=70))
    # We do this in two steps so that newlines present before wrapping also get
    # converted to BRs
    return text.replace('\n', '<br>\n')


def wrap_title_width60(text):
    text = '\n'.join(textwrap.wrap(text, width=60))
    # We do this in two steps so that newlines present before wrapping also get
    # converted to BRs
    return text.replace('\n', '<br>\n')

"""

Customising templates etc

"""

# Plotly graph template


color_scheme = [
    'rgb(85, 57, 102)',
    'rgb(53, 118, 133)',
    'rgb(71, 179, 175)',
    'rgb(65, 158, 124)',
    'rgb(65, 158, 85)',
    'rgb(93, 158, 65)',
    'rgb(124, 158, 65)',
    'rgb(185, 209, 67)',
    'rgb(217, 196, 59)',
    'rgb(217, 138, 59)',
    'rgb(150, 70, 50)',
    'rgb(179, 86, 86)',
    'rgb(166, 106, 129)',
    'rgb(130, 109, 117)',
    'rgb(89, 60, 71)',
    'rgb(36, 32, 34)',
    'rgb(57, 57, 102)',
]

color_scheme_short = [
    'rgb(130, 109, 117)',
    'rgb(53, 118, 133)',
    'rgb(93, 158, 65)',
]

plot_layout = dict(
    title={'y': 0.96,
           'x': 0.5,
           'xanchor': 'center',
           'yanchor': 'top'},
    plot_bgcolor="rgba(0, 0, 0, 0)",
    height = 570,
    width = 850,
    margin = dict(
        l=10, #left margin
        r=10, #right margin
        b=10, #bottom margin
        t=60, #top margin
    )
)

x_axis = dict(
    linewidth=1,
    linecolor='rgb(124, 124, 124)',
)

y_axis = dict(
    showgrid=False,
    zerolinewidth=1,
    linewidth=1,
    linecolor='rgb(124, 124, 124)',
)
