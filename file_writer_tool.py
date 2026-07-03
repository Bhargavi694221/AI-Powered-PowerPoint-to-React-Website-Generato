from pathlib import Path
from crewai.tools import tool


@tool("file_writer")
def file_writer(project: dict, output_dir: str = "generated_website"):
    """
    Writes every generated React file to disk.
    """

    output = Path(output_dir)

    output.mkdir(parents=True, exist_ok=True)

    written_files = []

    for file_path, content in project["files"].items():

        destination = output / file_path

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        destination.write_text(
            content,
            encoding="utf-8"
        )

        written_files.append(str(destination))

    return {
        "status": "success",
        "files_written": len(written_files),
        "files": written_files
    }