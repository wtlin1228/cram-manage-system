var React = require('react');
var CramHeader = require('CramHeader');
var CramFooter = require('CramFooter');
var StudentNoteMoreMain = require('StudentNoteMoreMain');

class StudentNoteMore extends React.Component {
  render() {
    return (
      <div>
        <CramHeader />
        <StudentNoteMoreMain />
        <CramFooter />
      </div>
    )
  }
}

module.exports = StudentNoteMore;
