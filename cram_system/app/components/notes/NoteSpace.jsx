var React = require('react');
var CramHeader = require('CramHeader');
var CramFooter = require('CramFooter');
var NoteSpaceMain = require('NoteSpaceMain');

class NoteSpace extends React.Component {
  render() {
    return (
      <div>
        <CramHeader />
        <NoteSpaceMain />
        <CramFooter />
      </div>
    )
  }
}

module.exports = NoteSpace;