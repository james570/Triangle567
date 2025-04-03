

def classify_triangle(a, b, c):
    """
    Classify a triangle based on its side lengths.

    Args:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.

    Returns:
        str: The type of triangle (Equilateral, Isosceles, Scalene, or Not a triangle).
    """
    # First, sort the sides to make it easier to check for right triangles
    sides = sorted([a, b, c])
    x, y, z = sides  # x and y are the smaller sides, z is the longest

    # Check if the sides form a valid triangle (Triangle Inequality Theorem)
    if x + y <= z:
        return "Not a triangle"

    # Determine the type of triangle
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check if it's a right triangle using the Pythagorean Theorem (a² + b² = c²)
    if x ** 2 + y ** 2 == z ** 2:
        triangle_type += " and Right"

    return triangle_type


# Example usage:
if __name__ == "__main__":
    print(classify_triangle(3, 4, 5))  # Should print: "Scalene and Right"
    print(classify_triangle(5, 5, 5))  # Should print: "Equilateral"
    print(classify_triangle(2, 2, 3))  # Should print: "Isosceles"
    print(classify_triangle(1, 2, 3))  # Should print: "Not a triangle"