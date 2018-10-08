#!/usr/bin/env node
// Blinks various LEDs
const Blynk = require('/usr/lib/node_modules/blynk-library');
const b = require('bonescript');
const util = require('util');

const LED0 = 'USR3';
const button = 'P9_12';
const LED1 = "P9_14";
b.pinMode(LED0, b.OUTPUT);
b.pinMode(button, b.INPUT);
b.pinMode(LED1, b.OUTPUT);

const AUTH = 'e37c55bf4e304966be5f154838f22dd1';


var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);
var v10 = new blynk.WidgetLED(10);
var v1 = new blynk.VirtualPin(1);

v0.on('write', function(param) {
    console.log('V0:', param[0]);
    b.digitalWrite(LED0, param[0]);
});

v1.on('write', function(param){
  var duty_cycle = parseFloat(param)/1023.0;
  console.log(duty_cycle, " ", parseFloat(param));
  b.analogWrite(LED1, duty_cycle);
});

v10.setValue(0);    // Initiallly off

b.attachInterrupt(button, toggle, b.CHANGE);

function toggle(x) {
    console.log("V10: ", x.value);
    x.value ? v10.turnOff() : v10.turnOn();
}
