var express = require('express');
var router = express.Router();

router.route('/v1/contatos')
	.get(function(req, res) {
		res.json({title:'Contatos - GET'});
	})
	.post(function(req, res) {
		res.json({title:'Contatos - POST'});
	});

module.exports = router;
