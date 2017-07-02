var React = require('react');
var ReactDOM = require('react-dom');
var NoteStudentByDate = require('NoteStudentByDate');

const app_element = document.getElementById('app');
ReactDOM.render(
  React.createElement(NoteStudentByDate, {loginState: app_element.getAttribute("loginState"), userName: app_element.getAttribute("userName")}),
  app_element
);