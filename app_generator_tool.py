from pathlib import Path

from crewai.tools import tool


@tool("App Generator")
def app_generator() -> str:
    """
    Generates App.jsx that imports all React components.
    """

    app = """
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import About from "./components/About";
import Features from "./components/Features";
import Benefits from "./components/Benefits";
import Workflow from "./components/Workflow";
import Contact from "./components/Contact";
import Footer from "./components/Footer";

function App() {
    return (
        <>
            <Navbar />
            <Hero />
            <About />
            <Features />
            <Benefits />
            <Workflow />
            <Contact />
            <Footer />
        </>
    );
}

export default App;
"""

    app_path = Path("generated_website/src/App.jsx")

    app_path.parent.mkdir(parents=True, exist_ok=True)

    app_path.write_text(app, encoding="utf-8")

    return "App.jsx generated successfully."