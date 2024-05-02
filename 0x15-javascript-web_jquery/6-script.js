#!/usr/bin/node
$('document').ready(() => {
  $('#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});

