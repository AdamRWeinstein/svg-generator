from PIL import Image

def png_to_silhouette(png_file, svg_file):
    # Open the PNG file
    img = Image.open(png_file)
    img = img.convert("RGBA")  # Ensure it's in RGBA format for transparency support
    width, height = img.size

    # SVG header
    svg_data = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'

    # Process the image pixels
    for y in range(height):
        x = 0
        while x < width:
            r, g, b, a = img.getpixel((x, y))

            # If the pixel is not transparent, start a new rectangle
            if a != 0:
                start_x = x
                # Extend the rectangle width as long as the next pixel is also not transparent
                while x < width and img.getpixel((x, y))[3] != 0:
                    x += 1
                length = x - start_x

                # Add a rectangle for this segment
                svg_data += f'<rect x="{start_x}" y="{y}" width="{length}" height="1" fill="black"/>\n'
            else:
                x += 1

    # SVG footer
    svg_data += '</svg>'

    # Write the SVG data to a file
    with open(svg_file, 'w') as f:
        f.write(svg_data)

    print(f"SVG silhouette file '{svg_file}' successfully created.")

# Usage example:
png_to_silhouette('./DexHouse.png', './Silhouettes/Dex.svg')
png_to_silhouette('./Higsby\'s.png', './Silhouettes/Higsby.svg')
png_to_silhouette('./HikariHome.png', './Silhouettes/Lan.svg')
png_to_silhouette('./MaylsHome.png', './Silhouettes/Mayl.svg')
png_to_silhouette('./YaisHome.png', './Silhouettes/Yai.svg')