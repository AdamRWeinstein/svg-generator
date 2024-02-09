from PIL import Image

def png_to_svg(png_file, svg_file):
    try:
        # Open the PNG file
        img = Image.open(png_file)
        img = img.convert("RGBA")  # Ensure it's in RGBA format
        width, height = img.size

        # SVG header
        svg_data = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'

        # Process the image pixels
        for y in range(height):
            x = 0
            while x < width:
                r, g, b, a = img.getpixel((x, y))

                # If the pixel is not transparent, start creating a rectangle
                if a != 0:
                    start_x = x
                    # Find the length of the segment with the same color
                    while x < width and img.getpixel((x, y)) == (r, g, b, a):
                        x += 1
                    length = x - start_x

                    # Add a rectangle to the SVG for this segment
                    svg_data += f'<rect x="{start_x}" y="{y}" width="{length}" height="1" fill="rgb({r},{g},{b})" fill-opacity="{a/255}"/>\n'
                else:
                    x += 1

        # SVG footer
        svg_data += '</svg>'

        # Write the SVG data to a file
        with open(svg_file, 'w') as f:
            f.write(svg_data)

        print(f"SVG file '{svg_file}' successfully created.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example:
png_to_svg('input.png', 'output.svg')
