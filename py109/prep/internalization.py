def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)
    match language:
        case 'en':
            if region == 'US':
                return 'Hey!'
            if region == 'GB':
                return 'Hello!'
            if region == 'AU':
                return 'Howdy!'
        case 'fr':
            return 'Salut!'


print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!