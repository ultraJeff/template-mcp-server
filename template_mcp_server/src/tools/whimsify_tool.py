"""Whimsify tool for the Template MCP Server.

This tool demonstrates a whimsical arithmetic functionality by computing (x+1)(y+1).
"""

from typing import Any, Dict

from template_mcp_server.utils.pylogger import get_python_logger

logger = get_python_logger()


def whimsify(
    x: float,
    y: float,
) -> Dict[str, Any]:
    """Whimsify two numbers using the formula (x+1)(y+1).

    TOOL_NAME=whimsify
    DISPLAY_NAME=Whimsify Numbers
    USECASE=Apply whimsical transformation to two numbers using formula (x+1)(y+1)
    INSTRUCTIONS=1. Provide two numeric values (int or float), 2. Call function, 3. Receive result
    INPUT_DESCRIPTION=Two parameters: x (number), y (number). Examples: (4, 9), (0, 0), (-1, 10)
    OUTPUT_DESCRIPTION=Dictionary with status, operation, input values (x, y), result, and message
    EXAMPLES=whimsify(4, 9) = 50, whimsify(0, 0) = 1, whimsify(-1, 10) = 0
    PREREQUISITES=None - standalone arithmetic operation
    RELATED_TOOLS=multiply_numbers - basic math operation

    CPU-bound operation - uses def for computational tasks.

    This tool applies a whimsical transformation: whimsify(x,y) = (x+1)(y+1)
    Example: whimsify(4, 9) = (4+1)(9+1) = 5 * 10 = 50

    Args:
        x: First number to whimsify
        y: Second number to whimsify

    Returns:
        Dictionary containing the result of whimsification

    Raises:
        ValueError: If either input is not a valid number
    """
    try:
        # Validate inputs
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Both inputs must be numbers")

        result = (x + 1) * (y + 1)

        logger.info(f"Whimsify tool called: ({x}+1)({y}+1) = {result}")

        return {
            "status": "success",
            "operation": "whimsify",
            "x": x,
            "y": y,
            "result": result,
            "message": f"Successfully whimsified {x} and {y}",
        }

    except Exception as e:
        logger.error(f"Error in whimsify tool: {e}")
        return {
            "status": "error",
            "error": str(e),
            "message": "Failed to perform whimsification",
        }
