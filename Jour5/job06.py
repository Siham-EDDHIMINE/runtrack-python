def arrondir_notes(notes: list) -> list:
    notes_arrondies = []
    for note in notes:
        if note >= 38:
            multiple = (note // 5 + 1) * 5
            if multiple - note < 3:
                note = multiple
        notes_arrondies.append(note)
    return notes_arrondies
notes = [73, 67, 38, 33]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)