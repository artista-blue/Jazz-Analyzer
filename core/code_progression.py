
class CodeProgression:

    @classmethod
    def is_251(cls, c1, c2, c3):
        step1 = c1['root'].calc_step(c2['root'])
        step2 = c2['root'].calc_step(c3['root'])
        # print(step1, step2)
        if step1 != 5 or step2 != 5:
            return None
        if c1['harmony'] == 'm7' and c2['harmony'] == '7' and c3['harmony'] == 'M7':
            return "Major 2 -> 5 -> 1"
        if c1['harmony'] == 'm7-5' and c2['harmony'] == '7' and c3['harmony'] == 'm7':
            return "Minor 2 -> 5 -> 1"
        return None
