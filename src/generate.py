import json

def generate(labels, colors, trans):
    """generates CccpChart class into ./cccpchart.py"""

    with open('cccpchart.py', 'w') as f:
        c = (
            f"# GENERATED FILE, DO NOT EDIT\n"
            f"from pychartjs import BaseChart, ChartType, Color\n"
            f"class CccpChart(BaseChart):\n\n"
            f"    type = ChartType.Bar\n\n"
            f"    class labels:\n        grouped = {labels}\n\n"
            f"    class data:\n\n"
        )
        f.write(c)
        for coin, data in trans.items():
            c = (
                f"        class {coin.capitalize()}:\n"
                f"            data = {data}\n"
                f"            backgroundColor = Color.Hex(\"{colors[coin]}\")\n\n"
            )
            f.write(c)


def translate(data, filename='coins.txt'):
    """return result.json translated to get handled by pychartjs

    returns a tuple of (labels, translation)
    """

    with open(filename, 'r') as f:
        coins = [name.rstrip() for name in f]
    translated = {coin:[] for coin in coins}
    labels = []
    for daily in data:
        labels.append(daily['name'])
        for coin, n in daily['coin_stats'].items():
            translated[coin].append(n)
    return labels, translated

def get_colors(filename='colors.txt'):
    """return a dict() of color codes"""
    colors = {}
    with open(filename, 'r') as f:
        for c in [color.rstrip() for color in f]:
            k,v = c.split()
            colors[k]=v
    return colors

def main():
    with open('result.json', 'r') as f:
        data = json.load(f)
    colors = get_colors()
    labels, translated = translate(data)
    generate(labels, colors, translated)

if __name__ == '__main__':
    main()