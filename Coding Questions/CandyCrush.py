# Remove 'rrr', 'ggg', 'bbb' from a string until they're all gone.

# Test Cases
# '' -> ''
# 'rgggb' -> 'rb'
# 'rrrgggbbb' - ''
# 'rgggbbbrr' -> 'rrr' -> ''
# 'rgbrgbrgb' -> 'rgbrgbrgb'
# 'rggbgggbbrrrgb' -> 'rggbbbgb' -> 'rgggb' -> 'rb'
# 'gggggggggggggggggggggg' -> 'g'

# Notes
# Strings are immutable and therefore it returns a string

def removeThreeInARow(s: 'string') -> 'string':
    done = False
    while not done:
        s = s.replace('rrr', '')
        s = s.replace('ggg', '')
        s = s.replace('bbb', '')
        if ('rrr' not in s) and ('ggg' not in s) and ('bbb' not in s):
            done = True
    return s

def main():
    test_cases = ['','rgggb','rrrgggbbb','rgggbbbrr','rgbrgbrgb', 'rggbgggbbrrrgb', 'gggggggggggggggggggggg']
    print(test_cases)
    for i in range(len(test_cases)):
        test_cases[i] = removeThreeInARow(test_cases[i])
    print(test_cases)

if __name__ == '__main__':
    main()

