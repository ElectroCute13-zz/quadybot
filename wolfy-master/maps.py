def translate(value, InputMin, InputMax, OutMin, OutMax):
    leftSpan = InputMax - InputMin
    rightSpan = OutMax - OutMin
    valueScaled = float(value - InputMin) / float(leftSpan)
    return OutMin + (valueScaled * rightSpan)
