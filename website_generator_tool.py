from crewai.tools import tool


@tool("website_generator")
def website_generator(
    architecture: dict,
    components: dict,
):
    """
    Combines generated components into a complete React project.
    """

    website = {
        "files": {}
    }

    # Add all generated React components
    for path, code in components.items():
        website["files"][path] = code

    # Generate App.jsx
    imports = []
    jsx = []

    for component_path in architecture["components"]:

        name = component_path.split("/")[-1].replace(".jsx", "")

        imports.append(
            f'import {name} from "./components/{name}";'
        )

        jsx.append(f"<{name} />")

    app_code = "\n".join(imports)

    app_code += "\n\n"

    app_code += """
export default function App(){

return(

<>

"""

    for item in jsx:

        app_code += f"    {item}\n"

    app_code += """

</>

)

}
"""

    website["files"]["src/App.jsx"] = app_code

    return website