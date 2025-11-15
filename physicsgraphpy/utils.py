import csv

def export_csv(filename, times, positions, velocities=None, accelerations=None):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        header = ['Time', 'Position']
        if velocities: header.append('Velocity')
        if accelerations: header.append('Acceleration')
        writer.writerow(header)
        for i, t in enumerate(times):
            row = [t, positions[i]]
            if velocities: row.append(velocities[i])
            if accelerations: row.append(accelerations[i])
            writer.writerow(row)

def format_markdown(title, content_dict):
    md = f"# {title}\n"
    for k, v in content_dict.items():
        md += f"\n**{k}:** {v}\n"
    return md
    
def convert_units(value, from_unit, to_unit):
    conversions = {
        ('m', 'cm'): lambda x: x * 100,
        ('cm', 'm'): lambda x: x / 100,
        ('m/s', 'km/h'): lambda x: x * 3.6,
        ('km/h', 'm/s'): lambda x: x / 3.6,
    }
    try:
        return conversions[(from_unit, to_unit)](value)
    except KeyError:
        raise ValueError("Unsupported conversion.")

def check_si_units(value, expected_unit):
    si_units = ['m', 's', 'kg']
    if expected_unit not in si_units:
        raise ValueError(f"{expected_unit} is not a standard SI unit.")

