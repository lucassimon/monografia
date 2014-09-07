var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res) {


	res.set('Content-Type', 'text/plain').
		send('loaderio-258034cd11bf2841160fe451c6850a09');
});

module.exports = router;
