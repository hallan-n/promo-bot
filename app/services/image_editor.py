from models import Product
from PIL import Image, ImageDraw, ImageFont
from utils import format_brl


def round(imagem, raio):
    mask = Image.new("L", imagem.size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle(
        [0, 0, imagem.width, imagem.height], radius=raio, fill=255
    )
    imagem_rounded = Image.new("RGBA", imagem.size)
    imagem_rounded.paste(imagem, (0, 0), mask=mask)
    return imagem_rounded


def add_text(
    base,
    text,
    color,
    size,
    font_type,
    x,
    y,
    width,
    height,
    underline=False,
    strike=False,
):
    draw = ImageDraw.Draw(base)
    font = ImageFont.truetype(f"./assets/inter-{font_type}.ttf", size=size)

    lines = []
    words = text.split()
    current_line = ""

    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        bbox = draw.textbbox((0, 0), test_line, font=font)
        line_width = bbox[2] - bbox[0]

        if line_width <= width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    for line in lines:
        draw.text((x, y), line, font=font, fill=color)

        bbox = draw.textbbox((x, y), line, font=font)
        line_width = bbox[2] - bbox[0]
        line_height = bbox[3] - bbox[1]

        if underline:
            underline_y = y + line_height + 5
            draw.line(
                (x, underline_y, x + line_width, underline_y), fill=color, width=3
            )

        if strike:
            strike_y = y + (line_height // 2) + 8
            draw.line((x, strike_y, x + line_width, strike_y), fill=color, width=3)

        y += line_height + height


def save_stories(product: Product, image_path: str, output_path: str):
    base = Image.open("./assets/base.png").convert("RGBA")
    center_img = Image.open(image_path).convert("RGBA").resize((1100, 1100))
    center_img = round(center_img, raio=50)

    if product.cupom:
        add_text(
            base,
            f"CUMPOM: {product.cupom.upper()}",
            "white",
            50,
            "bold",
            370,
            290,
            1100,
            5,
        )

    name = product.name
    if len(product.name) >= 85:
        name = f"{product.name[:80]}..."

    add_text(base, name, "#3F3F3F", 60, "regular", 250, 1600, 1100, 20)

    add_text(
        base,
        f"de R$ {format_brl(product.original_price)}",
        "red",
        50,
        "bold",
        250,
        1850,
        1100,
        8,
        None,
        True,
    )

    match len(str(int(product.price_discount))):
        case 1:
            add_text(
                base,
                f"R$ {format_brl(product.price_discount)}",
                "white",
                90,
                "bold",
                420,
                1960,
                1100,
                8,
            )
        case 2:
            add_text(
                base,
                f"R$ {format_brl(product.price_discount)}",
                "white",
                90,
                "bold",
                390,
                1960,
                1100,
                8,
            )
        case 3:
            add_text(
                base,
                f"R$ {format_brl(product.price_discount)}",
                "white",
                90,
                "bold",
                360,
                1960,
                1100,
                8,
            )
        case 4:
            add_text(
                base,
                f"R$ {format_brl(product.price_discount)}",
                "white",
                90,
                "bold",
                320,
                1960,
                1100,
                8,
            )
        case 5:
            add_text(
                base,
                f"R$ {format_brl(product.price_discount)}",
                "white",
                90,
                "bold",
                300,
                1960,
                1100,
                8,
            )

    if product.payment_condition:
        add_text(
            base,
            product.payment_condition,
            "#3F3F3F",
            50,
            "regular",
            1000,
            1930,
            350,
            10,
        )

    pos_center = (
        (base.width - center_img.width) // 2,
        (base.height - center_img.height) // 4,
    )
    base.paste(center_img, pos_center, center_img)

    base.save(output_path)
