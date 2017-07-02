var React = require('react');
var CramHeader = require('CramHeader');
var CramFooter = require('CramFooter');
var QuizToPrintMain = require('QuizToPrintMain');

class QuizToPrint extends React.Component {
  render() {
    return (
      <div>
        <CramHeader loginState={this.props.loginState} userName={this.props.userName} />
        <QuizToPrintMain />
        <CramFooter />
      </div>
    )
  }
}

module.exports = QuizToPrint;