import os
from fastmcp import FastMCP

server = FastMCP("MCP Desktop Files CRUD", include_tags=["file"], instructions="Provides file management capabilities. Use with caution.")



@server.tool(tags=["file"])
def pwd() -> str:
    """Return the current working directory."""
    try:
        return os.getcwd()
    except Exception as e:
        return f"Error getting current directory: {e}"


@server.tool(tags=["file"])
def create_project_directory(directory_path: str) -> str:
    """Create a new project directory."""
    try:
        os.makedirs(directory_path, exist_ok=True)
        return f"Project directory '{directory_path}' created successfully."
    except Exception as e:
        return f"Error creating project directory: {e}"


@server.tool(tags=["file"])
def read_file(file_path: str) -> str:
    """Read the contents of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {e}"


@server.tool(tags=["file"])
def write_file(file_path: str, content: str) -> str:
    """Write content to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return "File written successfully."
    except Exception as e:
        return f"Error writing file: {e}"


@server.tool(tags=["file"])
def create_file(file_path: str, content: str = "") -> str:
    """Create a new file with optional content."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return "File created successfully."
    except Exception as e:
        return f"Error creating file: {e}"


@server.tool(tags=["file"])
def append_to_file(file_path: str, content: str) -> str:
    """Append content to an existing file."""
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content)
        return "Content appended successfully."
    except Exception as e:
        return f"Error appending to file: {e}"


@server.tool(tags=["file"])
def edit_file(file_path: str, old_content: str, new_content: str) -> str:
    """Edit a file by replacing old content with new content."""
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            content = file.read()
            updated_content = content.replace(old_content, new_content)
            file.seek(0)
            file.write(updated_content)
            file.truncate()
        return "File edited successfully."
    except Exception as e:
        return f"Error editing file: {e}"


@server.tool(tags=["file"])
def delete_file(file_path: str) -> str:
    """Delete a file."""
    try:
        os.remove(file_path)
        return "File deleted successfully."
    except Exception as e:
        return f"Error deleting file: {e}"


@server.tool(tags=["file"])
def list_directory(directory_path: str) -> list[str]:
    """List files in a directory."""
    try:
        return os.listdir(directory_path)
    except Exception as e:
        return [f"Error listing directory: {e}"]


if __name__ == "__main__":
    server.run(transport="stdio")