var React = require('react');
var TableRowForNote = require('TableRowForNote');

class StudentNotes extends React.Component {
  constructor() {
    super();

    this.state = {
      notes: [],
      note_list: [],
    }

    this.getKind = this.getKind.bind(this);
    this.getStudyNote = this.getStudyNote.bind(this);
    this.checkStatus = this.checkStatus.bind(this);
    this.parseJSON = this.parseJSON.bind(this);
    this.storeData = this.storeData.bind(this);
    this.handleData = this.handleData.bind(this);
  }

  getKind(kind) {
    switch (kind) {
        case 'course': return '課程'
        case 'sign': return '點名'
        case 'homework': return '作業'
        case 'quiz': return '小考'
        case 'plan': return '讀計'
        case 'order': return '秩序'
        case 'bank': return '學費'
        case 'normal': return '一般'
      default: return 'no match'
    }
  }

  componentDidMount() {
    this.getStudyNote();
  }

  getStudyNote() {
    return fetch('/api/v1.0/note/get/student/' + this.props.student_id + '/8/', {
             accept: 'application/json',
             method: 'get',
             credentials: 'include'
           }).then(this.checkStatus)
             .then(this.parseJSON)
             .then(this.storeData)
             .then(this.handleData)
  }

  checkStatus(response) {
    if (response.status >= 200 && response.status < 300) {
      return response;
    } else {
      const error = new Error(`HTTP Error ${response.statusText}`);
      error.status = response.statusText;
      error.response = response;
      console.log(error);
      throw error;
    }
  }

  parseJSON(response) {
    return response.json();
  }

  storeData(data) {
    this.setState({
      notes: data,
    });
  }

  handleData() {
    var NoteList = this.state.notes['note_list'].map((note, index) => {
      return(
        <TableRowForNote
          key={note['id']}
          kind={this.getKind(note['kind'])}
          created_by={note['created_by']}
          content={note['content']}
          date={note['created_at']}
        />
      )
    })
    this.setState({
      note_list: NoteList,
    })
  }

  render() {
    const hStyle = {
      'textAlign': 'center',
    }

    const btnStyle = {
      'width': '100%',
    }

    return (
      <div>
        <div className="row"> <h5 style={hStyle}>Notes</h5></div>
        <div className="row">
          <div className="col-sm-12">
            <table className="table table-striped table-hover ">
              <thead>
                <tr>
                  <th>種類</th>
                  <th>內容</th>
                  <th>時間</th>
                  <th>作者</th>
                </tr>
              </thead>
              <tbody>
                {this.state.note_list}
              </tbody>
            </table>
          </div>
          <div>
            <a href="/student_note_more/" className="btn btn-primary" style={btnStyle}>More</a>
          </div>
        </div>
      </div>
    )
  }
}

module.exports = StudentNotes;