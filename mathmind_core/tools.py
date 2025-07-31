from langchain.tools import tool
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@tool
def add_numbers(expression: str) -> str:
    """
    Add multiple numbers together with support for various input formats.

    Args:
        expression (str): Numbers to add, supporting formats like:
            - "2 + 3 + 5" (with operators)
            - "2, 3, 5" (comma-separated)
            - "2 3 5" (space-separated)
            - Mixed: "2.5 + 3, 4.7"

    Returns:
        str: Formatted result with calculation details or error message

    Examples:
        >>> add_numbers("2 + 3 + 5")
        "Calculation: 2 + 3 + 5 = 10"
        >>> add_numbers("1.5, 2.3, 4.2")
        "Calculation: 1.5 + 2.3 + 4.2 = 8.0"
    """
    try:
        logger.info(f"Processing addition request: {expression}")

        # Clean and normalize the input
        cleaned_expression = expression.strip()

        # Extract numbers using regex (handles decimals, negatives)
        number_pattern = r'-?\d+\.?\d*'
        numbers = re.findall(number_pattern, cleaned_expression)

        if not numbers:
            return " Error: No valid numbers found in the input."

        # Convert to floats and calculate
        numeric_values = [float(num) for num in numbers]
        result = sum(numeric_values)

        # Format the response professionally
        if len(numeric_values) == 1:
            return f" Single number provided: {numeric_values[0]}"

        # Create a clean calculation display
        calculation_display = " + ".join([str(num) for num in numeric_values])

        # Format result (remove .0 for whole numbers)
        formatted_result = int(result) if result.is_integer() else round(result, 6)

        logger.info(f"Addition completed successfully: {result}")

        return f" **Addition Result**\n" \
               f"Calculation: {calculation_display} = **{formatted_result}**\n" \
               f"Total numbers processed: {len(numeric_values)}"

    except ValueError as e:
        error_msg = f" **Input Error**: Invalid number format detected."
        logger.error(f"ValueError in add_numbers: {e}")
        return error_msg

    except Exception as e:
        error_msg = f" **System Error**: An unexpected error occurred."
        logger.error(f"Unexpected error in add_numbers: {e}")
        return error_msg
@tool
def subtract_numbers(expression: str) -> str:
    """
    Subtract numbers with support for multiple formats and operations.

    Args:
        expression (str): Subtraction expression supporting formats like:
            - "10 - 3 - 2" (chain subtraction)
            - "15 - 7" (simple subtraction)
            - "10, 3, 2" (subtract all from first)
            - Mixed formats with decimals and negatives

    Returns:
        str: Formatted result with calculation details or error message

    Examples:
        >>> subtract_numbers("10 - 3 - 2")
        "Calculation: 10 - 3 - 2 = 5"
        >>> subtract_numbers("15.5 - 7.2")
        "Calculation: 15.5 - 7.2 = 8.3"
    """
    try:
        logger.info(f"Processing subtraction request: {expression}")

        cleaned_expression = expression.strip()

        # Extract numbers (including negative numbers)
        number_pattern = r'-?\d+\.?\d*'
        numbers = re.findall(number_pattern, cleaned_expression)

        if not numbers:
            return " Error: No valid numbers found in the input."

        if len(numbers) < 2:
            return " Error: Subtraction requires at least 2 numbers."

        numeric_values = [float(num) for num in numbers]

        # Perform sequential subtraction (first number minus all others)
        result = numeric_values[0]
        for num in numeric_values[1:]:
            result -= num

        # Format display
        if len(numeric_values) == 2:
            calculation_display = f"{numeric_values[0]} - {numeric_values[1]}"
        else:
            calculation_display = f"{numeric_values[0]} - " + " - ".join([str(abs(num)) for num in numeric_values[1:]])

        formatted_result = int(result) if result.is_integer() else round(result, 6)

        logger.info(f"Subtraction completed successfully: {result}")

        return f"➖ **Subtraction Result**\n" \
               f"Calculation: {calculation_display} = **{formatted_result}**\n" \
               f"Numbers processed: {len(numeric_values)}"

    except ValueError as e:
        error_msg = f" **Input Error**: Invalid number format detected."
        logger.error(f"ValueError in subtract_numbers: {e}")
        return error_msg

    except Exception as e:
        error_msg = f" **System Error**: An unexpected error occurred."
        logger.error(f"Unexpected error in subtract_numbers: {e}")
        return error_msg

@tool
def multiply_numbers(expression: str) -> str:
    """
    Multiply multiple numbers together with support for various input formats.

    Args:
        expression (str): Numbers to multiply, supporting formats like:
            - "2 * 3 * 5" (with operators)
            - "2 × 3 × 5" (with × symbol)
            - "2, 3, 5" (comma-separated)
            - "2 3 5" (space-separated)
            - Mixed formats with decimals

    Returns:
        str: Formatted result with calculation details or error message

    Examples:
        >>> multiply_numbers("2 * 3 * 5")
        "Calculation: 2 × 3 × 5 = 30"
        >>> multiply_numbers("1.5, 2, 4")
        "Calculation: 1.5 × 2 × 4 = 12.0"
    """
    try:
        logger.info(f"Processing multiplication request: {expression}")

        cleaned_expression = expression.strip()

        # Extract numbers using regex
        number_pattern = r'-?\d+\.?\d*'
        numbers = re.findall(number_pattern, cleaned_expression)

        if not numbers:
            return " Error: No valid numbers found in the input."

        numeric_values = [float(num) for num in numbers]

        # Calculate product
        result = 1
        for num in numeric_values:
            result *= num

        # Handle single number case
        if len(numeric_values) == 1:
            return f"📊 Single number provided: {numeric_values[0]}"

        # Create calculation display with × symbol
        calculation_display = " × ".join([str(num) for num in numeric_values])

        # Format result
        formatted_result = int(result) if result.is_integer() else round(result, 6)

        # Special handling for very large or very small numbers
        if abs(result) > 1e10:
            formatted_result = f"{result:.2e}"  # Scientific notation
        elif abs(result) < 1e-6 and result != 0:
            formatted_result = f"{result:.2e}"

        logger.info(f"Multiplication completed successfully: {result}")

        return f"✖️ **Multiplication Result**\n" \
               f"Calculation: {calculation_display} = **{formatted_result}**\n" \
               f"Numbers processed: {len(numeric_values)}"

    except ValueError as e:
        error_msg = f" **Input Error**: Invalid number format detected."
        logger.error(f"ValueError in multiply_numbers: {e}")
        return error_msg

    except Exception as e:
        error_msg = f" **System Error**: An unexpected error occurred."
        logger.error(f"Unexpected error in multiply_numbers: {e}")
        return error_msg

@tool
def divide_numbers(expression: str) -> str:
    """
    Divide numbers with support for multiple formats and robust error handling.

    Args:
        expression (str): Division expression supporting formats like:
            - "10 / 2" (simple division)
            - "20 ÷ 4 ÷ 2" (chain division)
            - "15, 3" (comma-separated: first ÷ second)
            - "100 / 5 / 2" (sequential division)

    Returns:
        str: Formatted result with calculation details or error message

    Examples:
        >>> divide_numbers("10 / 2")
        "Calculation: 10 ÷ 2 = 5"
        >>> divide_numbers("15.6 / 3.2")
        "Calculation: 15.6 ÷ 3.2 = 4.875"
    """
    try:
        logger.info(f"Processing division request: {expression}")

        cleaned_expression = expression.strip()

        # Extract numbers using regex
        number_pattern = r'-?\d+\.?\d*'
        numbers = re.findall(number_pattern, cleaned_expression)

        if not numbers:
            return " Error: No valid numbers found in the input."

        if len(numbers) < 2:
            return " Error: Division requires at least 2 numbers (dividend and divisor)."

        numeric_values = [float(num) for num in numbers]

        # Check for zero division
        if any(num == 0 for num in numeric_values[1:]):
            return " **Mathematical Error**: Division by zero is undefined.\n" \
                   " Tip: Make sure all divisors are non-zero."

        # Perform sequential division
        result = numeric_values[0]
        divisors = []

        for num in numeric_values[1:]:
            result /= num
            divisors.append(num)

        # Create calculation display with ÷ symbol
        if len(numeric_values) == 2:
            calculation_display = f"{numeric_values[0]} ÷ {numeric_values[1]}"
        else:
            calculation_display = f"{numeric_values[0]} ÷ " + " ÷ ".join([str(num) for num in divisors])

        # Format result with appropriate precision
        if result.is_integer():
            formatted_result = int(result)
        elif abs(result) > 1e10 or (abs(result) < 1e-4 and result != 0):
            formatted_result = f"{result:.2e}"  # Scientific notation
        else:
            formatted_result = round(result, 8)  # Higher precision for division
            # Remove trailing zeros
            if isinstance(formatted_result, float):
                formatted_result = f"{formatted_result:g}"

        # Add fraction representation for simple cases
        fraction_info = ""
        if len(numeric_values) == 2 and all(num.is_integer() for num in numeric_values):
            from math import gcd
            numerator = int(numeric_values[0])
            denominator = int(numeric_values[1])
            common_divisor = gcd(abs(numerator), abs(denominator))

            if common_divisor > 1:
                simplified_num = numerator // common_divisor
                simplified_den = denominator // common_divisor
                fraction_info = f"\n📐 Simplified fraction: {simplified_num}/{simplified_den}"

        logger.info(f"Division completed successfully: {result}")

        return f" **Division Result**\n" \
               f"Calculation: {calculation_display} = **{formatted_result}**{fraction_info}\n" \
               f"Numbers processed: {len(numeric_values)}"

    except ValueError as e:
        error_msg = f" **Input Error**: Invalid number format detected."
        logger.error(f"ValueError in divide_numbers: {e}")
        return error_msg

    except Exception as e:
        error_msg = f" **System Error**: An unexpected error occurred."
        logger.error(f"Unexpected error in divide_numbers: {e}")
        return error_msg

@tool
def power_numbers(expression: str) -> str:
  """
    Calculate powers and exponents with support for various input formats.

    Args:
        expression (str): Power expression supporting formats like:
            - "2 ^ 3" (2 to the power of 3)
            - "2 ** 3" (Python power notation)
            - "2, 3" (comma-separated: base, exponent)
            - "5 ^ 2 ^ 2" (chain powers, right-associative)
            - "sqrt(16)" or "16 ^ 0.5" (fractional exponents)

    Returns:
        str: Formatted result with calculation details or error message

    Examples:
        >>> power_numbers("2 ^ 3")
        "Calculation: 2³ = 8"
        >>> power_numbers("9 ^ 0.5")
        "Calculation: 9^0.5 = 3 (√9)"
    """
  try:
        import re  # Move import to top of function
        import math

        logger.info(f"Processing power calculation request: {expression}")

        cleaned_expression = expression.strip().lower()
        result = None
        calculation_display = ""
        special_info = ""

        # Handle special cases: sqrt, cube root, etc.
        if "sqrt" in cleaned_expression:
            sqrt_match = re.search(r'sqrt\s*\(\s*(-?\d+\.?\d*)\s*\)', cleaned_expression)
            if sqrt_match:
                number = float(sqrt_match.group(1))
                if number < 0:
                    return "Mathematical Error: Square root of negative numbers not supported in real numbers.\nTip: Use positive numbers for square roots."

                result = number ** 0.5
                calculation_display = f"√{number}"
                special_info = f" (Square root of {number})"

        # Handle regular power expressions
        if result is None:
            number_pattern = r'-?\d+\.?\d*'
            numbers = re.findall(number_pattern, cleaned_expression)

            if not numbers:
                return "Error: No valid numbers found in the input."

            if len(numbers) < 2:
                return "Error: Power calculation requires base and exponent."

            numeric_values = [float(num) for num in numbers]
            base = numeric_values[0]
            exponent = numeric_values[1]

            # Handle special mathematical cases
            if base == 0 and exponent < 0:
                return "Mathematical Error: 0 raised to negative power is undefined.\nTip: Zero cannot be raised to negative powers."

            if base < 0 and not exponent.is_integer():
                return "Mathematical Error: Negative base with fractional exponent not supported in real numbers.\nTip: Use positive bases with fractional exponents."

            # Calculate result
            result = base ** exponent

            # Create calculation display
            if exponent == 2:
                calculation_display = f"{base}²"
                special_info = f" ({base} squared)"
            elif exponent == 3:
                calculation_display = f"{base}³"
                special_info = f" ({base} cubed)"
            else:
                calculation_display = f"{base}^{exponent}"

        # Format result
        if abs(result) > 1e15:
            formatted_result = f"{result:.2e}"
            special_info += " (Very large number)"
        elif result.is_integer():
            formatted_result = int(result)
        else:
            formatted_result = f"{result:.10g}"

        logger.info(f"Power calculation completed successfully: {result}")

        return f"**Power Calculation Result**\nCalculation: {calculation_display} = **{formatted_result}**{special_info}"

  except OverflowError:
        return "Mathematical Error: Result too large to calculate.\nTip: Try smaller numbers or lower exponents."

  except Exception as e:
        error_msg = "System Error: An unexpected error occurred."
        logger.error(f"Unexpected error in power_numbers: {e}")
        return error_msg

@tool
def square_root(expression: str) -> str:
    """
    Calculate square roots with support for multiple input formats and mathematical insights.

    Args:
        expression (str): Square root expression supporting formats like:
            - "sqrt(25)" (function notation)
            - "√25" (root symbol)
            - "25" (just the number)
            - "sqrt 16" (space notation)
            - Multiple roots: "sqrt(9), sqrt(16)"

    Returns:
        str: Formatted result with calculation details or error message

    Examples:
        >>> square_root("sqrt(25)")
        "Calculation: √25 = 5 (Perfect square)"
        >>> square_root("10")
        "Calculation: √10 ≈ 3.162278 (Irrational)"
    """
    try:
        logger.info(f"Processing square root request: {expression}")

        cleaned_expression = expression.strip().replace('√', 'sqrt')
        results = []

        # Handle multiple square roots
        if ',' in cleaned_expression:
            parts = [part.strip() for part in cleaned_expression.split(',')]
            for part in parts:
                single_result = _calculate_single_sqrt(part)
                if single_result:
                    results.append(single_result)

            if not results:
                return " Error: No valid numbers found for square root calculation."

            # Format multiple results
            combined_results = "\n".join([f"• {result}" for result in results])
            return f"√ **Multiple Square Root Results**\n{combined_results}"

        else:
            # Single square root calculation
            single_result = _calculate_single_sqrt(cleaned_expression)
            if single_result:
                return f"√ **Square Root Result**\n{single_result}"
            else:
                return " Error: No valid number found for square root calculation."

    except Exception as e:
        error_msg = f" **System Error**: An unexpected error occurred."
        logger.error(f"Unexpected error in square_root: {e}")
        return error_msg

@tool
def _calculate_single_sqrt(expression: str) -> str:
    """Helper function to calculate a single square root."""
    try:
        import re
        import math

        # Extract number from various formats
        if "sqrt" in expression:
            # Handle sqrt(number) or sqrt number
            sqrt_match = re.search(r'sqrt\s*\(?\s*(-?\d+\.?\d*)\s*\)?', expression)
            if sqrt_match:
                number = float(sqrt_match.group(1))
            else:
                return None
        else:
            # Just a plain number
            number_match = re.search(r'(-?\d+\.?\d*)', expression)
            if number_match:
                number = float(number_match.group(1))
            else:
                return None

        # Validate input
        if number < 0:
            return f"√{number} = **Undefined** (Negative numbers don't have real square roots)\n" \
                   f" Note: √{number} = {abs(number)**0.5:.6g}i (imaginary number)"

        if number == 0:
            return f"√0 = **0** (Square root of zero is zero)"

        # Calculate square root
        result = math.sqrt(number)

        # Determine if it's a perfect square
        is_perfect_square = result.is_integer()

        # Format result
        if is_perfect_square:
            formatted_result = int(result)
            math_type = "Perfect square"
            extra_info = f" {int(number)} is a perfect square!"
        else:
            formatted_result = f"{result:.10g}"  # Remove trailing zeros
            math_type = "Irrational number"

            # Check if it's close to a simple fraction
            simple_fractions = [(1/2, "1/2"), (1/3, "1/3"), (2/3, "2/3"), (1/4, "1/4"), (3/4, "3/4")]
            fraction_approx = ""
            for frac_val, frac_str in simple_fractions:
                if abs(result - frac_val) < 0.001:
                    fraction_approx = f" ≈ {frac_str}"
                    break

            extra_info = f"📐 Decimal approximation{fraction_approx}"

        # Add mathematical insights
        insights = []

        # Perfect square insights
        if is_perfect_square:
            root = int(result)
            insights.append(f"Verification: {root} × {root} = {int(number)}")

        # Special number insights
        if number == 2:
            insights.append("√2 ≈ 1.414 (Diagonal of unit square)")
        elif number == 3:
            insights.append("√3 ≈ 1.732 (Height of equilateral triangle)")
        elif number == 5:
            insights.append("√5 ≈ 2.236 (Related to golden ratio)")
        elif number == 10:
            insights.append("√10 ≈ 3.162 (Common in engineering)")

        insight_text = f"\n {' | '.join(insights)}" if insights else ""

        return f"√{number} = **{formatted_result}** ({math_type})\n" \
               f"{extra_info}{insight_text}"

    except Exception as e:
        logger.error(f"Error in _calculate_single_sqrt: {e}")
        return None

@tool
def calculate_expression(expression: str) -> str:
    """
    Intelligent calculator that evaluates mathematical expressions and routes to specialized tools when appropriate.

    Args:
        expression (str): Mathematical expression supporting:
            - Simple operations: "5+3", "10-2" (routes to specialized tools)
            - Basic operations: +, -, *, /, ^, **
            - Parentheses for grouping: (2+3)*4
            - Mathematical functions: sqrt, abs, sin, cos, tan, log
            - Constants: pi, e
            - Mixed expressions: "2*pi*r" or "sqrt(a^2 + b^2)"

    Returns:
        str: Formatted result with step-by-step breakdown or error message

    Examples:
        >>> calculate_expression("5 + 3")
        Routes to specialized addition tool
        >>> calculate_expression("2*pi*r")
        "Expression: 2*pi*r = [result] (Advanced calculation)"
    """
    try:
        logger.info(f"Processing expression: {expression}")

        import re
        import math

        # First, try to route to specialized tools for simple operations
        routing_result = _route_to_specialized_tool(expression)
        if routing_result:
            tool_name, result = routing_result
            logger.info(f"Routed to {tool_name}")
            return f"[{tool_name}]\n{result}"

        # If no routing, proceed with advanced calculation
        logger.info("Processing with advanced calculator")

        # Clean and prepare expression
        cleaned_expr = expression.strip().lower()
        original_expr = expression.strip()

        # Replace common mathematical notation
        replacements = {
            '^': '**',          # Power operator
            'π': 'pi',          # Pi constant
            '×': '*',           # Multiplication symbol
            '÷': '/',           # Division symbol
            'sqrt': 'math.sqrt', # Square root function
            'sin': 'math.sin',   # Sine function
            'cos': 'math.cos',   # Cosine function
            'tan': 'math.tan',   # Tangent function
            'log': 'math.log10', # Logarithm base 10
            'ln': 'math.log',    # Natural logarithm
            'abs': 'abs',        # Absolute value
            'pi': 'math.pi',     # Pi constant
            'e': 'math.e'        # Euler's number
        }

        # Apply replacements
        processed_expr = cleaned_expr
        for old, new in replacements.items():
            processed_expr = processed_expr.replace(old, new)

        # Validate expression for safety
        dangerous_patterns = ['import', 'exec', 'eval', '__', 'open', 'file']
        if any(pattern in processed_expr for pattern in dangerous_patterns):
            return "Security Error: Expression contains prohibited operations."

        # Evaluate the expression
        try:
            result = eval(processed_expr, {"__builtins__": {}, "math": math, "abs": abs})
        except NameError as e:
            return f"Expression Error: Unknown function or variable in expression.\nDetails: {str(e)}"
        except ZeroDivisionError:
            return "Mathematical Error: Division by zero detected in expression."
        except ValueError as e:
            return f"Mathematical Error: Invalid operation in expression.\nDetails: {str(e)}"

        # Format the result
        if isinstance(result, complex):
            if result.imag == 0:
                result = result.real
            else:
                return f"Complex Result: {result.real:.6g} + {result.imag:.6g}i"

        # Determine result formatting
        if abs(result) > 1e15:
            formatted_result = f"{result:.4e}"
            precision_note = " (Scientific notation - very large number)"
        elif abs(result) < 1e-10 and result != 0:
            formatted_result = f"{result:.4e}"
            precision_note = " (Scientific notation - very small number)"
        elif abs(result - round(result)) < 1e-10:
            formatted_result = int(round(result))
            precision_note = ""
        else:
            formatted_result = f"{result:.10g}"
            precision_note = ""

        # Analyze expression complexity
        complexity_indicators = []
        if 'math.sqrt' in processed_expr:
            complexity_indicators.append("Square root operation")
        if any(trig in processed_expr for trig in ['math.sin', 'math.cos', 'math.tan']):
            complexity_indicators.append("Trigonometric function")
        if any(log in processed_expr for log in ['math.log', 'math.log10']):
            complexity_indicators.append("Logarithmic function")
        if 'math.pi' in processed_expr:
            complexity_indicators.append("Pi constant used")
        if 'math.e' in processed_expr:
            complexity_indicators.append("Euler's number used")
        if '**' in processed_expr:
            complexity_indicators.append("Exponentiation")

        # Build response
        response_parts = []
        response_parts.append("ADVANCED CALCULATION RESULT")
        response_parts.append(f"Expression: {original_expr} = {formatted_result}{precision_note}")

        if complexity_indicators:
            response_parts.append(f"Operations detected: {', '.join(complexity_indicators)}")

        # Add verification for simple cases
        if len(processed_expr.replace(' ', '')) < 20 and not any(func in processed_expr for func in ['math.sin', 'math.cos', 'math.tan', 'math.log']):
            try:
                if '+' in original_expr or '-' in original_expr or '*' in original_expr or '/' in original_expr:
                    response_parts.append("Expression successfully evaluated using order of operations")
            except:
                pass

        logger.info(f"Complex expression evaluated successfully: {result}")

        return "\n".join(response_parts)

    except SyntaxError:
        return "Syntax Error: Invalid mathematical expression format.\nTip: Check parentheses and operator placement."

    except Exception as e:
        error_msg = "System Error: Unable to evaluate expression."
        logger.error(f"Unexpected error in calculate_expression: {e}")
        return error_msg

@tool
def _route_to_specialized_tool(expression: str):
    """Route simple expressions to specialized tools."""
    import re

    cleaned = expression.strip().lower().replace(' ', '')
    original = expression.strip()

    # Check for mathematical constants/functions first
    advanced_indicators = ['pi', 'π', 'e', 'sin', 'cos', 'tan', 'log', 'ln', '(', ')']
    if any(indicator in cleaned for indicator in advanced_indicators):
        return None  # Use advanced calculator

    # Simple addition: only + signs with numbers
    if '+' in cleaned and not any(op in cleaned for op in ['*', '/', '^', '**', 'sqrt']):
        if re.match(r'^\d+\.?\d*(\+\d+\.?\d*)+$', cleaned):
            return ("Addition Tool", add_numbers(original))

    # Simple subtraction: only - signs with numbers
    if '-' in cleaned and not any(op in cleaned for op in ['*', '/', '^', '**', 'sqrt']):
        if re.match(r'^\d+\.?\d*(-\d+\.?\d*)+$', cleaned):
            return ("Subtraction Tool", subtract_numbers(original))

    # Simple multiplication: only * or × signs
    if ('*' in cleaned or '×' in cleaned) and not any(op in cleaned for op in ['+', '/', '^', '**', 'sqrt']) and not '--' in cleaned:
        return ("Multiplication Tool", multiply_numbers(original))

    # Simple division: only / or ÷ signs
    if ('/' in cleaned or '÷' in cleaned) and not any(op in cleaned for op in ['+', '*', '×', '^', '**', 'sqrt']):
        return ("Division Tool", divide_numbers(original))

    # Power operations: simple base^exponent
    if ('^' in cleaned or '**' in cleaned) and re.match(r'^\d+\.?\d*(\^|\*\*)\d+\.?\d*$', cleaned):
        return ("Power Tool", power_numbers(original))

    # Square root operations
    if 'sqrt' in cleaned or '√' in cleaned:
        return ("Square Root Tool", square_root(original))

    return None
@tool
def solve_geometry_word_problem(problem: str) -> str:
    """
    Solve geometry word problems involving area, perimeter, volume, etc.

    Args:
        problem (str): Geometry word problem containing:
            - Shape type (circle, rectangle, triangle, etc.)
            - Dimensions
            - What to calculate (area, perimeter, volume)

    Examples:
        "A circle has radius 7cm. What's the area?"
        "Rectangle is 10m long and 6m wide. Find the perimeter."
        "Square with side 5 inches. Calculate area and perimeter."
    """
    try:
        import re
        import math
        logger.info(f"Processing geometry problem: {problem}")

        problem_lower = problem.lower()

        # Extract numbers
        numbers = re.findall(r'(\d+\.?\d*)', problem)
        if not numbers:
            return "❌ Error: No dimensions found in the problem."

        # Identify shape
        shape = None
        if any(word in problem_lower for word in ['circle', 'circular', 'round']):
            shape = 'circle'
        elif any(word in problem_lower for word in ['rectangle', 'rectangular']):
            shape = 'rectangle'
        elif any(word in problem_lower for word in ['square']):
            shape = 'square'
        elif any(word in problem_lower for word in ['triangle', 'triangular']):
            shape = 'triangle'

        if not shape:
            return "❌ Error: Could not identify the shape. Please specify circle, rectangle, square, or triangle."

        # Identify what to calculate
        calculate_area = any(word in problem_lower for word in ['area', 'surface'])
        calculate_perimeter = any(word in problem_lower for word in ['perimeter', 'circumference', 'around'])

        # If nothing specified, calculate both
        if not calculate_area and not calculate_perimeter:
            calculate_area = calculate_perimeter = True

        results = []
        formulas_used = []

        # Circle calculations
        if shape == 'circle':
            radius = float(numbers[0])

            if calculate_area:
                area = math.pi * radius ** 2
                results.append(f"Area = π × r² = π × {radius}² = {area:.2f} square units")
                formulas_used.append("Area of circle: π × r²")

            if calculate_perimeter:
                circumference = 2 * math.pi * radius
                results.append(f"Circumference = 2 × π × r = 2 × π × {radius} = {circumference:.2f} units")
                formulas_used.append("Circumference: 2 × π × r")

        # Rectangle calculations
        elif shape == 'rectangle':
            if len(numbers) < 2:
                return "❌ Error: Rectangle requires length and width."

            length = float(numbers[0])
            width = float(numbers[1])

            if calculate_area:
                area = length * width
                results.append(f"Area = length × width = {length} × {width} = {area:.2f} square units")
                formulas_used.append("Area of rectangle: length × width")

            if calculate_perimeter:
                perimeter = 2 * (length + width)
                results.append(f"Perimeter = 2 × (length + width) = 2 × ({length} + {width}) = {perimeter:.2f} units")
                formulas_used.append("Perimeter of rectangle: 2 × (length + width)")

        # Square calculations
        elif shape == 'square':
            side = float(numbers[0])

            if calculate_area:
                area = side ** 2
                results.append(f"Area = side² = {side}² = {area:.2f} square units")
                formulas_used.append("Area of square: side²")

            if calculate_perimeter:
                perimeter = 4 * side
                results.append(f"Perimeter = 4 × side = 4 × {side} = {perimeter:.2f} units")
                formulas_used.append("Perimeter of square: 4 × side")

        # Triangle calculations (assuming equilateral or given base and height)
        elif shape == 'triangle':
            if len(numbers) >= 2:
                base = float(numbers[0])
                height = float(numbers[1])

                if calculate_area:
                    area = 0.5 * base * height
                    results.append(f"Area = ½ × base × height = ½ × {base} × {height} = {area:.2f} square units")
                    formulas_used.append("Area of triangle: ½ × base × height")
            else:
                return "❌ Error: Triangle area calculation requires base and height."

        # Format response
        calculation_details = "\n".join([f"• {result}" for result in results])
        formulas_text = "\n".join([f"📐 {formula}" for formula in formulas_used])

        return f"📏 **Geometry Problem Solution**\n\n" \
               f"**Shape:** {shape.title()}\n" \
               f"**Calculations:**\n{calculation_details}\n\n" \
               f"**Formulas used:**\n{formulas_text}"

    except Exception as e:
        logger.error(f"Error in solve_geometry_word_problem: {e}")
        return "❌ System Error: Unable to solve geometry problem."

@tool
def solve_discount_problem(problem: str) -> str:
    """
    Solve discount and tax problems with multiple steps.

    Args:
        problem (str): Word problem containing:
            - Original price
            - Discount percentage
            - Tax percentage (optional)
            - Tip percentage (optional)

    Examples:
        "I bought a $120 jacket with 15% discount, then paid 8% tax"
        "A pizza costs $20. If I tip 18%, what's the total?"
        "Item costs $50 with 25% off and 10% tax"
    """
    try:
        import re
        logger.info(f"Processing discount problem: {problem}")

        # Extract numerical values and percentages
        prices = re.findall(r'\$?(\d+\.?\d*)', problem.lower())
        percentages = re.findall(r'(\d+\.?\d*)%', problem.lower())

        if not prices:
            return "❌ Error: No price found in the problem. Please include the original price."

        original_price = float(prices[0])

        # Initialize calculation steps
        steps = []
        current_amount = original_price
        steps.append(f"Original price: ${original_price:.2f}")

        # Identify discount, tax, and tip
        discount_rate = 0
        tax_rate = 0
        tip_rate = 0

        problem_lower = problem.lower()

        # Find discount
        discount_keywords = ['discount', 'off', 'sale', 'reduction', 'markdown']
        if any(keyword in problem_lower for keyword in discount_keywords) and percentages:
            for i, percentage in enumerate(percentages):
                if any(keyword in problem_lower for keyword in discount_keywords):
                    discount_rate = float(percentage) / 100
                    break

        # Find tax
        tax_keywords = ['tax', 'sales tax', 'vat']
        if any(keyword in problem_lower for keyword in tax_keywords):
            for percentage in percentages:
                # Usually tax comes after discount in the sentence
                if discount_rate == 0 or float(percentage) != discount_rate * 100:
                    tax_rate = float(percentage) / 100
                    break

        # Find tip
        tip_keywords = ['tip', 'gratuity', 'service charge']
        if any(keyword in problem_lower for keyword in tip_keywords):
            for percentage in percentages:
                if float(percentage) / 100 not in [discount_rate, tax_rate]:
                    tip_rate = float(percentage) / 100
                    break

        # Apply discount first
        if discount_rate > 0:
            discount_amount = current_amount * discount_rate
            current_amount -= discount_amount
            steps.append(f"Discount ({discount_rate*100:.1f}%): -${discount_amount:.2f}")
            steps.append(f"After discount: ${current_amount:.2f}")

        # Apply tax to discounted price
        if tax_rate > 0:
            tax_amount = current_amount * tax_rate
            current_amount += tax_amount
            steps.append(f"Tax ({tax_rate*100:.1f}%): +${tax_amount:.2f}")
            steps.append(f"After tax: ${current_amount:.2f}")

        # Apply tip (usually on pre-tax amount for restaurants)
        if tip_rate > 0:
            if tax_rate > 0:
                # Tip on pre-tax amount (common practice)
                tip_base = current_amount - tax_amount if tax_rate > 0 else current_amount
            else:
                tip_base = current_amount

            tip_amount = tip_base * tip_rate
            current_amount += tip_amount
            steps.append(f"Tip ({tip_rate*100:.1f}%): +${tip_amount:.2f}")
            steps.append(f"Final total: ${current_amount:.2f}")

        # Format response
        calculation_summary = "\n".join([f"• {step}" for step in steps])

        # Add insights
        insights = []
        if discount_rate > 0:
            savings = original_price * discount_rate
            savings_percent = (savings / original_price) * 100
            insights.append(f"You saved ${savings:.2f} ({savings_percent:.1f}%)")

        if tax_rate > 0 and tip_rate > 0:
            insights.append("Tax and tip were calculated separately as per common practice")

        insight_text = "\n💡 " + " | ".join(insights) if insights else ""

        return f"💰 **Purchase Calculation Result**\n\n" \
               f"**Step-by-step breakdown:**\n{calculation_summary}\n" \
               f"\n**Final amount to pay: ${current_amount:.2f}**{insight_text}"

    except Exception as e:
        logger.error(f"Error in solve_discount_problem: {e}")
        return "❌ System Error: Unable to solve discount problem."

@tool
def solve_multi_step_problem(problem: str) -> str:
    """
    Solve complex multi-step word problems that combine different mathematical operations.

    Args:
        problem (str): Multi-step problem that might involve:
            - Sequential calculations
            - Percentages, discounts, and increases
            - Rate and time problems
            - Ratio and proportion problems

    Examples:
        "John earns $50k/year. He gets 10% raise, then 5% bonus. What's his new salary?"
        "A car travels 60 mph for 2 hours, then 40 mph for 1.5 hours. Total distance?"
        "Recipe serves 4 people. Need for 10 people. Original uses 2 cups flour, 3 eggs."
    """
    try:
        import re
        logger.info(f"Processing multi-step problem: {problem}")

        problem_lower = problem.lower()

        # Extract all numbers
        numbers = re.findall(r'(\d+\.?\d*)', problem)
        percentages = re.findall(r'(\d+\.?\d*)%', problem)

        steps = []
        current_value = None

        # Salary/Income problems
        if any(word in problem_lower for word in ['salary', 'earn', 'income', 'pay', 'wage']):
            if numbers:
                initial_salary = float(numbers[0])
                # Handle k notation (50k = 50,000)
                if 'k' in problem_lower:
                    initial_salary *= 1000

                current_value = initial_salary
                steps.append(f"Initial salary: ${current_value:,.2f}")

                # Apply raises and bonuses
                for i, percentage in enumerate(percentages):
                    rate = float(percentage) / 100

                    if 'raise' in problem_lower or 'increase' in problem_lower:
                        increase = current_value * rate
                        current_value += increase
                        steps.append(f"After {percentage}% raise: +${increase:,.2f} = ${current_value:,.2f}")
                    elif 'bonus' in problem_lower:
                        bonus = current_value * rate
                        current_value += bonus
                        steps.append(f"After {percentage}% bonus: +${bonus:,.2f} = ${current_value:,.2f}")

        # Distance/Speed/Time problems
        elif any(word in problem_lower for word in ['mph', 'speed', 'distance', 'travel', 'hour']):
            total_distance = 0
            total_time = 0

            # Extract speed and time pairs
            i = 0
            while i < len(numbers) - 1:
                speed = float(numbers[i])
                time = float(numbers[i + 1])

                distance = speed * time
                total_distance += distance
                total_time += time

                steps.append(f"Segment {i//2 + 1}: {speed} mph × {time} hours = {distance} miles")
                i += 2

            current_value = total_distance
            steps.append(f"Total distance: {total_distance} miles")
            steps.append(f"Total time: {total_time} hours")

            if total_time > 0:
                avg_speed = total_distance / total_time
                steps.append(f"Average speed: {avg_speed:.2f} mph")

        # Recipe scaling problems
        elif any(word in problem_lower for word in ['recipe', 'serves', 'people', 'cups', 'ingredients']):
            # Find original serving size and target size
            serving_numbers = [float(n) for n in numbers if 'people' in problem or 'serves' in problem]
            if len(serving_numbers) >= 2:
                original_serves = serving_numbers[0]
                target_serves = serving_numbers[1]
                scale_factor = target_serves / original_serves

                steps.append(f"Original recipe serves: {original_serves} people")
                steps.append(f"Need to serve: {target_serves} people")
                steps.append(f"Scale factor: {target_serves} ÷ {original_serves} = {scale_factor:.2f}")

                # Scale ingredients
                ingredient_amounts = [float(n) for n in numbers if n not in [str(original_serves), str(target_serves)]]
                for i, amount in enumerate(ingredient_amounts):
                    new_amount = amount * scale_factor
                    steps.append(f"Ingredient {i+1}: {amount} × {scale_factor:.2f} = {new_amount:.2f}")

        # If no specific pattern matched, try general sequential calculation
        else:
            if numbers and percentages:
                current_value = float(numbers[0])
                steps.append(f"Starting value: {current_value}")

                for percentage in percentages:
                    rate = float(percentage) / 100
                    if 'increase' in problem_lower or 'more' in problem_lower:
                        increase = current_value * rate
                        current_value += increase
                        steps.append(f"After {percentage}% increase: {current_value:.2f}")
                    elif 'decrease' in problem_lower or 'less' in problem_lower:
                        decrease = current_value * rate
                        current_value -= decrease
                        steps.append(f"After {percentage}% decrease: {current_value:.2f}")

        if not steps:
            return "❌ Error: Could not identify the problem type or find sufficient information."

        # Format response
        step_details = "\n".join([f"{i+1}. {step}" for i, step in enumerate(steps)])

        final_answer = ""
        if current_value is not None:
            if 'salary' in problem_lower or '$' in problem:
                final_answer = f"\n\n**Final Answer: ${current_value:,.2f}**"
            else:
                final_answer = f"\n\n**Final Answer: {current_value:.2f}**"

        return f"🔢 **Multi-Step Problem Solution**\n\n" \
               f"**Step-by-step calculation:**\n{step_details}{final_answer}"

    except Exception as e:
        logger.error(f"Error in solve_multi_step_problem: {e}")
        return "❌ System Error: Unable to solve multi-step problem."

# Add these tools to your existing setup
def get_enhanced_math_tools():
    """
    Get all mathematical tools including word problem solvers.
    """
    return [
        calculate_expression,           # Your existing smart calculator
        solve_discount_problem,         # New: Discount/tax/tip problems
        solve_geometry_word_problem,    # New: Geometry problems
        solve_multi_step_problem,       # New: Complex multi-step problems
        add_numbers,                    # Existing specialized tools
        subtract_numbers,
        multiply_numbers,
        divide_numbers,
        power_numbers,
        square_root
    ]