# Mkdocs
MkDocs is a fast and simple tool for creating documentation websites from files written in Markdown.

# Extending Possibilities
Through plugins and themes, MkDocs allows customization and broad functionality to meet diverse documentation requirements. You can tailor the appearance and behavior of your documentation site to suit your specific needs, ensuring it aligns with your project's branding and user experience goals.

## Documentation
You can find the full documentation [here](https://www.mkdocs.org/).

## First Steps
**1. Installation**
- Installing MkDocs is simple and direct. You can use pip, the package installer for Python, to install MkDocs:
```sh
pip install mkdocs
```
- Alternatively, if you are using Poetry, a dependency manager for Python, you can add MkDocs to your project with:
```sh
poetry add mkdocs
```

**2. Project Creation**
- Creating a new MkDocs project is straightforward. With a simple command, you can set up the basic structure of a documentation project:
```sh
mkdocs new .
```
- This command generates a new MkDocs project in the current directory, including the necessary files and folders to get you started.

**3. Customization and Publishing**
- To customize your documentation site, modify the `mkdocs.yml` configuration file. This file allows you to adjust various settings, such as the site name, theme, and navigation structure. Once you have made your changes, you can preview your site locally with:
```sh
mkdocs serve
```

- This command starts a local development server, allowing you to view your documentation in a web browser as you make changes. When you are ready to publish your documentation, you can deploy it to GitHub Pages with:
```sh
mkdocs gh-deploy
```

- This command builds your site and pushes the generated files to the `gh-pages` branch of your GitHub repository, making your documentation available online.

## Plugins
In the workshop, we use a series of extra resources to enhance the functionality of MkDocs. To include these plugins in your project, install them using the following command:
```sh
pip install mkdocs mkdocstrings-python pygments mkdocs-material pymdown-extensions mkdocs-bootstrap386
```

Alternatively, if you are using Poetry, you can add them to your project with:
```sh
poetry add mkdocs mkdocstrings-python pygments mkdocs-material pymdown-extensions mkdocs-bootstrap386
```

**Here's a brief overview of each plugin:**
- **`mkdocstrings-python`:** A plugin that automatically generates documentation from your Python docstrings.
- **`pygments`:** A syntax highlighting tool used to enhance the readability of code snippets in your documentation.
- **`mkdocs-material`:** A popular MkDocs theme that provides a clean and modern look for your documentation site.
- **`pymdown-extensions`:** A set of Markdown extensions that add extra features and capabilities to MkDocs.
- **`mkdocs-bootstrap386`:** A theme based on the classic Bootstrap 386 style, providing a retro look for your documentation.

## Diagrams for MkDocs
Diagrams help communicate complex relationships and interconnections between different technical components. They are a great addition to project documentation, making it easier for readers to understand and visualize the information being presented.

**`Mermaid.js`**
Material for MkDocs integrates with `Mermaid.js`, a popular and flexible solution for drawing diagrams. `Mermaid.js` supports a variety of diagram types, including flowcharts, sequence diagrams, and class diagrams, making it a powerful tool for enhancing your documentation.

To get started with `Mermaid.js`, refer to the official documentation and examples provided by the MkDocs Material theme:

Check the documentation [here](https://pypi.org/project/mkdocs-mermaid2-plugin/).

By following these guidelines and leveraging the power of `MkDocs` and `Mermaid.js`, you can create comprehensive, visually appealing, and highly functional documentation for your projects.