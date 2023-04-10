class SVG:

    _params = []

    def __init__(self, name: str, width: int, height: int):
        self._name = name
        self._width = width
        self._height = height

    def save(self):
        s = f'<svg width="{self._width}" height="{self._height}" xmlns="http://www.w3.org/2000/svg">\n'

        for p in self._params:
            s += "\t" + p + "\n"

        s += '</svg>'

        # os.makedirs(f"SVG_Curves/{self._name}.svg", exist_ok=True)
        with open(f"SVG_Curves/{self._name}.svg", 'w+') as f:
            f.write(s)

    def append(self, obj):
        self._params.append(str(obj))
