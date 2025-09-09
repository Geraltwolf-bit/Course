def main():
    import string

    n = int(input("Enter the numer: "))
    text = input("Enter your text: ")

    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()

    text_to_list = clean_text.split()

    list_with_ngrams = []
    for i in range(len(text_to_list)):
        list_with_ngrams.append(text_to_list[i:n+i])

    output = []
    for sublist in list_with_ngrams:
        output.append(' '.join(sublist))

    print(output)

main()