from flask import jsonify,Flask

app = Flask(__name__)


work_notes_1 = [
    {
     'title': 'notes1',
     'text_content': 'text1',
     'id': '1',
     'tag_name': 'important',
     'in_archive': 'true',
     'date_of_create': '01.01.2001',
     'date_of_remove': '01.01.2002'
}
]


@app.route('/notes1')
def work_notes1():
    return jsonify({'work_notes_1': work_notes_1})



work_notes_2 = [
    {
     'title': 'notes2',
     'text_content': 'text2',
     'id': '2',
     'tag_name': 'todo_list',
     'in_archive': 'false',
     'date_of_create': '02.02.2002',
     'date_of_remove': '02.02.2003'
}
]


@app.route('/notes2')
def work_notes2():
    return jsonify({'work_notes_2': work_notes_2})



work_notes_3 = [
    {
     'title': 'notes3',
     'text_content': 'text3',
     'id': '3',
     'tag_name': 'question',
     'in_archive': 'true',
     'date_of_create': '03.03.2003',
     'date_of_remove': '03.03.2004'
}
]

@app.route('/notes3')
def work_notes3():
    return jsonify({'work_notes_3': work_notes_3})


archive_notes = [{

}]

@app.route('/archive')
def archive_notes():
    return jsonify(
        {
            'archive_notes1': work_notes_1,
            'archive_notes2':work_notes_3
        }
    )


app.run()

