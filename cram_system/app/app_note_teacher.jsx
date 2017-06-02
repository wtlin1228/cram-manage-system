var React = require('react');
var ReactDOM = require('react-dom');
var NoteTeacher = require('NoteTeacher');

const app_element = document.getElementById('app');
ReactDOM.render(
  React.createElement(NoteTeacher, {loginState: app_element.getAttribute("loginState"), userName: app_element.getAttribute("userName")}),
  app_element
);
