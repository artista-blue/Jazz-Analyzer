
class Tone:

    NUM_TONES = 12
    STEP = 360 / NUM_TONES

    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

    def calc_step(self, tone):
        a1 = self.angle
        a2 = tone.angle
        diff = (a2 - a1)
        if diff < 0:
            diff += 360
        return diff / self.STEP

    def __str__(self):
        return f'{self.name} ({self.angle})'


class Tones:

    TONE_NAMES_LIST = [
        ['C'],
        ['C#', 'Db'],
        ['D'],
        ['D#', 'Eb'],
        ['E'],
        ['F'],
        ['F#', 'Gb'],
        ['G'],
        ['G#', 'Ab'],
        ['A'],
        ['A#', 'Bb'],
        ['B', 'Cb']
    ]

    def __init__(self):
        self._init_tones()

    def _init_tones(self):
        self.tone_map = {}
        angle = 0
        for tone_names in self.TONE_NAMES_LIST:
            for tone_name in tone_names:
                tone = Tone(tone_name, angle)
                self.tone_map[tone_name] = tone
            angle += Tone.STEP

    def get(self, tone_name):
        return self.tone_map.get(tone_name)

    def __str__(self):
        return str(self.tone_map)
