def write_term(latin_phrase, transcription_phrase, translation_phrase, source_phrase):
    new_term_line = f"{latin_phrase};{transcription_phrase};{translation_phrase};{source_phrase}"
    with open("./data/phrases.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_term_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    with open("./data/phrases.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))
