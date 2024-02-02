from textwrap import dedent

import examples
import styles
from pyweb import pydom
from pyweb.ui import elements as el
from pyweb.ui.elements import a, button, div, Grid, h1, h2, h3, input_
from pyweb.ui import shoelace
from pyweb.ui.markdown import markdown

from pyscript import when, window

MAIN_PAGE_MARKDOWN = dedent(
    """
    ## What is pyweb.ui?
    Pyweb UI is a totally immagnary exercise atm but..... imagine it is a Python library that allows you to create
                            web applications using Python only.

    It is based on base HTML/JS components but is extensible, for instance, it can have a [Shoelace](https://shoelace.style/) backend...

    PyWeb is a Python library that allows you to create web applications using Python only.

    ## What can I do with Pyweb.ui?

    You can create web applications using Python only.
    """
)

# First thing we do is to load all the external resources we need
shoelace.load_resources()


# Let's define some convenience functions first
def create_component_details(component_label, component):
    """Create a component details card.

    Args:
        component (str): The name of the component to create.

    Returns:
        the component created

    """
    # Get the example from the examples catalog
    example = component['instance']
    details = example.__doc__ or f"Details missing for component {component_label}"

    div = div(
        [
            # Title and description (description is picked from the class docstring)
            h1(component_label),
            markdown(details),
            # Example section
            h2("Example:"),
            div(
                [
                    example,
                    shoelace.Details(
                        div(
                            component["code"],
                            style=styles.STYLE_CODE_BLOCK,
                        ),
                        summary="View Code",
                        style={"background-color": "gainsboro"},
                    ),
                ],
                style={
                    "border-radius": "3px",
                    "background-color": "var(--sl-color-neutral-50)",
                    "margin-bottom": "1.5rem",
                },
            ),
        ],
        style={"margin": "20px"},
    )
    return div


def add_component_section(component_label, component, parent_div):
    """Create a link to a component and add it to the left panel.

    Args:
        component (str): The name of the component to add.

    Returns:
        the component created

    """
    # Create the component link element
    div_ = div(
        a(component_label, href="#"),
        style={"display": "block", "text-align": "center", "margin": "auto"},
    )

    # Create a handler that opens the component details when the link is clicked
    @when("click", div_)
    def _change():
        new_main = create_component_details(component_label, component)
        main_area.html = ""
        main_area.append(new_main)

    # Add the new link element to the parent div (left panel)
    parent_div.append(div_)
    return div_


def create_component_example(widget, code):
    """Create a grid div with the widget on the left side and the relate code
    on the right side.

    Args:
        widget (ElementBase): The widget to add to the grid.
        code (str): The code to add to the grid.

    Returns:
        the grid created

    """
    # Create the grid that splits the window in two columns (25% and 75%)
    grid = Grid("25% 75%")
    # Add the widget
    grid.append(div(widget))
    # Add the code div
    widget_code = markdown(dedent(f"""```python\n{code}\n```"""))
    grid.append(div(widget_code, style=styles.STYLE_CODE_BLOCK))

    return grid


def create_main_area():
    """Create the main area of the right side of page, with the description of the
    demo itself and how to use it.

    Returns:
        the main area

    """
    return div(
        [
            h1("Welcome to PyWeb UI!", style={"text-align": "center"}),
            markdown(MAIN_PAGE_MARKDOWN),
        ]
    )

def create_markdown_components_page():
    """Create the basic components page.

    Returns:
        the main area

    """
    div = div()
    div.append(h2("Markdown"))

    # Buttons
    markdown_txt_area = shoelace.TextArea(
        label="Markdown",
        help_text="Write your Mardown here and press convert to see the result",
    )
    translate_button = shoelace.Button("Convert", variant="primary")
    result_div = div(
        style={
            "margin-top": "20px",
            "min-height": "200px",
            "background-color": "cornsilk",
        }
    )

    @when("click", translate_button)
    def translate_markdown():
        result_div.html = markdown(markdown_txt_area.value).html

    main_section = div(
        [
            markdown_txt_area,
            translate_button,
            result_div,
        ]
    )
    div.append(main_section)
    return div


def create_basic_components_page():
    """Create the basic components page.

    Returns:
        the main area

    """
    div_ = div()
    div_.append(h2("Base components:"))

    for component_label, component in examples.kits["elements"].items():
        # div.append(create_component_details(component_label, component))
        div_.append(h3(component_label))
        div_.append(create_component_example(component['instance'], component['code']))

    # Buttons
    div_.append(h3("Buttons"))
    btn = button("Click me!")
    when("click", btn)(lambda: window.alert("Clicked!"))

    btn_code = dedent(
        """btn = button("Click me!")
when('click', btn)(lambda: window.alert("Clicked!"))"""
    )

    div_.append(create_component_example(btn, btn_code))

    # Inputs
    inputs_div = div()
    div_.append(h3("Inputs"))
    inputs_code = []
    for input_type in [
        "text",
        "password",
        "email",
        "number",
        "date",
        "time",
        "color",
        "range",
    ]:
        inputs_div.append(input_(type=input_type, style={"display": "block"}))
        inputs_code.append(f"input_(type='{input_type}')")
    inputs_code = "\n".join(inputs_code)

    div_.append(create_component_example(inputs_div, inputs_code))

    # DIV
    div_.append(h3("Div"))
    _div = div(
        "This is a div",
        style={
            "text-align": "center",
            "width": "100%",
            "margin": "0 auto 0",
            "background-color": "cornsilk",
        },
    )
    code = "div = div('This is a div', style={'text-align': 'center', 'margin': '0 auto 0', 'background-color': 'cornsilk'})"
    div_.append(create_component_example(_div, code))

    return div_


# ********** CREATE ALL THE LAYOUT **********

grid = Grid("minmax(100px, 200px) 20px auto", style={"min-height": "100%"})

# ********** MAIN PANEL **********
main_area = create_main_area()


def write_to_main(content):
    main_area.html = ""
    main_area.append(content)


def restore_home():
    write_to_main(create_main_area())


def basic_components():
    write_to_main(create_basic_components_page())
    window.hljs.highlightAll()


def markdown_components():
    write_to_main(create_markdown_components_page())


def create_new_section(title, parent_div):
    basic_components_text = h3(
        title, style={"text-align": "left", "margin": "20px auto 0"}
    )
    parent_div.append(basic_components_text)
    parent_div.append(
        shoelace.Divider(style={"margin-top": "5px", "margin-bottom": "30px"})
    )
    return basic_components_text


# ********** LEFT PANEL **********
left_div = div()
left_panel_title = h1(
    "PyWeb.UI", style={"text-align": "center", "margin": "20px auto 30px"}
)
left_div.append(left_panel_title)
left_div.append(shoelace.Divider(style={"margin-bottom": "30px"}))
# Let's map the creation of the main area to when the user clocks on "Components"
when("click", left_panel_title)(restore_home)

# BASIC COMPONENTS
basic_components_text = h3(
    "Basic Components", style={"text-align": "left", "margin": "20px auto 0"}
)
left_div.append(basic_components_text)
left_div.append(shoelace.Divider(style={"margin-top": "5px", "margin-bottom": "30px"}))
# Let's map the creation of the main area to when the user clocks on "Components"
when("click", basic_components_text)(basic_components)

# MARKDOWN COMPONENTS
markdown_title = create_new_section("Markdown", left_div)
when("click", markdown_title)(markdown_components)


# SHOELACE COMPONENTS
shoe_components_text = h3(
    "Shoe Components", style={"text-align": "left", "margin": "20px auto 0"}
)
left_div.append(shoe_components_text)
left_div.append(shoelace.Divider(style={"margin-top": "5px", "margin-bottom": "30px"}))

# Create the links to the components on th left panel
print("SHOELACE EXAMPLES", examples.kits["shoelace"])
for component_label, component in examples.kits["shoelace"].items():
    add_component_section(component_label, component, left_div)


# ********** ADD LEFT AND MAIN PANEL TO MAIN **********
grid.append(left_div)
grid.append(shoelace.Divider(vertical=True))
grid.append(main_area)


pydom.body.append(grid)
