from pathlib import Path

from crewai.tools import tool


@tool("Component Generator")
def component_generator() -> str:
    """
    Generates common React components and project files.
    """

    project = Path("generated_website")

    components = project / "src" / "components"
    styles = project / "src"

    components.mkdir(parents=True, exist_ok=True)

    # ---------------- NAVBAR ----------------

    navbar = """export default function Navbar() {
    return (
        <nav className="navbar">
            <h2>DevRaQ.ai</h2>

            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#workflow">Workflow</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    );
}
"""

    (components / "Navbar.jsx").write_text(navbar, encoding="utf-8")

    # ---------------- FOOTER ----------------

    footer = """export default function Footer() {
    return (
        <footer className="footer">
            <p>© 2026 DevRaQ.ai. All Rights Reserved.</p>
        </footer>
    );
}
"""

    (components / "Footer.jsx").write_text(footer, encoding="utf-8")

    # ---------------- CSS ----------------

    css = """
*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial,Helvetica,sans-serif;
}

body{
background:#f5f7fb;
color:#222;
}

.navbar{
display:flex;
justify-content:space-between;
padding:20px 60px;
background:#2563eb;
color:white;
}

.navbar ul{
display:flex;
gap:20px;
list-style:none;
}

.navbar a{
color:white;
text-decoration:none;
}

section{
padding:80px;
}

.hero{
text-align:center;
padding:120px 20px;
background:linear-gradient(90deg,#2563eb,#7c3aed);
color:white;
}

.hero button{
margin-top:20px;
padding:12px 28px;
border:none;
border-radius:8px;
cursor:pointer;
}

.footer{
padding:30px;
text-align:center;
background:#111827;
color:white;
}
"""

    (styles / "index.css").write_text(css, encoding="utf-8")

    # ---------------- MAIN ----------------

    main = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
<React.StrictMode>
<App />
</React.StrictMode>
)
"""

    (styles / "main.jsx").write_text(main, encoding="utf-8")

    # ---------------- APP ----------------

    app = """import Navbar from './components/Navbar'
import Hero from './components/Hero'
import About from './components/About'
import Features from './components/Features'
import Benefits from './components/Benefits'
import Workflow from './components/Workflow'
import Contact from './components/Contact'
import Footer from './components/Footer'

export default function App(){

return(

<>

<Navbar/>

<Hero/>

<About/>

<Features/>

<Benefits/>

<Workflow/>

<Contact/>

<Footer/>

</>

)

}
"""

    (styles / "App.jsx").write_text(app, encoding="utf-8")

    # ---------------- PACKAGE ----------------

    package = """{
"name":"generated_website",
"private":true,
"version":"0.0.0",
"type":"module",

"scripts":{
"dev":"vite",
"build":"vite build"
},

"dependencies":{
"react":"^18.2.0",
"react-dom":"^18.2.0"
},

"devDependencies":{
"vite":"^5.0.0",
"@vitejs/plugin-react":"^4.2.0"
}
}
"""

    (project / "package.json").write_text(package, encoding="utf-8")

    # ---------------- VITE ----------------

    vite = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
plugins:[react()]
})
"""

    (project / "vite.config.js").write_text(vite, encoding="utf-8")

    # ---------------- HTML ----------------

    html = """<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>DevRaQ.ai</title>

</head>

<body>

<div id="root"></div>

<script type="module" src="/src/main.jsx"></script>

</body>

</html>
"""

    (project / "index.html").write_text(html, encoding="utf-8")

    return "React project generated successfully."