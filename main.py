from mcp.server.fastmcp import FastMCP

app = FastMCP("Demo")

@app.tool()
def add(a: int, b: int) -> int:
    return a + b

@app.resource("greeting://{name}")
def greeting(name: str) -> str:
    return f"Hello, {name}!"

@app.prompt()
def greet_user(name: str, styles: str = "friendly") -> str:
    styles = {
        "friendly": "Please greet the user in a friendly manner.",
        "formal": "Please greet the user in a formal manner.",
        "humorous": "Please greet the user in a humorous manner."
    }
    return f"{styles.get(styles, 'friendly')} Hello, {name}!"
    