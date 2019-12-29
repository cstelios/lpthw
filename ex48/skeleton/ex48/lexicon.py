mapping = {
    'direction' : ["north", "south", "east", "west", "down", "up", "left", "right", "back"],
    'verb' : ["go", "stop", "kill", "eat", "run"],
    'stop' : ["the", "in", "of", "from", "at", "it"],
    'noun' : ["door", "bear", "princess", "cabinet", "honey"]
    }
mapping_categories = mapping.keys()

def scan(input):
    result = []

    for word in input.split():
        try:
            result.append(('number', int(word)))
        except ValueError:
            for category, item in mapping.items():
                if word.lower() in item:
                    existing_category = category
                    break
                else:
                    existing_category = 'error'

            result.append((existing_category, word.lower()))

    return result

#print(scan(input("> ")))
