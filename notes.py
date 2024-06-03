print('Input s as the command to stop writing notes, w to write a new note, and d to display notes.')
all_notes = []
while True:
    note_name = input('Note name:')
    note = input('Note:')
    note_total = [f"{note_name}: {note}"]
    all_notes.append(*note_total)
    command = input('command:')
    if command == 's':
        break
    if command == 'w':
        do_not_do_anything = True
    if command == 'd':
        for elem in all_notes:
            print(elem)
