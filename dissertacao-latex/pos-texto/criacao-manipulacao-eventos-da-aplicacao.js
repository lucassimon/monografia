var events = require('events')
var eventEmitter = new events.EventEmitter();

function mainLoop() {
	console.log('Starting application');
	eventEmitter.emit('AplicationStart');

	console.log('Running application');
	eventEmitter.emit('AplicationRun');

	console.log('Stopping application');
	eventEmitter.emit('AplicationStop');
}

function onApplicationStart() {
	console.log('Handling Application Start Event');
}

function onApplicationRun() {
	console.log('Handling Application Run Event');
}

function onApplicationStop() {
	console.log('Handling Application Stop Event');
}

eventEmitter.on('ApplicationStart', onApplicationStart);
eventEmitter.on('ApplicationRun', onApplicationRun);
eventEmitter.on('ApplicationStop', onApplicationStop);

mainLoop();
