var React = require('react');
var CramHeader = require('CramHeader');
var CramFooter = require('CramFooter');
var HomeworkMain = require('HomeworkMain');

class Homework extends React.Component {
  render() {
    return (
      <div>
        <CramHeader />
        <HomeworkMain />
        <CramFooter />
      </div>
    )
  }
}

module.exports = Homework;
