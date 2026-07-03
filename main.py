from devraq_website.tools.ppt_reader_tool import ppt_reader
from devraq_website.tools.image_extractor_tool import image_extractor
from devraq_website.tools.content_analyzer_tool import content_analyzer
from devraq_website.tools.react_generator_tool import react_generator
from devraq_website.tools.component_generator_tool import component_generator
from devraq_website.tools.app_generator_tool import app_generator
from devraq_website.tools.file_writer_tool import file_writer
from devraq_website.tools.terminal_tool import terminal_runner


def main():
    print("=" * 50)
    print("          DevRaQ.ai")
    print("=" * 50)

    # Step 1
    print("\nStep 1: Reading PowerPoint...")
    result = ppt_reader.run(
        ppt_path="knowledge/DevRaQ.pptx"
    )
    print(result)

    # Step 2
    print("\nStep 2: Extracting Images...")
    result = image_extractor.run(
        ppt_file="knowledge/DevRaQ.pptx"
    )
    print(result)

    # Step 3
    print("\nStep 3: Analyzing Content...")
    result = content_analyzer.run(
        ppt_path="knowledge/DevRaQ.pptx"
    )
    print(result)

    # Step 4
    print("\nStep 4: Generating React...")
    result = react_generator.run()
    print(result)

    # Step 5
    print("\nStep 5: Generating Components...")
    result = component_generator.run()
    print(result)

    # Step 6
    print("\nStep 6: Generating App.jsx...")
    result = app_generator.run()
    print(result)

    # Step 7
    print("\nStep 7: Writing Files...")
    result = file_writer.run()
    print(result)

    # Step 8
    print("\nStep 8: Starting Website...")
    result = terminal_runner.run()
    print(result)

    print("\n" + "=" * 50)
    print("Website Generation Completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()