'use strict';
// #region Algemeen
//const IP = prompt('geef publiek IP', 'http://127.0.0.1:5000');
const LOCAL_DOMAINS = ["localhost", "127.0.0.1", 5000];

if (LOCAL_DOMAINS.includes(window.location.hostname))
  alert("It's a local server!");
  
var socket = io();
let servomotor;
console.log('test');
const listenToButton = function() {
  servomotor.addEventListener('click', function() {
    console.log('click op de drukknop');
    socket.emit('button');
  });
};

const getSocketConnection = function() {
  socket = io('http://127.0.0.1' + ':5000');
};
const init = function() {
  servomotor = document.querySelector('#servo');
  getSocketConnection();
  listenToButton();
};

const showSensorData = function(data) {
  sensors = JSON.parse(data);
  table = document.querySelector('.js-table');

  for (let i = 0; i < sensors.length; ++i) {
    table.innerHTML += `
          <div class="c-table-row">
                              <div class="c-table-cell c-cell">
                                  <div class="c-table-cell--heading">Entry ID</div>
                                  <div class="c-table-cell--content js-Date">${
                                    sensors[i]['EntryID']
                                  }</div>
                              </div>
                              <div class="c-table-cell c-cell">
                                  <div class="c-table-cell--heading">Sensor ID</div>
                                  <div class="c-table-cell--content ">${
                                    sensors[i]['SensorID']
                                  }</div>
                              </div>
                              <div class="c-table-cell c-cell topic-cell">
                                  <div class="c-table-cell--content js-Title">${
                                    sensors[i]['Name']
                                  }</div>
                              </div>
                              <div class="c-table-cell c-cell">
                                  <div class="c-table-cell--heading">Time</div>
                                  <div class="c-table-cell--content">${
                                    sensors[i]['Time']
                                  }
                                  </div>
                              </div>
                              <div class="c-table-cell c-table-cell--foot c-cell">
                                  <div class="c-table-cell--heading">Value</div>
                                  <div class="c-table-cell--content">${
                                    sensors[i]['Value']
                                  }</div>
                              </div>
                          </div>
      `;
  }
};

document.addEventListener('DOMContentLoaded', function() {
  console.info('DOM geladen');
  console.log('test');
  init();
});
// #endregion
