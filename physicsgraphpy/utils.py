def convert_units(value, from_unit, to_unit):
    """
    Convert between SI units for length, velocity, and acceleration.
    Supported examples: m <-> cm, m/s <-> km/h, m/s^2 <-> g
    """
    conversions = {
        ("m", "cm"): lambda x: x * 100,
        ("cm", "m"): lambda x: x / 100,
        ("m/s", "km/h"): lambda x: x * 3.6,
        ("km/h", "m/s"): lambda x: x / 3.6,
        ("m/s^2", "g"): lambda x: x / 9.8,
        ("g", "m/s^2"): lambda x: x * 9.8
    }
    try:
        return conversions[(from_unit, to_unit)](value)
    except KeyError:
        raise ValueError("Unsupported unit conversion.")

def format_markdown(title, content_dict):
    """
    Simple function to format results in Markdown.
    """
    md = f"# {title}\n"
    for k, v in content_dict.items():
        md += f"\n**{k}:**\n\n{v}\n"
    return md
